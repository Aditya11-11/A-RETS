# A-RETS
### AI-Driven Resonant Transmutation & Screening Simulator

A-RETS is a full-stack research simulator for modeling resonant nuclear transmutation, specifically the ¹⁹⁶Hg → ¹⁹⁵Au photonuclear reaction.

## Features
- **Physics Engine**: Breit-Wigner resonance modeling, Gamow tunneling with Debye screening.
- **AI Surrogate**: PyTorch MLP for rapid yield prediction.
- **RL Control**: PPO agent for plasma stability in Penning traps.
- **Dashboard**: Interactive Streamlit UI for parameter exploration.

## Quick Start
1. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Generate synthetic data**:
   ```bash
   python simulation/dataset_generator.py --samples 5000
   ```
3. **Train surrogate model**:
   ```bash
   python ml/train_surrogate.py --epochs 20
   ```
4. **Launch Dashboard**:
   ```bash
   streamlit run dashboard/app.py
   ```

## Repository Structure
- `physics/`: Core physics modules (Q-value, Cross-section, Gamow factor).
- `ml/`: Surrogate model and RL environment/training.
- `api/`: FastAPI backend.
- `dashboard/`: Streamlit interactive UI.
- `simulation/`: Synthetic data generation.
