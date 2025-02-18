import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

solar_energy = [10, 15, 20, 28, 40, 55, 72, 90, 112, 140, 175, 215, 260, 310, 365, 430, 500, 580, 670, 770, 880]
wind_energy = [30, 40, 50, 65, 85, 110, 140, 175, 215, 260, 310, 370, 430, 500, 580, 670, 770, 880, 1000, 1140, 1300]
hydro_energy = [220, 230, 240, 250, 260, 270, 280, 290, 295, 300, 305, 310, 315, 320, 323, 325, 328, 330, 335, 340, 345]
geothermal_energy = [15, 17, 20, 24, 29, 35, 42, 50, 60, 72, 86, 102, 120, 140, 162, 185, 210, 240, 270, 305, 340]

data = np.array([solar_energy, wind_energy, hydro_energy, geothermal_energy])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Geothermal'],
             colors=['#8da0cb']*4, alpha=0.7)

ax.set_title('Growth of Renewable Energy Production (2010-2030)', fontsize=18, fontweight='bold', color='darkgreen')
ax.set_xlabel('Year', fontsize=13, color='purple')
ax.set_ylabel('Energy Production (GWh)', fontsize=13, color='purple')

ax.legend(title='Energy Source', loc='lower right', fontsize=11, facecolor='lightgray')

ax.set_xticks(np.arange(2010, 2031, 2))
ax.set_yticks(np.arange(0, 1401, 200))
ax.set_xlim(2010, 2030)
ax.set_ylim(0, 1400)

ax.grid(True, linestyle='-.', alpha=0.5, linewidth=0.8, color='grey')

total_production = np.sum(data, axis=0)
ax2 = ax.twinx()
ax2.plot(years, total_production, marker='^', linestyle='-', color='navy', label='Total Renewable Production')
ax2.set_ylabel('Total Production (GWh)', fontsize=12, color='navy')
ax2.tick_params(axis='y', colors='navy')

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, loc='upper right', title='Energy Metrics', facecolor='lightgray')

plt.tight_layout()
plt.show()