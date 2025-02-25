import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = [4, 5, 7, 10, 14, 18, 23, 29, 36, 44, 53]
wind_energy = [3, 4, 6, 9, 13, 17, 22, 28, 35, 43, 52]
hydro_energy = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
biomass_energy = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

energy_consumption = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, energy_consumption, labels=[
    'Solar', 'Wind', 'Hydro', 'Biomass'
], colors=['#66c2a5', '#8da0cb', '#fc8d62', '#ffcc00'], alpha=0.75)

ax.set_title('Renewable Energy (2010-2020)', fontsize=14, fontweight='normal', pad=10)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy (TWh)', fontsize=12)

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1), title='Sources', fontsize=10)

ax.set_xticks(np.arange(2010, 2021, 1))

total_energy_consumption = np.sum(energy_consumption, axis=0)
ax.plot(years, total_energy_consumption, color='darkgreen', linewidth=1.5, linestyle='-', marker='o', markersize=5, label='Total')
ax.text(2020, total_energy_consumption[-1], f'{total_energy_consumption[-1]:.1f}', fontsize=9, color='darkgreen', ha='right')

ax.grid(True, linestyle='-', alpha=0.3)

plt.tight_layout()

plt.show()