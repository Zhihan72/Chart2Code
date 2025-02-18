import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([5, 6, 8, 11, 15, 20, 26, 35, 47, 60, 75])
wind_energy = np.array([10, 12, 15, 20, 25, 33, 40, 52, 65, 80, 100])
hydropower_energy = np.array([30, 32, 35, 36, 37, 38, 39, 40, 41, 42, 44])
geothermal_energy = np.array([2, 3, 3, 4, 5, 6, 7, 9, 12, 15, 18])  # New data series

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
bar_offset = np.array([-1.5, -0.5, 0.5, 1.5]) * bar_width

ax.bar(years + bar_offset[0], solar_energy, width=bar_width, label='Solar Energy', color='lightblue', edgecolor='black')
ax.bar(years + bar_offset[1], wind_energy, width=bar_width, label='Wind Energy', color='seagreen', edgecolor='black')
ax.bar(years + bar_offset[2], hydropower_energy, width=bar_width, label='Hydropower', color='gold', edgecolor='black')
ax.bar(years + bar_offset[3], geothermal_energy, width=bar_width, label='Geothermal Energy', color='gray', edgecolor='black')  # New data series added

ax.set_title('Adoption of Renewable Energy Sources\nin Futuristan (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)
ax.set_xticks(years)
ax.set_xticklabels(years)
ax.legend(loc='upper left', fontsize=12)
ax.text(2010.5, 125, 'Note: Significant growth post-2015', fontsize=12, style='italic', 
        bbox={'facecolor': 'lightgray', 'alpha': 0.5, 'pad': 5})
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()