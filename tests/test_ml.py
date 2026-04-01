import torch
import pytest
from ml.surrogate_model import SurrogateModel

def test_model_inference_shape():
    """Verify the surrogate model accepts 3 inputs and returns 1 output."""
    model = SurrogateModel(input_dim=3, hidden_dim=64)
    dummy_input = torch.randn(5, 3) # Batch of 5 samples
    output = model(dummy_input)
    
    assert output.shape == (5, 1)

def test_model_loading():
    """Check if the saved model file exists and is loadable."""
    import os
    model_path = "ml/surrogate_model.pt"
    if os.path.exists(model_path):
        model = SurrogateModel()
        model.load_state_dict(torch.load(model_path))
        assert not model.training # Ensure it's in eval mode
    else:
        pytest.skip("Model weight file not found, skipping load test.")
