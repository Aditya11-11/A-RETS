import pytest
import numpy as np
from physics.breit_wigner import breit_wigner_cross_section
from physics.qvalue import compute_q_value, get_threshold_energy
from physics.gamow_factor import calculate_gamow_factor

def test_breit_wigner_peak():
    """Verify the cross-section is highest at the resonance energy (6.6 MeV)."""
    E_res = 6.6
    Gamma = 0.5
    sigma_peak = 500.0
    
    sigma_at_res = breit_wigner_cross_section(E_res, E_res, Gamma, sigma_peak)
    sigma_off_res = breit_wigner_cross_section(8.0, E_res, Gamma, sigma_peak)
    
    assert sigma_at_res == sigma_peak
    assert sigma_at_res > sigma_off_res

def test_q_value_mercury():
    """Test Q-value calculation for Hg-196 -> Au-195 + n."""
    # Masses in amu
    m_p = 195.9658
    m_d = 194.9659
    m_e = 1.0087
    
    q = compute_q_value(m_p, m_d, m_e)
    # Expected Q is approx -8.19 MeV for this reaction
    assert pytest.approx(q, rel=1e-2) == -8.19

def test_gamow_probability():
    """Ensure Gamow tunneling probability is bounded between 0 and 1."""
    prob = calculate_gamow_factor(energy_mev=5.0, z1=80, z2=1, mass_amu=1.0)
    assert 0 <= prob <= 1
