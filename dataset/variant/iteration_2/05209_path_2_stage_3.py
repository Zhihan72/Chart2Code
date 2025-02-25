import matplotlib.pyplot as plt
import numpy as np

sectors = ['Transp', 'Indust', 'Resi', 'Agri', 'Waste']
years = ['17', '18', '19', '20', '21']

emission_levels = np.array([
    [135, 125, 140, 100, 130],
    [180, 170, 200, 190, 195],
    [108, 110, 120, 115,  90],
    [65,   80,  70,  55,   75],
    [44,   35,  47,  50,  40]
])

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
indices = np.arange(len(sectors))

for i, year in enumerate(years):
    bar_positions = indices + i * bar_height
    ax.barh(bar_positions, emission_levels[:, i], bar_height, label=year)

ax.set_ylabel('Sectors', fontsize=14)
ax.set_xlabel('CO2 Emission (kMT)', fontsize=14)
ax.set_title('CO2 Levels in Greentopia (2017-2021)', fontsize=16, fontweight='bold')
ax.set_yticks(indices + bar_height * len(years) / 2)
ax.set_yticklabels(sectors)

ax.legend(title='Yr', loc='upper right', bbox_to_anchor=(1.12, 1), fontsize='large')
ax.xaxis.grid(True, linestyle='--', which='major', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()