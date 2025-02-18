import numpy as np
import matplotlib.pyplot as plt

# Data with manually altered order
centuries = np.arange(1400, 2300, 200)
energy_flux = np.array([70, 50, 130, 100, 90, 110])  # Manually shuffled
crystal_formation = np.array([15, 10, 35, 25, 22, 32])  # Manually shuffled

# Creating figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot
ax.scatter(energy_flux, crystal_formation, color='purple', edgecolor='black', s=150, marker='*', alpha=0.7, label='Data')

# Title and labels
ax.set_title("Mystical Energy vs. Crystals (1400-2200)", fontsize=16, fontweight='bold')
ax.set_xlabel("Energy Flux", fontsize=14)
ax.set_ylabel("Formation Rate", fontsize=14)

# Annotations
for i, century in enumerate(centuries):
    ax.annotate(f'{century}', (energy_flux[i], crystal_formation[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

# Trend line
fit = np.polyfit(energy_flux, crystal_formation, 1)
fit_fn = np.poly1d(fit)
ax.plot(energy_flux, fit_fn(energy_flux), color='blue', linestyle='--', linewidth=2, label='Trend')

# Grid and ticks
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xticks(np.arange(40, 141, 20))
ax.set_yticks(np.arange(0, 41, 5))

# Legend
ax.legend(loc='upper left', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()