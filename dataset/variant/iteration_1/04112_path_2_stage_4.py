import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2005', '2007', '2009', '2011', '2013', '2015', '2017', '2019', '2021', '2023'])

species_a_landing_density = np.array([30, 45, 33, 35, 65, 50, 60, 55, 37, 62])
species_b_landing_density = np.array([27, 20, 30, 42, 25, 35, 38, 45, 32, 40])
species_c_landing_density = np.array([17, 10, 23, 15, 25, 13, 30, 27, 32, 35])

bar_width = 0.25
indices = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffled the colors for each species
ax.barh(indices, species_a_landing_density, height=bar_width, color='green', label='Species A')
ax.barh(indices + bar_width, species_b_landing_density, height=bar_width, color='blue', label='Species B')
ax.barh(indices + 2 * bar_width, species_c_landing_density, height=bar_width, color='red', label='Species C')

ax.set_yticks(indices + bar_width)
ax.set_yticklabels(years)

ax.set_title('Horizontal Bar Chart of Landing Densities (2005 - 2023)', fontsize=16, fontweight='bold', color='navy')
ax.set_ylabel('Year', fontsize=12)
ax.set_xlabel('Landing Density (Birds per km²)', fontsize=12)

ax.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()