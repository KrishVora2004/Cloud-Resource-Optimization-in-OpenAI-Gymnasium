# envs/cloud_env.py

import gymnasium as gym
from gymnasium import spaces
import numpy as np


class CloudEnv(gym.Env):
    """
    Custom Cloud Resource Optimization Environment
    (Scope-agnostic skeleton)
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super(CloudEnv, self).__init__()

        # -------------------------------
        # Action Space
        # 0 -> Scale Down
        # 1 -> Maintain
        # 2 -> Scale Up
        # -------------------------------
        self.action_space = spaces.Discrete(3)

        # -------------------------------
        # Observation Space (PLACEHOLDERS)
        # [load, utilization, performance, scaling_state]
        # Values normalized between 0 and 1
        # -------------------------------
        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=(4,),
            dtype=np.float32
        )

        # Internal state
        self.state = None
        self.current_step = 0
        self.max_steps = 200

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        # Initial dummy state
        self.state = np.array([
            0.5,  # load indicator
            0.5,  # resource utilization
            0.5,  # performance indicator
            0.5   # scaling indicator
        ], dtype=np.float32)

        self.current_step = 0

        return self.state, {}

    def step(self, action):
        self.current_step += 1

        # -------------------------------
        # Placeholder dynamics
        # (This WILL be replaced later)
        # -------------------------------
        load, util, perf, scale = self.state

        if action == 0:      # Scale Down
            util -= 0.05
            perf -= 0.03
            scale -= 0.05

        elif action == 2:    # Scale Up
            util += 0.05
            perf += 0.02
            scale += 0.05

        # Maintain → minimal drift
        load += np.random.uniform(-0.02, 0.02)

        # Clamp values
        load = np.clip(load, 0.0, 1.0)
        util = np.clip(util, 0.0, 1.0)
        perf = np.clip(perf, 0.0, 1.0)
        scale = np.clip(scale, 0.0, 1.0)

        self.state = np.array([load, util, perf, scale], dtype=np.float32)

        # -------------------------------
        # Placeholder Reward Logic
        # -------------------------------
        reward = (
            + perf                 # prefer good performance
            - abs(util - 0.6)      # penalize under/over utilization
        )

        # -------------------------------
        # Termination conditions
        # -------------------------------
        terminated = False
        truncated = self.current_step >= self.max_steps

        return self.state, reward, terminated, truncated, {}

    def render(self):
        print(
            f"Step: {self.current_step}, "
            f"State: {self.state}"
        )

    def close(self):
        pass
