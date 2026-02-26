import numpy as np
import pandas as pd
import h5py
import argparse
from physics.reaction_rate import calculate_reaction_rate

def generate_synthetic_data(num_samples=50000):
    print(f"Generating {num_samples} samples...")
    
    # Ranges for parameters
    E_photon_range = (1.0, 15.0)  # MeV
    photon_flux_range = (1e10, 1e15) # photons/cm^2/s
    electron_density_range = (0.0, 1e20) # cm^-3
    mag_field_range = (0.1, 10.0) # T
    target_thickness_range = (0.01, 1.0) # cm
    temp_range = (0.1, 10.0) # keV

    data = []
    
    # Physics constants for Hg-196
    E_res = 6.6
    Gamma = 0.5
    sigma_peak = 500.0 # mb
    target_density = 4e22 # atoms/cm^3 (approx for liquid Hg)

    for i in range(num_samples):
        E_p = np.random.uniform(*E_photon_range)
        flux = np.random.uniform(*photon_flux_range)
        n_e = np.random.uniform(*electron_density_range)
        B = np.random.uniform(*mag_field_range)
        thick = np.random.uniform(*target_thickness_range)
        T = np.random.uniform(*temp_range)
        
        # Calculate yield (simplified grid integration)
        E_grid = np.linspace(E_p - 0.5, E_p + 0.5, 50)
        rate = calculate_reaction_rate(E_grid, flux, target_density * thick, E_res, Gamma, sigma_peak, n_e)
        
        data.append([E_p, flux, n_e, B, thick, T, rate])
        
        if (i+1) % 5000 == 0:
            print(f"Progress: {i+1}/{num_samples}")

    columns = ['photon_energy', 'photon_flux', 'electron_density', 'magnetic_field', 'target_thickness', 'temperature', 'yield']
    df = pd.DataFrame(data, columns=columns)
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=1000) # Default small for testing
    parser.add_argument("--output", type=str, default="data/synthetic_dataset.h5")
    args = parser.parse_args()
    
    df = generate_synthetic_data(args.samples)
    df.to_hdf(args.output, key='data', mode='w')
    print(f"Dataset saved to {args.output}")
