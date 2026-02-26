import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from torch.utils.data import DataLoader, TensorDataset
from ml.surrogate_model import YieldPredictor
import argparse

def train(epochs=100, batch_size=32, data_path="data/synthetic_dataset.h5"):
    # Load data
    try:
        df = pd.read_hdf(data_path, key='data')
    except:
        print(f"Error: {data_path} not found. Run dataset_generator.py first.")
        return

    features = df.drop('yield', axis=1).values
    targets = df['yield'].values.reshape(-1, 1)

    X = torch.tensor(features, dtype=torch.float32)
    y = torch.tensor(targets, dtype=torch.float32)

    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = YieldPredictor(input_size=X.shape[1])
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print("Starting training...")
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for batch_X, batch_y in loader:
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        if (epoch+1) % 10 == 0:
            print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(loader):.4e}")

    torch.save(model.state_dict(), "ml/surrogate_model.pt")
    print("Model saved to ml/surrogate_model.pt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()
    train(args.epochs, args.batch_size)
