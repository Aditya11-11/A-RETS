import gymnasium as gym
from gymnasium import spaces
import numpy as np

class PlasmaTrapEnv(gym.Env):
    """
    Simulation of a Penning trap plasma confinement.
    Goal: Maintain radial and axial stability under gamma-ray bombardment.
    """
    def __init__(self):
        super(PlasmaTrapEnv, self).__init__()
        
        # Observation space: 
        # [ion_radial_displacement, ion_axial_velocity, plasma_temp, field_B, field_E, reaction_rate_t]
        self.observation_space = spaces.Box(
            low=np.array([0, -10, 0, 0, -1000, 0]),
            high=np.array([10, 10, 100, 10, 1000, 1e12]),
            dtype=np.float32
        )
        
        # Action space: [delta_B (-0.1 to +0.1 T), delta_E (-500 to +500 V/m)]
        self.action_space = spaces.Box(
            low=np.array([-0.1, -500]),
            high=np.array([0.1, 500]),
            dtype=np.float32
        )
        
        self.state = None
        self.steps = 0
        self.max_steps = 1000
        
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        # Initial state: stable center, low temperature, nominal fields
        self.state = np.array([0.1, 0.0, 1.0, 5.0, 100.0, 1e6], dtype=np.float32)
        self.steps = 0
        return self.state, {}
        
    def step(self, action):
        delta_B, delta_E = action
        self.steps += 1
        
        # Update fields
        self.state[3] = np.clip(self.state[3] + delta_B, 0, 10)
        self.state[4] = np.clip(self.state[4] + delta_E, -1000, 1000)
        
        # Simplified dynamics: 
        # radial displacement increases with temp, decreases with B field strength
        self.state[0] += (self.state[2] * 0.1) / (self.state[3] + 1) - 0.05
        self.state[0] = np.clip(self.state[0], 0, 15)
        
        # axial velocity affected by E field
        self.state[1] += delta_E * 0.001
        
        # temperature increases with reaction rate (bombardment)
        self.state[2] += self.state[5] * 1e-12
        
        # Confinement check
        failed = self.state[0] > 5.0 or abs(self.state[1]) > 8.0
        
        reward = 1.0
        if failed:
            reward = -100.0
            terminated = True
        else:
            terminated = self.steps >= self.max_steps
            # Bonus for high reaction rate stability
            reward += self.state[5] * 1e-9
            
        truncated = False
        return self.state, reward, terminated, truncated, {}

    def render(self):
        pass
