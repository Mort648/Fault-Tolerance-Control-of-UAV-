import numpy as np

# Physical constants
m = 1.0
g = 9.81
I = 0.01
L = 0.2

# Time settings
dt = 0.01
T = 10.0
N = int(T / dt)

# Target values
z_target = 2.0
theta_target = 0.0

# PID gains
Kp_z = 15.0
Ki_z = 0.5
Kd_z = 10.0

Kp_theta = 10.0
Ki_theta = 0.1
Kd_theta = 2.0
