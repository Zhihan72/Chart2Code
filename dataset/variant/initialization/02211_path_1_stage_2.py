import numpy as np
import matplotlib.pyplot as plt

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_types = ['Solar', 'Wind', 'Hydro', 'Bioenergy']

energy_percentages = np.array([
    [30, 25, 35, 10],  # Africa
    [40, 20, 25, 15],  # Asia
    [25, 40, 20, 15],  # Europe
    [35, 30, 25, 10],  # North America
    [20, 35, 30, 15],  # South America
    [50, 20, 20, 10]   # Oceania
])

colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']

fig, ax = plt.subplots(figsize=(12, 8))

for i, continent in enumerate(continents):
    bottom = 0
    for j, energy_type in enumerate(energy_types):
        ax.barh(continent, energy_percentages[i][j], left=bottom, color=colors[j])
        bottom += energy_percentages[i][j]

ax.set_xlabel('Percentage')
ax.set_title('Mapping the Future:\nRenewable Energy Adoption Across the Continents (2050 Projections)', fontsize=14, fontweight='bold')

plt.tight_layout()

plt.show()