import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)
fossil_fuels = np.array([85, 82, 80, 75, 72, 66, 59, 48, 43, 33, 22, 14, 6, 5, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
solar_power = np.array([2, 3, 8, 10, 14, 21, 29, 39, 48, 59, 68, 75, 83, 92, 95, 94, 95, 96, 97, 97, 99, 98, 98, 98, 98, 98])
wind_power = np.array([5, 7, 9, 9, 11, 13, 16, 19, 27, 29, 34, 39, 41, 41, 44, 49, 51, 52, 52, 55, 54, 55, 55, 55, 55, 55])
hydro_power = np.array([4, 4, 4, 6, 8, 9, 10, 12, 15, 15, 18, 19, 20, 22, 21, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22])
nuclear_power = np.array([4, 7, 9, 13, 12, 16, 18, 21, 22, 24, 31, 31, 30, 33, 34, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33])

energy_data = np.vstack([fossil_fuels, solar_power, wind_power, hydro_power, nuclear_power])

fig, ax = plt.subplots(figsize=(14, 8))

# Changed line styles and marker symbols
line_styles = ['-', '--', '-.', ':', '-']
markers = ['o', 'v', 's', 'p', '*']
for i, data in enumerate(energy_data):
    ax.plot(years, data, line_styles[i], marker=markers[i], label=['Fossil Fuels', 'Solar Power', 'Wind Power', 'Hydro Power', 'Nuclear Power'][i])

# Added grid and changed legend placement
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(loc='upper left', fontsize='small', frameon=False)

# Modified border visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
plt.tight_layout()

plt.show()