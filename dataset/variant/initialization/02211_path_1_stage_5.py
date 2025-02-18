import numpy as np
import matplotlib.pyplot as plt

continents = ['Asia', 'Europe', 'Africa', 'South America', 'North America']
energy_types = ['Hydro', 'Bioenergy', 'Solar', 'Wind']

energy_percentages = np.array([
    [25, 15, 40, 20],  # Asia
    [40, 15, 25, 20],  # Europe
    [35, 10, 30, 25],  # Africa
    [30, 15, 20, 35],  # South America
    [25, 10, 35, 30]   # North America
])

# Changed the order of colors
colors = ['#FF6347', '#32CD32', '#1E90FF', '#FFD700']

fig, ax = plt.subplots(figsize=(12, 8))

for i, continent in enumerate(continents):
    bottom = 0
    for j, energy_type in enumerate(energy_types):
        ax.barh(continent, energy_percentages[i][j], left=bottom, color=colors[j])
        bottom += energy_percentages[i][j]

ax.set_xlabel('Energy Mix (%)')
ax.set_title('Renewable Use in\nGlobal Regions by 2050', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()