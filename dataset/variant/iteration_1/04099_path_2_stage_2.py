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

# Changed the color order manually
ax.stackplot(years, energy_data, labels=['Fossil Fuels', 'Solar Power', 'Wind Power', 'Hydro Power', 'Nuclear Power'], 
             colors=['#1f78b4', '#6a3d9a', '#d73027', '#33a02c', '#ffd700'], alpha=0.8)

ax.set_title('Energy Transition in NeoCity\n(2025-2050)', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, weight='bold')
ax.set_ylabel('Energy Production (TWh)', fontsize=14, weight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Energy Sources', fontsize=12)
plt.tight_layout()

ax.annotate('Solar Dominates', xy=(2041, 90), xytext=(2030, 120),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, weight='bold')
ax.annotate('Fossil Fuels Phase Out', xy=(2040, 3), xytext=(2028, 30),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, weight='bold')

plt.show()