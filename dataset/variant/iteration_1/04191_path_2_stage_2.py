import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)

solar_energy = np.array([50, 65, 80, 95, 112, 130, 150, 175, 200, 230, 260, 295, 330, 370, 410, 455, 500, 550, 600, 655, 710, 770, 830, 895, 960, 1030])
wind_energy = np.array([35, 42, 50, 60, 72, 85, 99, 115, 132, 152, 174, 198, 225, 254, 285, 318, 353, 390, 430, 472, 517, 565, 616, 670, 727, 787])
hydro_energy = np.array([20, 23, 28, 34, 42, 51, 61, 74, 88, 105, 123, 143, 165, 189, 215, 243, 273, 305, 339, 375, 413, 453, 495, 540, 587, 637])

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