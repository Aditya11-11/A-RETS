# A-RETS: AI-Driven Resonant Transmutation & Screening Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**A-RETS** is a full-stack computational framework designed to model, optimize, and control the photonuclear transmutation reaction $^{196}\text{Hg}(\gamma, n)^{195}\text{Au}$ near the Giant Dipole Resonance (GDR) threshold. 

By integrating physics-informed neural networks (PINNs) and Reinforcement Learning (RL), A-RETS provides a sub-millisecond surrogate for complex nuclear cross-section calculations, enabling real-time plasma stability control.

## Statement of Need
Traditional Monte Carlo transport methods for nuclear reactions are computationally expensive, often requiring hours for a single parameter sweep. A-RETS addresses this by providing a high-fidelity ML surrogate (PyTorch MLP) that achieves $R^2 > 0.97$ while being $100\times$ faster. This speed enables the use of Proximal Policy Optimization (PPO) agents to manage plasma confinement in Penning traps—a task impossible with slow, classical simulators.

## Key Features
* **Physics Engine:** Implements Breit-Wigner resonance modeling, Gamow tunneling factors, and Debye electron screening.
* **AI Surrogate:** A Physics-Informed MLP for rapid isotope yield prediction.
* **RL Control:** A PPO-based agent trained for stable plasma confinement, outperforming PID baselines.
* **Interactive UI:** A Streamlit-based dashboard for live parameter exploration and visualization.

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
## Installation
```bash
git clone [https://github.com/yourusername/A-RETS.git](https://github.com/yourusername/A-RETS.git)
cd A-RETS
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Repository Structure
- `physics/`: Core physics modules (Q-value, Cross-section, Gamow factor).
- `ml/`: Surrogate model and RL environment/training.
- `api/`: FastAPI backend.
- `dashboard/`: Streamlit interactive UI.
- `simulation/`: Synthetic data generation.
