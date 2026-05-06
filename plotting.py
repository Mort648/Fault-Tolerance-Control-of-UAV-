import matplotlib.pyplot as plt
import numpy as np
from parameters import *

def plot_results(z_normal, theta_normal, z_ftc, theta_ftc):

    t = np.linspace(0, T, N)

    plt.figure(figsize=(12, 5))

    # Altitude plot
    plt.subplot(1, 2, 1)
    plt.plot(t, z_normal, label='Without FTC', linestyle='--')
    plt.plot(t, z_ftc, label='With FTC')
    plt.title("Altitude vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.legend()
    plt.grid(True)

    # Angle plot
    plt.subplot(1, 2, 2)
    plt.plot(t, theta_normal, label='Without FTC', linestyle='--')
    plt.plot(t, theta_ftc, label='With FTC')
    plt.title("Angle vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (degrees)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
