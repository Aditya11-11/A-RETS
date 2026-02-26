import numpy as np

AMU_TO_MEV = 931.494  # 1 atomic mass unit in MeV

def compute_q_value(m_parent: float, m_daughter: float, m_emitted: float) -> float:
    """
    Returns Q-value in MeV. Negative = endothermic.
    m_parent: mass of parent nucleus in amu
    m_daughter: mass of daughter nucleus in amu
    m_emitted: mass of emitted particle in amu (e.g., proton or neutron)
    """
    delta_mass = (m_parent - m_daughter - m_emitted)
    return delta_mass * AMU_TO_MEV

def get_threshold_energy(q_value: float, m_target: float) -> float:
    """
    Returns threshold energy in MeV for a photonuclear reaction.
    q_value: Q-value in MeV (usually negative for endothermic)
    m_target: mass of target nucleus in amu
    """
    if q_value >= 0:
        return 0.0
    # E_th = -Q * (1 + m_photon/m_target)
    # Since m_photon is effectively 0 relative to m_target in this context
    # E_th ≈ -Q
    return abs(q_value) * (1 + 1e-6) # Small correction factor
