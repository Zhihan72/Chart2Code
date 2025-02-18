import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([5, 6, 8, 11, 15, 20, 26, 35, 47, 60, 75])
wind_energy = np.array([10, 12, 15, 20, 25, 33, 40, 52, 65, 80, 100])
hydropower_energy = np.array([30, 32, 35, 36, 37, 38, 39, 40, 41, 42, 44])
geothermal_energy = np.array([2, 3, 3, 4, 5, 6, 7, 9, 12, 15, 18])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
bar_offset = np.array([-1.5, -0.5, 0.5, 1.5]) * bar_width

# Updated colors, edge colors, and line styles
ax.bar(years + bar_offset[0], solar_energy, width=bar_width, label='Solar', color='cornflowerblue', edgecolor='navy', linestyle='-')
ax.bar(years + bar_offset[1], wind_energy, width=bar_width, label='Wind', color='mediumseagreen', edgecolor='darkgreen', linestyle=':')
ax.bar(years + bar_offset[2], hydropower_energy, width=bar_width, label='Hydro', color='goldenrod', edgecolor='saddlebrown', linestyle='--')
ax.bar(years + bar_offset[3], geothermal_energy, width=bar_width, label='Geo', color='dimgray', edgecolor='black', linestyle='-.')

# Updated title and label fontsizes
ax.set_title('Renewable Energy in Futuristan (2010-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Production (TWh)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years)

# Altered legend position and style
ax.legend(loc='upper right', fontsize=10, frameon=False)

# Removed grid lines
# ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Updated annotation
ax.text(2010.5, 120, 'Growth post-2015', fontsize=10, style='italic',
        bbox={'facecolor': 'whitesmoke', 'alpha': 0.3, 'pad': 5})

plt.tight_layout()
plt.show()