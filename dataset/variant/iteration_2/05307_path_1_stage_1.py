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

ax.stackplot(years, energy_consumption, labels=[
    'Solar', 'Wind', 'Hydro', 'Biomass', 'Geo'
], colors=['#ffcc00', '#66c2a5', '#8da0cb', '#fc8d62', '#e78ac3'], alpha=0.85)

ax.set_title('Renewable Energy (2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy (TWh)', fontsize=14)

ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Sources', fontsize=12)

ax.set_xticks(np.arange(2010, 2021, 1))

total_energy_consumption = np.sum(energy_consumption, axis=0)
ax.plot(years, total_energy_consumption, color='black', linewidth=2, label='Total')
ax.text(2020, total_energy_consumption[-1], f'{total_energy_consumption[-1]:.1f}', fontsize=10, color='black', ha='right')

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()