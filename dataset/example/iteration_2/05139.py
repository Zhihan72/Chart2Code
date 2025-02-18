import numpy as np
import matplotlib.pyplot as plt

# Backstory: This chart shows the correlation between two quirky fictional elements: "Energy Flux" (a measure of mystical energy) and "Crystal Formation" (formation rate of magical crystals) as recorded by a group of wizards over several centuries.

# Data: Years recorded and corresponding mystical data
centuries = np.arange(1400, 2300, 200)
energy_flux = np.array([50, 70, 100, 130, 110, 90])
crystal_formation = np.array([10, 15, 25, 35, 32, 22])

# Creating figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot
scatter = ax.scatter(energy_flux, crystal_formation, color='purple', edgecolor='black', s=150, marker='*', alpha=0.7, label='Mystical Data')

# Title and labels
ax.set_title("Chronicles of Mystical Energy and Crystal Formation\n(1400 - 2200 AD)", fontsize=16, fontweight='bold')
ax.set_xlabel("Energy Flux (Mystical Index)", fontsize=14)
ax.set_ylabel("Crystal Formation Rate (per Century)", fontsize=14)

# Add annotations for each data point
for i, century in enumerate(centuries):
    ax.annotate(f'{century} AD', (energy_flux[i], crystal_formation[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

# Adding a linear trend line
# Fit a linear trend using polyfit with degree 1 (linear)
fit = np.polyfit(energy_flux, crystal_formation, 1)
fit_fn = np.poly1d(fit)
ax.plot(energy_flux, fit_fn(energy_flux), color='blue', linestyle='--', linewidth=2, label='Trend Line')

# Adding grid and customizing ticks
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xticks(np.arange(40, 141, 20))
ax.set_yticks(np.arange(0, 41, 5))

# Adding legend
ax.legend(loc='upper left', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()