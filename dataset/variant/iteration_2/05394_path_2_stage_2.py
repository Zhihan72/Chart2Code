import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

luminosity_star_system1 = np.array([0.01, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35])
temperature_star_system1 = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380])

luminosity_star_system2 = np.array([0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0])
temperature_star_system2 = np.array([400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600])

kde_temp1 = gaussian_kde(temperature_star_system1)
kde_temp2 = gaussian_kde(temperature_star_system2)

temperature_grid = np.linspace(200, 600, 100)

density_temp1 = kde_temp1(temperature_grid)
density_temp2 = kde_temp2(temperature_grid)

fig, ax = plt.subplots(1, 2, figsize=(14, 7), sharey=True)

# Subplot for Star System 2 moved to the first position
ax[0].plot(density_temp2, temperature_grid, color='red', alpha=0.7)
ax[0].fill_betweenx(temperature_grid, density_temp2, color='red', alpha=0.1)
ax[0].scatter([0]*len(temperature_star_system2), temperature_star_system2, color='red', edgecolor='black', s=80, alpha=0.7)
ax[0].set_title("Star System 2: Temperature Density", fontsize=12, fontweight='bold', pad=10)
ax[0].set_ylabel("Temperature (K)", fontsize=10)
ax[0].set_xlabel("Density", fontsize=10)
ax[0].grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Subplot for Star System 1 moved to the second position
ax[1].plot(density_temp1, temperature_grid, color='blue', alpha=0.7)
ax[1].fill_betweenx(temperature_grid, density_temp1, color='blue', alpha=0.1)
ax[1].scatter([0]*len(temperature_star_system1), temperature_star_system1, color='blue', edgecolor='black', s=80, alpha=0.7)
ax[1].set_title("Star System 1: Temperature Density", fontsize=12, fontweight='bold', pad=10)
ax[1].set_xlabel("Density", fontsize=10)
ax[1].grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

fig.suptitle("Temperature Density Distribution in Different Star Systems", fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()