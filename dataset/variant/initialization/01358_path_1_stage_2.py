import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

regions = ["Northern Region", "Coastal Region", "Desert Region", "Urban Region", "Mountain Region"]

efficiency = np.array([
    [15, 17, 18, 20, 22], 
    [18, 19, 20, 21, 22], 
    [20, 21, 23, 25, 27], 
    [16, 18, 19, 21, 22], 
    [14, 15, 16, 17, 18]   
])

variability = np.array([
    [1.5, 1.6, 1.7, 1.8, 2.0],
    [1.2, 1.3, 1.4, 1.5, 1.6],
    [1.8, 2.0, 2.2, 2.3, 2.5],
    [1.3, 1.4, 1.5, 1.6, 1.7],
    [1.1, 1.2, 1.3, 1.4, 1.5]  
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['blue', 'green', 'orange', 'red', 'purple']

for i in range(len(regions)):
    ax.errorbar(
        years, efficiency[i], yerr=variability[i], 
        fmt='-o', color=colors[i], capsize=5, linewidth=2, markersize=6, alpha=0.9
    )

ax.set_title('Exploration of Renewable Energy Adoption:\n'
             'Analyzing Efficiency and Variability Across Regions (2018-2022)', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Efficiency (%)', fontsize=12)

plt.tight_layout()
plt.show()