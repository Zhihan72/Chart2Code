import matplotlib.pyplot as plt
import numpy as np

# Data construction
years = np.arange(2020, 2031)
solar_energy = np.array([10, 14, 18, 22, 27, 33, 40, 48, 57, 67, 78])
wind_energy = np.array([15, 18, 22, 26, 31, 37, 44, 51, 59, 68, 78])
hydro_energy = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
geothermal_energy = np.array([5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25])

# Stacked data array
data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Updated colors for plot
ax.stackplot(years, data, labels=['Solar Energy', 'Wind Energy', 'Hydraulic Energy', 'Geothermal Energy'],
             colors=['#e57373', '#ba68c8', '#7986cb', '#64b5f6'], alpha=0.8)

# Adding labels, title, and legend
ax.set_title('Transition to Renewable Energy Sources (2020-2030)', fontsize=15, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (in TeraWatts)', fontsize=12)
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, frameon=False)

# Customizing ticks and grid
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 221, 20))
ax.grid(True, linestyle='--', alpha=0.5)

# Adding annotation to highlight significant growth
ax.annotate('Significant Surge in Solar', xy=(2025, 33), xytext=(2022, 80),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10,
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.8))

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()