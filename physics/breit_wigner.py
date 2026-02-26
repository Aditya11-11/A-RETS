import numpy as np

def breit_wigner_cross_section(E: np.ndarray, E_res: float,
                                Gamma: float, sigma_peak: float) -> np.ndarray:
    """
    E       : photon energy array (MeV)
    E_res   : resonance energy (MeV) ~6.6 MeV for Hg-196
    Gamma   : resonance width (MeV)
    sigma_peak : peak cross-section (mb)
    """
    numerator = sigma_peak * (Gamma / 2)**2
    denominator = (E - E_res)**2 + (Gamma / 2)**2
    return numerator / denominator
