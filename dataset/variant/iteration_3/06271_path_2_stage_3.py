import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

solar_energy = [10, 15, 20, 28, 40, 55, 72, 90, 112, 140, 175, 215, 260, 310, 365, 430, 500, 580, 670, 770, 880]
wind_energy = [30, 40, 50, 65, 85, 110, 140, 175, 215, 260, 310, 370, 430, 500, 580, 670, 770, 880, 1000, 1140, 1300]
hydro_energy = [220, 230, 240, 250, 260, 270, 280, 290, 295, 300, 305, 310, 315, 320, 323, 325, 328, 330, 335, 340, 345]

data = np.array([solar_energy, wind_energy, hydro_energy])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Sunny', 'Breezy', 'Wet'],
             colors=['#fdae61', '#abd9e9', '#2c7bb6'], alpha=0.8)

ax.set_title('Eco-Power Surge (2010-2030)', fontsize=18, fontweight='bold')
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Output (GWh)', fontsize=14)

ax.legend(title='Power Sources', loc='upper right', fontsize=10)

ax.set_xticks(np.arange(2010, 2031, 2))
ax.set_yticks(np.arange(0, 1401, 200))
ax.set_xlim(2010, 2030)
ax.set_ylim(0, 1400)

ax.grid(True, linestyle='-.', alpha=0.5)

total_production = np.sum(data, axis=0)
ax2 = ax.twinx()
ax2.plot(years, total_production, marker='s', linestyle='-.', linewidth=2, color='#4daf4a', label='Overall Output')
ax2.set_ylabel('Total Output (GWh)', fontsize=12, color='#4daf4a')
ax2.tick_params(axis='y', colors='#4daf4a')

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, loc='upper right', title='Power Data')

plt.tight_layout()
plt.show()