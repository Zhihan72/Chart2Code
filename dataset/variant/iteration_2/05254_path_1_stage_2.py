import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = np.array([2, 3, 4, 6, 8, 12, 15, 18, 22, 26, 30])
wind_energy = np.array([5, 7, 10, 13, 16, 20, 25, 29, 35, 40, 45])
hydro_energy = np.array([30, 31, 32, 33, 34, 34, 35, 36, 37, 37, 38])
biomass_energy = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
geothermal_energy = np.array([1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7])

total_renewable_energy = solar_energy + wind_energy + hydro_energy + biomass_energy + geothermal_energy

data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy])

fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.stackplot(years, data, labels=['Solar Energy', 'Wind', 'Hydro', 'Biomass', 'Geo'],
              colors=['#E59400', '#76C2C5', '#417F79', '#836EAA', '#A1A615'], alpha=0.7)

ax1.plot(years, total_renewable_energy, color='darkgreen', marker='x', linestyle='-', linewidth=2.5, label='Total Renewable Energy')

ax1.set_title('Renewable Energy Growth\n(2010-2020)', fontsize=17, fontweight='medium', ha='right')
ax1.set_xlabel('Years', fontsize=13, color='dimgray')
ax1.set_ylabel('Production (TWh)', fontsize=13, color='dimgray')

ax1.legend(loc='lower right', title='Energy Types', fontsize=11, frameon=True)
ax1.grid(alpha=0.5, linestyle=':')

plt.tight_layout()
plt.show()