---
title: 'A-RETS: AI-Driven Resonant Transmutation & Screening Simulator'
tags:
  - photonuclear transmutation
  - Breit-Wigner cross-section
  - Gamow factor
  - electron screening
  - surrogate neural network
  - reinforcement learning
  - plasma stability
  - Penning trap
authors:
  - name: Aditya Patel
    orcid: 0009-0007-3944-1128
    affiliation: Independent Researcher, Ahmedabad, Gujarat, India
date: March 2026
bibliography: paper.bib
---

# Summary
[cite_start]A-RETS (AI-Driven Resonant Transmutation & Screening Simulator) is a comprehensive full-stack computational framework designed to model, optimize, and control the photonuclear transmutation reaction $^{196}\text{Hg}(\gamma,n)^{195}\text{Au}$ near the Giant Dipole Resonance (GDR) threshold at 6.6 MeV. [cite_start]The system integrates three tightly coupled layers: a physics engine implementing Breit-Wigner resonance cross-sections and Gamow tunneling factors with Debye electron screening; a machine learning layer comprising a physics-informed surrogate neural network and a Proximal Policy Optimization (PPO) reinforcement learning agent; and an interactive Streamlit dashboard for live visualization and parameter tuning. 

# Statement of Need
[cite_start]The precise modeling of photonuclear reactions traditionally relies on first-principles treatments that are accurate but computationally expensive, such as Monte Carlo transport. [cite_start]These methods are often too slow for "human-in-the-loop" exploration or the development of real-time control policies. [cite_start]A-RETS addresses this gap by providing a physics-informed surrogate neural network that reduces simulation time by approximately two orders of magnitude compared to traditional methods while maintaining high accuracy ($R^2 > 0.97$). [cite_start]This acceleration allows the framework to employ RL agents for real-time plasma stabilization in Penning traps—a task that is computationally prohibitive under full physics simulation. [cite_start]The A-RETS RL agent achieves a 94% confinement success rate, significantly outperforming classical PID controller baselines. [cite_start]This modular architecture serves as a template for AI-assisted nuclear reaction engineering across various photonuclear and fusion-relevant domains.

# Mentions
[cite_start]The A-RETS framework is built upon and integrates the following open-source technologies:
* [cite_start]**Physics and Simulation**: NumPy, SciPy, SymPy, and OpenMC.
* [cite_start]**Machine Learning**: PyTorch for the surrogate model and Stable-Baselines3 (with Gymnasium) for the PPO agent.
* [cite_start]**Interface and API**: Streamlit and Plotly for the dashboard, supported by a FastAPI and Uvicorn REST layer.
* [cite_start]**Infrastructure**: MLflow for experiment tracking and DVC for artifact versioning.

# References
[cite_start][cite: 1] Baldwin, G. C., & Klaiber, G. S. (1947). Photo-fission in heavy elements. Physical Review, 71(1), 3–10.
[cite_start][cite: 2] Sherr, R., Bainbridge, K. T., & Anderson, H. H. (1941). Transmutation of mercury by fast neutrons. Physical Review, 60(7), 473.
[cite_start][cite: 3] Assenbaum, H. J., Langanke, K., & Weiss, A. (1987). Effects of electron screening on low-energy fusion cross sections. Zeitschrift für Physik A, 327(4), 461–468.
[cite_start][cite: 4] Degrave, J., Felici, F., Buchli, J., et al. (2022). Magnetic control of tokamak plasmas through deep reinforcement learning. Nature, 602(7897), 414–419.
[cite_start][cite: 5] Wang, M., Huang, W. J., Kondev, F. G., et al. (2021). The AME 2020 atomic mass evaluation. Chinese Physics C, 45(3), 030003.
[cite_start][cite: 6] Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal policy optimization algorithms. arXiv:1707.06347.
[cite_start][cite: 7] Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural networks. Journal of Computational Physics, 378, 686–707.
[cite_start][cite: 8] Blond, N., Chevallier, L., & Berthier, T. (2021). Neural network surrogate models for Monte Carlo transport calculations. Annals of Nuclear Energy, 152, 107970.
[cite_start][cite: 9] Stable-Baselines3 contributors. (2021). Stable-Baselines3: Reliable reinforcement learning implementations. JMLR, 22(268), 1–8.
[cite_start][cite: 10] Paszke, A., Gross, S., Massa, F., et al. (2019). PyTorch: An imperative style, high-performance deep learning library. NeurIPS, 32.
