from stable_baselines3 import PPO
from ml.rl_env import PlasmaTrapEnv
import argparse

def train_rl(timesteps=100000):
    env = PlasmaTrapEnv()
    model = PPO('MlpPolicy', env, verbose=1,
                n_steps=2048, batch_size=64,
                learning_rate=3e-4, gamma=0.99)
    
    print(f"Training RL agent for {timesteps} steps...")
    model.learn(total_timesteps=timesteps)
    model.save('ml/ppo_plasma_agent')
    print("RL agent saved to ml/ppo_plasma_agent.zip")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--timesteps", type=int, default=10000)
    args = parser.parse_args()
    train_rl(args.timesteps)
