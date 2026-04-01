from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "A-RETS API Operational"}

def test_prediction_endpoint():
    payload = {"energy": 6.6, "flux": 1e13, "density": 1e18}
    response = client.post("/predict", params=payload)
    
    assert response.status_code == 200
    assert "predicted_reaction_rate" in response.json()
