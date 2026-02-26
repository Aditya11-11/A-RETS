import streamlit as st
import numpy as np
import plotly.graph_objects as go
import sys
import os

# Ensure the project root is in sys.path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from physics.breit_wigner import breit_wigner_cross_section
from physics.reaction_rate import calculate_reaction_rate
from physics.qvalue import compute_q_value, get_threshold_energy

st.set_page_config(page_title="A-RETS Dashboard", layout="wide")

st.title("🛡️ A-RETS: AI-Driven Resonant Transmutation Simulator")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("🔬 Parameters")
    
    st.subheader("FEL / Beam")
    photon_energy = st.slider("Photon Energy (MeV)", 1.0, 15.0, 6.6, 0.1)
    photon_flux = st.number_input("Photon Flux (γ/cm²/s)", value=1e13, format="%.2e")
    
    st.subheader("Plasma & Target")
    electron_density = st.number_input("Electron Density (cm⁻³)", value=1e18, format="%.2e")
    mag_field = st.slider("Magnetic Field (T)", 0.1, 10.0, 5.0, 0.1)
    target_thickness = st.slider("Target Thickness (cm)", 0.01, 1.0, 0.1, 0.01)
    temperature = st.slider("Plasma Temp (keV)", 0.1, 10.0, 1.0, 0.1)

    st.subheader("☢️ Q-Value Calculator")
    m_p = st.number_input("Parent Mass (amu)", value=195.9658, format="%.4f")
    m_d = st.number_input("Daughter Mass (amu)", value=194.9659, format="%.4f")
    m_e = st.number_input("Emitted Mass (amu)", value=1.0087, format="%.4f")
    
    q_val = compute_q_value(m_p, m_d, m_e)
    e_th = get_threshold_energy(q_val, m_p)

with col2:
    st.header("📊 Physics Visualization")
    
    # Breit-Wigner Cross Section Plot
    E_res = 6.6
    Gamma = 0.5
    sigma_peak = 500.0
    
    E_range = np.linspace(1, 15, 500)
    sigma = breit_wigner_cross_section(E_range, E_res, Gamma, sigma_peak)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=E_range, y=sigma, name="Cross Section σ(E)", line=dict(color='cyan', width=2)))
    fig.add_vline(x=photon_energy, line_dash="dash", line_color="orange", annotation_text="Current Energy")
    
    fig.update_layout(
        title="Breit-Wigner Resonance Peak (Hg-196)",
        xaxis_title="Energy (MeV)",
        yaxis_title="Cross Section (mb)",
        template="plotly_dark"
    )
    st.plotly_chart(fig, width='stretch')
    
    # Reaction Rate Display
    target_density = 4e22
    E_grid = np.linspace(photon_energy - 0.5, photon_energy + 0.5, 100)
    rate = calculate_reaction_rate(E_grid, photon_flux, target_density * target_thickness, 
                                   E_res, Gamma, sigma_peak, electron_density)
    
    st.metric("Predicted Reaction Rate", f"{rate:.4e} rx/cm³/s")
    
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        st.metric("Q-Value", f"{q_val:.4f} MeV")
    with col_q2:
        st.metric("Threshold Energy", f"{e_th:.4f} MeV")
    
    # Placeholder for RL Confinement Area
    st.subheader("🤖 Plasma Confinement (RL Agent)")
    stability = np.clip(1.0 - (temperature * 0.05 / (mag_field + 0.1)), 0, 1)
    status_color = "green" if stability > 0.8 else "orange" if stability > 0.5 else "red"
    st.markdown(f"Status: <span style='color:{status_color}'>{'Stable' if stability > 0.8 else 'Unstable'} (Score: {stability:.2f})</span>", unsafe_allow_html=True)
    
    confinement_data = np.random.normal(0, 1.0 - stability, 100).cumsum()
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(y=confinement_data, name="Ion Displacement", line=dict(color='magenta')))
    fig2.update_layout(title="Ion Displacement Over Time", template="plotly_dark")
    st.plotly_chart(fig2, width='stretch')

st.sidebar.info("A-RETS: Researching Resonant Photonuclear Reactions at 6.6 MeV.")
