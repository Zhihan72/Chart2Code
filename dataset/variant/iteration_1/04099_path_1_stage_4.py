import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)
fossil_fuels = np.array([85, 83, 80, 76, 71, 65, 58, 50, 41, 32, 23, 15, 8, 4, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
solar_power = np.array([2, 4, 7, 11, 16, 22, 30, 40, 50, 60, 70, 78, 85, 90, 93, 94, 95, 95, 96, 97, 98, 98, 98, 98, 98, 98])
wind_power = np.array([5, 6, 8, 9, 10, 12, 15, 20, 25, 30, 35, 38, 40, 42, 45, 48, 50, 52, 53, 54, 54, 55, 55, 55, 55, 55])
hydro_power = np.array([3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22])

energy_data = np.vstack([fossil_fuels, solar_power, wind_power, hydro_power])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, energy_data, colors=['#d73027'], alpha=0.8)

ax.set_title('Energy Shift (2025-2050)', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=14, weight='bold')
ax.set_ylabel('Prod (TWh)', fontsize=14, weight='bold')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

plt.tight_layout()

ax.annotate('Solar Leads', xy=(2041, 90), xytext=(2030, 120),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, weight='bold')
ax.annotate('Fossils End', xy=(2040, 3), xytext=(2028, 30),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, weight='bold')

plt.show()