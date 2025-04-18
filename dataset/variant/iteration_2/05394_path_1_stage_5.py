import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Data for three star systems
luminosity_star_system1 = np.array([0.01, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35])
temperature_star_system1 = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380])

luminosity_star_system2 = np.array([0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0])
temperature_star_system2 = np.array([400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600])

# Adding made-up data for star system 3
luminosity_star_system3 = np.array([0.12, 0.18, 0.24, 0.28, 0.34, 0.4, 0.45, 0.5, 0.55, 0.6])
temperature_star_system3 = np.array([230, 250, 270, 290, 310, 330, 350, 370, 390, 410])

# Density estimates using Gaussian KDE
kde_luminosity_star_system1 = gaussian_kde(luminosity_star_system1)
kde_temperature_star_system1 = gaussian_kde(temperature_star_system1)
kde_luminosity_star_system2 = gaussian_kde(luminosity_star_system2)
kde_temperature_star_system2 = gaussian_kde(temperature_star_system2)
kde_luminosity_star_system3 = gaussian_kde(luminosity_star_system3)
kde_temperature_star_system3 = gaussian_kde(temperature_star_system3)

# Create grid over which to evaluate the KDE
luminosity_grid1 = np.linspace(min(luminosity_star_system1) - 0.1, max(luminosity_star_system1) + 0.1, 100)
temperature_grid1 = np.linspace(min(temperature_star_system1) - 20, max(temperature_star_system1) + 20, 100)
density_luminosity1 = kde_luminosity_star_system1(luminosity_grid1)
density_temperature1 = kde_temperature_star_system1(temperature_grid1)

luminosity_grid2 = np.linspace(min(luminosity_star_system2) - 0.1, max(luminosity_star_system2) + 0.1, 100)
temperature_grid2 = np.linspace(min(temperature_star_system2) - 20, max(temperature_star_system2) + 20, 100)
density_luminosity2 = kde_luminosity_star_system2(luminosity_grid2)
density_temperature2 = kde_temperature_star_system2(temperature_grid2)

luminosity_grid3 = np.linspace(min(luminosity_star_system3) - 0.1, max(luminosity_star_system3) + 0.1, 100)
temperature_grid3 = np.linspace(min(temperature_star_system3) - 20, max(temperature_star_system3) + 20, 100)
density_luminosity3 = kde_luminosity_star_system3(luminosity_grid3)
density_temperature3 = kde_temperature_star_system3(temperature_grid3)

# Create plot
fig, ax = plt.subplots(3, 1, figsize=(10, 21), sharex=False)

# Plot for Star System 1
ax[0].plot(density_luminosity1, luminosity_grid1, color='blue')
ax[0].plot(density_temperature1, temperature_grid1, color='green')

# Plot for Star System 2
ax[1].plot(density_luminosity2, luminosity_grid2, color='red')
ax[1].plot(density_temperature2, temperature_grid2, color='orange')

# Plot for Star System 3
ax[2].plot(density_luminosity3, luminosity_grid3, color='purple')
ax[2].plot(density_temperature3, temperature_grid3, color='brown')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()