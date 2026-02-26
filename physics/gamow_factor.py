import numpy as np

# Physical Constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)
e = 1.602176634e-19 # Elementary charge (C)
alpha = 1/137.036   # Fine structure constant
c = 2.99792458e8    # Speed of light (m/s)
eV = 1.602176634e-19 # 1 eV in Joules

def gamow_factor(Z1: int, Z2: int, E_keV: float,
                  electron_density: float = 0.0, T_e_keV: float = 1.0) -> float:
    """
    Z1, Z2          : atomic numbers of projectile and target
    E_keV           : center-of-mass energy in keV
    electron_density: plasma density (cm⁻³) for Debye screening
    T_e_keV         : electron temperature in keV
    """
    # Reduced mass (approximation for photonuclear η/n, but here we model tunneling)
    # For Hg-196 (γ,n), the "tunneling" part is often used for charged particle emission,
    # but the prompt requested Debye screening for the Penning trap.
    
    # Debye screening length (cm)
    # λ_D = sqrt(ε0 * k_B * T_e / (n_e * e^2))
    # In approximate plasma units: λ_D ≈ 743 * sqrt(T_e[eV] / n_e[cm^-3]) cm
    T_e_eV = T_e_keV * 1000
    if electron_density > 0:
        lambda_D = 743 * np.sqrt(T_e_eV / electron_density)
        # Screening potential U_screen in eV
        # U_screen = Z1 * Z2 * e^2 / lambda_D (in cgs/Gaussian or SI)
        # Using eV friendly form: U_s ≈ 1.44e-7 * Z1 * Z2 / lambda_D [eV] if lambda_D is in cm
        U_screen = (1.44e-7 * Z1 * Z2) / lambda_D
    else:
        U_screen = 0.0

    E_eff_eV = E_keV * 1000 + U_screen
    
    # Generic Gamow factor: G = pi * Z1 * Z2 * alpha * sqrt(2 * mu * c^2 / E)
    # For our reaction (gamma, n), tunneling is actually for the outgoing particle if charged,
    # but the request specifically mentioned Debye screening reducing barrier height.
    # We'll use a representative mass mu ≈ 1 amu for the tunneling particle (neutron/proton)
    mu_c2_mev = 931.5
    G = np.pi * Z1 * Z2 * alpha * np.sqrt(2 * mu_c2_mev * 1e6 / E_eff_eV)
    
    # Probability = exp(-G) where G = 2 * pi * eta
    # Our G calculation already includes the 2*pi factors
    return np.exp(-G)
