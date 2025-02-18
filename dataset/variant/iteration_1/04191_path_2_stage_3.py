import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)

solar_energy = np.array([95, 65, 130, 150, 50, 112, 175, 80, 410, 370, 330, 200, 230, 500, 260, 295, 710, 455, 600, 655, 710, 890, 770, 415, 960, 1030])
wind_energy = np.array([60, 42, 50, 35, 72, 85, 115, 99, 152, 132, 198, 430, 174, 198, 225, 472, 285, 318, 565, 765, 390, 413, 517, 616, 627, 787])
hydro_energy = np.array([34, 75, 23, 20, 42, 51, 105, 61, 88, 123, 143, 189, 165, 215, 243, 305, 273, 375, 453, 339, 495, 540, 587, 413, 637, 305])

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.plot(years, solar_energy, label='Solar', marker='o', linestyle='-', linewidth=2, color='orange')
ax1.plot(years, wind_energy, label='Wind', marker='s', linestyle='--', linewidth=2, color='mediumvioletred')
ax1.plot(years, hydro_energy, label='Hydro', marker='^', linestyle='-.', linewidth=2, color='deepskyblue')

ax1.set_title('Renewable Energy in SolarCity (2025-2050)', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Prod. (GWh)', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.7)

ax1.set_xlim(2024, 2051)
ax1.set_ylim(0, 1100)

ax1.legend(title='Sources', title_fontsize=12, fontsize=10, loc='upper left')

total_energy = solar_energy + wind_energy + hydro_energy

ax2 = ax1.twinx()
ax2.plot(years, total_energy, label='Total', color='slateblue', linestyle=':', linewidth=2, marker='x')

ax2.set_ylabel('Total (GWh)', fontsize=14)
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()