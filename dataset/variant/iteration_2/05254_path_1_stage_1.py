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
ax1.stackplot(years, data, labels=['Solar Energy', 'Wind Energy', 'Hydro Energy', 'Biomass Energy', 'Geothermal Energy'], 
              colors=['#FF4500', '#ADD8E6', '#98FB98', '#DDA0DD', '#FFD700'], alpha=0.8)

ax1.plot(years, total_renewable_energy, color='black', marker='o', linestyle='--', linewidth=2, label='Total Renewable Energy')

ax1.set_title('Evolution of Renewable Energy Sources\n(2010-2020)', fontsize=16, fontweight='bold', ha='center')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14)

max_year = years[np.argmax(total_renewable_energy)]
max_value = np.max(total_renewable_energy)
ax1.annotate(f'Max Energy: {max_value} TWh\nin {max_year}', xy=(max_year, max_value),
             xytext=(max_year-3, max_value-10),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center', color='black')

ax1.legend(loc='upper left', title='Renewable Energy Sources', fontsize=12, frameon=False)
ax1.grid(alpha=0.3)

plt.tight_layout()
plt.show()