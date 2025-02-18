import numpy as np
import matplotlib.pyplot as plt

# Data
centuries = np.arange(1400, 2300, 200)
energy_flux = np.array([50, 70, 100, 130, 110])
crystal_formation = np.array([10, 15, 25, 35, 32])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot
ax.scatter(energy_flux, crystal_formation, color='purple', edgecolor='black', s=150, marker='*', alpha=0.7)

# Randomly altered textual elements
ax.set_title("Enchanted Energies and Crystal Growth Analysis\n(1400 - 2200 AD)", fontsize=16, fontweight='bold')
ax.set_xlabel("Mystical Flow (Energy Index)", fontsize=14)
ax.set_ylabel("Rate of Crystalization (each Century)", fontsize=14)

# Annotate points with randomly altered labels
annotations = ['14th Century Marker', '16th Marker', '18th Era', '20th Span', '22nd Time Stamp']
for i, annotation in enumerate(annotations):
    ax.annotate(annotation, (energy_flux[i], crystal_formation[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

# Regression line
fit = np.polyfit(energy_flux, crystal_formation, 1)
fit_fn = np.poly1d(fit)
ax.plot(energy_flux, fit_fn(energy_flux), color='blue', linestyle='--', linewidth=2)

# Adjust ticks
ax.set_xticks(np.arange(40, 141, 20))
ax.set_yticks(np.arange(0, 41, 5))

plt.tight_layout()
plt.show()