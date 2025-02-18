import numpy as np
import matplotlib.pyplot as plt

centuries = np.arange(1400, 2300, 200)
energy_flux = np.array([70, 50, 130, 100, 90, 110])
crystal_formation = np.array([15, 10, 35, 25, 22, 32])

fig, ax = plt.subplots(figsize=(14, 8))

# Apply a single color consistently across all data groups
common_color = 'purple'

ax.scatter(energy_flux, crystal_formation, color=common_color, edgecolor='black', s=150, marker='*', alpha=0.7)

ax.set_title("Mystical Energy vs. Crystals (1400-2200)", fontsize=16, fontweight='bold')
ax.set_xlabel("Energy Flux", fontsize=14)
ax.set_ylabel("Formation Rate", fontsize=14)

for i, century in enumerate(centuries):
    ax.annotate(f'{century}', (energy_flux[i], crystal_formation[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

# Fit line using the same common color
fit = np.polyfit(energy_flux, crystal_formation, 1)
fit_fn = np.poly1d(fit)
ax.plot(energy_flux, fit_fn(energy_flux), color=common_color, linestyle='--', linewidth=2)

plt.tight_layout()
plt.show()