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

# Applying a single color consistently across all data groups
single_color = 'skyblue'

for i, year in enumerate(years):
    bar_positions = indices + i * bar_height
    ax.barh(bar_positions, emission_levels[:, i], bar_height, label=f"20{year}", color=single_color, edgecolor='black', linestyle=':')

ax.legend(title='Year', loc='lower right', fontsize='small', title_fontsize='medium')

ax.set_xlabel('CO2 Emission (kMT)', fontsize=12)
ax.set_title('CO2 Levels in Greentopia', fontsize=18, fontweight='light')
ax.set_yticks(indices + bar_height * len(years) / 2)
ax.set_yticklabels(sectors, fontsize=10)

ax.xaxis.grid(True, linestyle='-.', which='minor', linewidth=0.4, alpha=0.5)

ax.spines['right'].set_linewidth(2)
ax.spines['right'].set_color('darkgrey')
ax.spines['top'].set_color('orange')
ax.spines['top'].set_linewidth(1)

plt.tight_layout()
plt.show()