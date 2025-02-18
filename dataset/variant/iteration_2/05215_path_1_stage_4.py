import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [5, 7, 10, 14, 18, 23, 29, 35, 42, 50, 58]
wind = [4, 6, 9, 13, 17, 22, 27, 33, 40, 47, 55]
hydro = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
geothermal = [1, 2, 3, 4, 6, 8, 11, 14, 17, 21, 25]
biomass = [3, 4, 5, 6, 8, 10, 13, 16, 19, 23, 27]
tidal = [1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 15] # New dataset for Tidal Energy
nuclear = [0, 0, 0, 1, 2, 2, 4, 6, 8, 11, 14] # New dataset for Nuclear Energy

fig, ax1 = plt.subplots(figsize=(16, 9))

ax1.plot(years, solar, marker='x', linestyle='-', color='#DAF7A6', linewidth=2, label='Sunlight')
ax1.plot(years, wind, marker='p', linestyle='-.', color='#FFC300', linewidth=2, label='Breeze')
ax1.plot(years, hydro, marker='H', linestyle=':', color='#C70039', linewidth=2, label='Water Flow')
ax1.plot(years, geothermal, marker='v', linestyle='--', color='#900C3F', linewidth=2, label='Earth Heat')
ax1.plot(years, biomass, marker='o', linestyle='-', color='#581845', linewidth=2, label='Plant Power')
ax1.plot(years, tidal, marker='D', linestyle='-', color='#FF5733', linewidth=2, label='Tidal Energy') # Plotting Tidal Energy
ax1.plot(years, nuclear, marker='s', linestyle='--', color='#900C3F', linewidth=2, label='Nuclear Energy') # Plotting Nuclear Energy

ax1.set_title('Diverse Growth of Energy Sources (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Percentage Contribution (%)', fontsize=14)
ax1.set_xticks(years)
ax1.grid(visible=False)
ax1.legend(title='Energy Types', loc='upper right', fontsize=12)

ax1.annotate('Rapid Rise of Sunlight', xy=(2018, 42), xytext=(2017, 51),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='#DAF7A6')
ax1.annotate('Increasing Earth Heat', xy=(2016, 8), xytext=(2014, 16),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='#900C3F')

plt.tight_layout()
plt.show()