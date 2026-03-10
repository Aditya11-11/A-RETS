---
title: 'A-RETS: AI-Driven Resonant Transmutation & Screening Simulator'
tags:
  - Python
  - Physics
  - Nuclear Transmutation
  - Reinforcement Learning
  - Surrogate Modeling
authors:
  - name: Author Name
    orcid: 0000-0000-0000-0000
    affiliation: 1
affiliations:
  - name: Institution Name
    index: 1
date: 20 February 2026
bibliography: paper.bib
---

# Summary

A-RETS (AI-Driven Resonant Transmutation & Screening Simulator) is an open-source research tool designed to model and optimize resonant nuclear transmutation processes, specifically the $^{196}\text{Hg}(\gamma,n)^{195}\text{Au}$ reaction at the 6.6 MeV resonance threshold. The software integrates a high-fidelity physics engine with machine learning surrogates and reinforcement learning controllers to simulate reaction yields and plasma stability in experimental setups like Penning traps.

# Statement of Need

Research into resonant nuclear transmutation requires precise modeling of cross-sections, tunneling probabilities, and plasma screening effects. Traditional simulation tools (e.g., Monte Carlo transport) are often computationally expensive, hindering rapid parameter space exploration. A-RETS addresses this by providing:

1.  **Physics-Informed Surrogates**: A PyTorch-based multi-layer perceptron (MLP) trained on synthetic physics data to provide instantaneous yield predictions.
2.  **Debye-Screening Integration**: Implementation of Gamow factor modifications due to electron screening in high-density plasma environments.
3.  **Autonomous Control**: A Reinforcement Learning (RL) agent using Proximal Policy Optimization (PPO) to simulate the real-time stabilization of ion confinement during gamma-ray bombardment.

This tool is intended for researchers in nuclear physics, plasma science, and isotope production who require an interactive and optimized environment for experimental design.

# Mathematics

The cross-section $\sigma(E)$ is modeled using the Breit-Wigner formula near the Giant Dipole Resonance:

$$\sigma(E) = \sigma_{peak} \frac{(\Gamma/2)^2}{(E - E_{res})^2 + (\Gamma/2)^2}$$

Tunneling probabilities include the Debye screening potential $U_{screen}$:

$$E_{eff} = E + U_{screen}$$

# Acknowledgements

Initial code structures and the data visualization scripts were developed with assistance of **Antigravity**, an agentic AI coding assistant developed by Google DeepMind, and subsequently verified and refined by the author to ensure physical accuracy.

# References
[1] Baldwin, G. C., & Klaiber, G. S. (1947). Photo-fission in heavy elements. Physical Review, 71(1), 3–
10.
[2] Sherr, R., Bainbridge, K. T., & Anderson, H. H. (1941). Transmutation of mercury by fast neutrons.
Physical Review, 60(7), 473.
[3] Assenbaum, H. J., Langanke, K., & Weiss, A. (1987). Effects of electron screening on low-energy
fusion cross sections. Zeitschrift für Physik A, 327(4), 461–468.
[4] Degrave, J., Felici, F., Buchli, J., et al. (2022). Magnetic control of tokamak plasmas through deep
reinforcement learning. Nature, 602(7897), 414–419.
[5] Wang, M., Huang, W. J., Kondev, F. G., et al. (2021). The AME 2020 atomic mass evaluation.
Chinese Physics C, 45(3), 030003.
[6] Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal policy
optimization algorithms. arXiv:1707.06347.
[7] Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural networks. Journal of
Computational Physics, 378, 686–707.
[8] Blond, N., Chevallier, L., & Berthier, T. (2021). Neural network surrogate models for Monte Carlo
transport calculations. Annals of Nuclear Energy, 152, 107970.
[9] Stable-Baselines3 contributors. (2021). Stable-Baselines3: Reliable reinforcement learning
implementations. JMLR, 22(268), 1–8.
[10] Paszke, A., Gross, S., Massa, F., et al. (2019). PyTorch: An imperative style, high-performance deep
learning library. NeurIPS, 32.
