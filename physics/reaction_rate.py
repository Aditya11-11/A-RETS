import numpy as np
from .breit_wigner import breit_wigner_cross_section
from .gamow_factor import gamow_factor

def calculate_reaction_rate(E_photon: np.ndarray, 
                            photon_flux: float, 
                            target_density: float,
                            E_res: float, 
                            Gamma: float, 
                            sigma_peak: float,
                            electron_density: float = 0.0) -> float:
    """
    R = n * Phi * integral(sigma(E) * f(E) dE)
    E_photon: array of photon energies (MeV)
    photon_flux: Phi (photons/cm^2/s)
    target_density: n (atoms/cm^3)
    """
    # Simple cross-section (Breit-Wigner)
    sigma = breit_wigner_cross_section(E_photon, E_res, Gamma, sigma_peak)
    
    # Apply Gamow factor as a transparency/probability modifier (simplified model)
    # Z1=1 (representative), Z2=80 (Hg)
    Z1, Z2 = 1, 80
    G_factors = np.array([gamow_factor(Z1, Z2, E*1000, electron_density) for E in E_photon])
    
    # Effective cross-section
    sigma_eff = sigma * G_factors
    
    # Integrate (assuming E_photon is a fine grid)
    dE = E_photon[1] - E_photon[0] if len(E_photon) > 1 else 1.0
    integral = np.sum(sigma_eff * dE)
    
    # Reaction rate R (reactions/cm^3/s)
    # sigma is in mb, convert to cm^2 (1 mb = 1e-27 cm^2)
    R = target_density * photon_flux * integral * 1e-27
    return R
