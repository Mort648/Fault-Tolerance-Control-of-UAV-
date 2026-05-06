from simulation import simulate
from plotting import plot_results

# Run simulations
z_normal, theta_normal = simulate(ftc_enabled=False)
z_ftc, theta_ftc = simulate(ftc_enabled=True)

# Plot results
plot_results(z_normal, theta_normal, z_ftc, theta_ftc)
