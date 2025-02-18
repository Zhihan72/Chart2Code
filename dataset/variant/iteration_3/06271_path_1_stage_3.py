import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

# Shuffling the energy data manually to introduce randomness
solar_energy = [40, 72, 15, 430, 28, 365, 90, 112, 10, 140, 770, 175, 580, 310, 500, 20, 670, 260, 215, 880, 55]
wind_energy = [430, 215, 50, 880, 260, 40, 500, 370, 770, 110, 1000, 1140, 85, 670, 1300, 580, 310, 65, 140, 500, 30]
hydro_energy = [310, 345, 270, 350, 240, 305, 320, 325, 240, 230, 335, 280, 295, 270, 250, 335, 315, 330, 305, 223, 300]
geothermal_energy = [60, 15, 29, 210, 24, 340, 17, 240, 35, 305, 140, 86, 50, 270, 162, 20, 102, 42, 120, 72, 185]

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