import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually changing the values within each energy group
solar_energy = np.array([5, 6, 7, 9, 12, 14, 16, 19, 21, 24, 29])
wind_energy = np.array([6, 8, 11, 14, 15, 19, 23, 30, 32, 38, 43])
hydro_energy = np.array([32, 33, 34, 33, 35, 35, 36, 37, 38, 39, 38])
biomass_energy = np.array([4, 3, 6, 7, 6, 9, 10, 11, 13, 11, 14])
geothermal_energy = np.array([2, 2, 3, 4, 4, 5, 4, 6, 5, 7, 6])

total_renewable_energy = solar_energy + wind_energy + hydro_energy + biomass_energy + geothermal_energy

data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy])

fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Bio', 'Geo'],
              colors=['#E59400', '#76C2C5', '#417F79', '#836EAA', '#A1A615'], alpha=0.7)

ax1.plot(years, total_renewable_energy, color='darkgreen', marker='x', linestyle='-', linewidth=2.5, label='Total Renewables')

ax1.set_title('Renewable Growth\n2010-2020', fontsize=17, fontweight='medium', ha='right')
ax1.set_xlabel('Year', fontsize=13, color='dimgray')
ax1.set_ylabel('Production (TWh)', fontsize=13, color='dimgray')

ax1.legend(loc='lower right', title='Types', fontsize=11, frameon=True)
ax1.grid(alpha=0.5, linestyle=':')

plt.tight_layout()
plt.show()