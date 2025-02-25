import matplotlib.pyplot as plt
import numpy as np

sectors = ['Transport', 'Industrial', 'Residential', 'Agriculture', 'Waste Management']
years = ['2017', '2018', '2019', '2020', '2021']

emission_levels = np.array([
    [140, 135, 130, 125, 100],  # Transport
    [200, 195, 190, 180, 170],  # Industrial
    [120, 115, 110, 108,   90],  # Residential
    [80,   75,  70,  65,   55],  # Agriculture
    [50,   47,  44,  40,   35]   # Waste Management
])

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
indices = np.arange(len(sectors))

for i, year in enumerate(years):
    bar_positions = indices + i * bar_height
    ax.barh(bar_positions, emission_levels[:, i], bar_height, label=year)

ax.set_ylabel('Sector', fontsize=14)
ax.set_xlabel('Carbon Emission (Thousand Metric Tons)', fontsize=14)
ax.set_title('Carbon Emission Levels in Greentopia (2017-2021)', fontsize=16, fontweight='bold')
ax.set_yticks(indices + bar_height * len(years) / 2)
ax.set_yticklabels(sectors)

ax.legend(title='Year', loc='upper right', bbox_to_anchor=(1.12, 1), fontsize='large')
ax.xaxis.grid(True, linestyle='--', which='major', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()