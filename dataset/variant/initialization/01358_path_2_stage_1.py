import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
regions = ["Northern Region", "Coastal Region", "Desert Region", "Urban Region"]

# Shuffled average efficiency for each region
efficiency = np.array([
    [18, 15, 22, 17, 20],  # Northern Region (shuffled)
    [21, 18, 22, 19, 20],  # Coastal Region (shuffled)
    [27, 23, 25, 21, 20],  # Desert Region (shuffled)
    [21, 16, 22, 18, 19]   # Urban Region (shuffled)
])

# Shuffled variability for each region
variability = np.array([
    [1.7, 2.0, 1.8, 1.5, 1.6],  # Northern Region (shuffled)
    [1.6, 1.2, 1.5, 1.3, 1.4],  # Coastal Region (shuffled)
    [2.5, 2.2, 2.3, 2.0, 1.8],  # Desert Region (shuffled)
    [1.7, 1.3, 1.6, 1.4, 1.5]   # Urban Region (shuffled)
])

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['blue', 'green', 'orange', 'red']

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