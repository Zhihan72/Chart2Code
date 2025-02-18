import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [4, 5, 7, 10, 14, 18, 23, 29, 36, 44, 53]
wind_energy = [3, 4, 6, 9, 13, 17, 22, 28, 35, 43, 52]
hydro_energy = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
biomass_energy = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
geothermal_energy = [1, 1.5, 2, 3, 4, 6, 8, 10, 13, 15, 18]
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