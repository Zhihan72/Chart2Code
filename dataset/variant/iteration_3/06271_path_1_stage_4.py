import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

solar_energy = [40, 72, 15, 430, 28, 365, 90, 112, 10, 140, 770, 175, 580, 310, 500, 20, 670, 260, 215, 880, 55]
wind_energy = [430, 215, 50, 880, 260, 40, 500, 370, 770, 110, 1000, 1140, 85, 670, 1300, 580, 310, 65, 140, 500, 30]
hydro_energy = [310, 345, 270, 350, 240, 305, 320, 325, 240, 230, 335, 280, 295, 270, 250, 335, 315, 330, 305, 223, 300]
geothermal_energy = [60, 15, 29, 210, 24, 340, 17, 240, 35, 305, 140, 86, 50, 270, 162, 20, 102, 42, 120, 72, 185]

data = np.array([solar_energy, wind_energy, hydro_energy, geothermal_energy])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Wind', 'Hydro', 'Geothermal', 'Solar'],  # Manually shuffled
             colors=['#8da0cb']*4, alpha=0.7)

ax.set_title('Renewable Energy Surge (2010-2030)', fontsize=18, fontweight='bold', color='orange')  # Randomly altered
ax.set_xlabel('Chronological Year', fontsize=13, color='teal')  # Randomly altered
ax.set_ylabel('Production Volume (GWh)', fontsize=13, color='teal')  # Randomly altered

ax.legend(title='Renewable Types', loc='lower right', fontsize=11, facecolor='lightsteelblue')  # Randomly altered

ax.set_xticks(np.arange(2010, 2031, 2))
ax.set_yticks(np.arange(0, 1401, 200))
ax.set_xlim(2010, 2030)
ax.set_ylim(0, 1400)

ax.grid(True, linestyle='-.', alpha=0.5, linewidth=0.8, color='grey')

total_production = np.sum(data, axis=0)
ax2 = ax.twinx()
ax2.plot(years, total_production, marker='^', linestyle='-', color='darkred', label='Cumulative Renewable Output')  # Randomly altered
ax2.set_ylabel('Aggregate Output (GWh)', fontsize=12, color='darkred')  # Randomly altered
ax2.tick_params(axis='y', colors='darkred')

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, loc='upper right', title='Energy Overview', facecolor='lightsteelblue')  # Randomly altered

plt.tight_layout()
plt.show()