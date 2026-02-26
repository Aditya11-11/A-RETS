from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import torch
from physics.reaction_rate import calculate_reaction_rate
from ml.surrogate_model import load_model

app = FastAPI(title="A-RETS API", description="AI-Driven Resonant Transmutation & Screening Simulator API")

# Load model (placeholder path)
model = None
try:
    model = load_model("ml/surrogate_model.pt")
except:
    pass

class PhysicsParams(BaseModel):
    photon_energy: float
    photon_flux: float
    electron_density: float = 0.0
    target_thickness: float = 0.1

class MLParams(BaseModel):
    features: list[float] # [photon_energy, flux, n_e, B, thickness, T]

@app.get("/")
async def root():
    return {"message": "A-RETS API is active"}

@app.post("/physics/reaction_rate")
async def get_reaction_rate(params: PhysicsParams):
    E_grid = np.linspace(params.photon_energy - 0.5, params.photon_energy + 0.5, 100)
    # Default Hg-196 params
    E_res, Gamma, sigma_peak = 6.6, 0.5, 500.0
    target_density = 4e22
    
    rate = calculate_reaction_rate(E_grid, params.photon_flux, target_density * params.target_thickness, 
                                   E_res, Gamma, sigma_peak, params.electron_density)
    return {"reaction_rate": float(rate)}

@app.post("/ml/predict")
async def predict_yield(params: MLParams):
    if model is None:
        raise HTTPException(status_code=503, detail="Surrogate model not loaded")
    
    with torch.no_grad():
        inputs = torch.tensor([params.features], dtype=torch.float32)
        prediction = model(inputs)
    return {"predicted_yield": float(prediction.item())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
