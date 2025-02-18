import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

# Add new region "Mountain Region"
regions = ["Northern Region", "Coastal Region", "Desert Region", "Urban Region", "Mountain Region"]

# Include data for the new region, "Mountain Region"
efficiency = np.array([
    [15, 17, 18, 20, 22],  # Northern Region
    [18, 19, 20, 21, 22],  # Coastal Region
    [20, 21, 23, 25, 27],  # Desert Region
    [16, 18, 19, 21, 22],  # Urban Region
    [14, 15, 16, 17, 18]   # Mountain Region
])

# Include variability for the new region
variability = np.array([
    [1.5, 1.6, 1.7, 1.8, 2.0],  # Northern Region
    [1.2, 1.3, 1.4, 1.5, 1.6],  # Coastal Region
    [1.8, 2.0, 2.2, 2.3, 2.5],  # Desert Region
    [1.3, 1.4, 1.5, 1.6, 1.7],  # Urban Region
    [1.1, 1.2, 1.3, 1.4, 1.5]   # Mountain Region
])

fig, ax = plt.subplots(figsize=(12, 8))

# Extend colors to accommodate the new region
colors = ['blue', 'green', 'orange', 'red', 'purple']

# Plot data for each region
for i, region in enumerate(regions):
    ax.errorbar(
        years, efficiency[i], yerr=variability[i], label=region,
        fmt='-o', color=colors[i], capsize=5, linewidth=2, markersize=6, alpha=0.9
    )

ax.set_title('Exploration of Renewable Energy Adoption:\n'
             'Analyzing Efficiency and Variability Across Regions (2018-2022)', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Efficiency (%)', fontsize=12)

ax.legend(title='Regions', loc='upper left')
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()