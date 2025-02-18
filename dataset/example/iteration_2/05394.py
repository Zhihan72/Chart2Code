import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Backstory: Exploring the Luminosity and Temperature Distribution of Exoplanets in Two Different Star Systems

# Data: Luminosity (Solar Luminosity units) and Temperature (Kelvin) of Exoplanets in Two Hypothetical Star Systems
luminosity_star_system1 = np.array([0.01, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35])
temperature_star_system1 = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380])

luminosity_star_system2 = np.array([0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0])
temperature_star_system2 = np.array([400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600])

# Create the density estimates for both star systems using Gaussian KDE
kde_star_system1 = gaussian_kde(np.vstack([luminosity_star_system1, temperature_star_system1]))
kde_star_system2 = gaussian_kde(np.vstack([luminosity_star_system2, temperature_star_system2]))

# Create a grid over which we evaluate the KDE
luminosity_grid = np.linspace(0, 1, 100)
temperature_grid = np.linspace(200, 600, 100)
L, T = np.meshgrid(luminosity_grid, temperature_grid)
positions = np.vstack([L.ravel(), T.ravel()])

density_star_system1 = np.reshape(kde_star_system1(positions).T, L.shape)
density_star_system2 = np.reshape(kde_star_system2(positions).T, L.shape)

# Create the plot with subplots for each star system
fig, ax = plt.subplots(1, 2, figsize=(14, 7), sharey=True)

# Plot for Star System 1
contour1 = ax[0].contourf(L, T, density_star_system1, cmap='Blues', alpha=0.7)
ax[0].scatter(luminosity_star_system1, temperature_star_system1, color='blue', edgecolor='black', s=80, alpha=0.7)
ax[0].set_title("Star System 1: Luminosity vs Temperature", fontsize=12, fontweight='bold', pad=10)
ax[0].set_xlabel("Luminosity (Solar Luminosity units)", fontsize=10)
ax[0].set_ylabel("Temperature (K)", fontsize=10)
ax[0].grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
fig.colorbar(contour1, ax=ax[0], orientation='vertical', label='Density')

# Plot for Star System 2
contour2 = ax[1].contourf(L, T, density_star_system2, cmap='Reds', alpha=0.7)
ax[1].scatter(luminosity_star_system2, temperature_star_system2, color='red', edgecolor='black', s=80, alpha=0.7)
ax[1].set_title("Star System 2: Luminosity vs Temperature", fontsize=12, fontweight='bold', pad=10)
ax[1].set_xlabel("Luminosity (Solar Luminosity units)", fontsize=10)
ax[1].grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
fig.colorbar(contour2, ax=ax[1], orientation='vertical', label='Density')

# Main title for the entire figure
fig.suptitle("Stellar Wonders:\nDensity Distribution of Exoplanet Characteristics in Different Star Systems", fontsize=16, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()