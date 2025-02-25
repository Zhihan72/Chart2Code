import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Manually shuffled data within each energy source
solar_energy = [14, 23, 44, 5, 4, 53, 36, 10, 29, 18, 7]
wind_energy = [22, 4, 3, 13, 52, 9, 28, 35, 43, 6, 17]
hydro_energy = [28, 24, 40, 22, 26, 38, 30, 34, 36, 32, 20]
biomass_energy = [24, 12, 30, 10, 14, 28, 18, 20, 16, 22, 26]
geothermal_energy = [6, 15, 13, 3, 1, 18, 10, 8, 4, 1.5, 2]
energy_consumption = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, energy_consumption, colors=['#d95f02', '#1b9e77', '#7570b3', '#e7298a', '#66a61e'], alpha=0.9)

ax.set_xticks(np.arange(2010, 2021, 2))

total_energy_consumption = np.sum(energy_consumption, axis=0)
ax.plot(years, total_energy_consumption, color='red', linestyle='-.', linewidth=1.5, marker='o', markersize=5)

ax.grid(True, linestyle=':', color='gray', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(2)

plt.tight_layout()
plt.show()