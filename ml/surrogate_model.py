import torch
import torch.nn as nn

class YieldPredictor(nn.Module):
    def __init__(self, input_size=6):
        super(YieldPredictor, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.GELU(),
            nn.BatchNorm1d(128),
            nn.Linear(128, 256),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(256, 128),
            nn.GELU(),
            nn.Linear(128, 1),
            nn.ReLU()  # Yield must be >= 0
        )
        
    def forward(self, x):
        return self.net(x)

def load_model(path, input_size=6, device='cpu'):
    model = YieldPredictor(input_size)
    try:
        model.load_state_dict(torch.load(path, map_checkpoint=device))
        model.eval()
    except:
        print(f"Warning: Could not load model from {path}. Using fresh model.")
    return model.to(device)
