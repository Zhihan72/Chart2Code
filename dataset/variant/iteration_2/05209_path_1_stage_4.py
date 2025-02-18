import matplotlib.pyplot as plt
import numpy as np

# Altered labels and titles
sectors = ['Waste Mgmt', 'Residential', 'Agriculture', 'Transport', 'Energy', 'Industrial']
years = ['2019', '2017', '2020', '2018', '2021']
emission_levels = np.array([
    [44, 50, 40, 47, 35],       # Waste Mgmt
    [110, 120, 108, 115, 90],   # Residential
    [70, 80, 65, 75, 55],       # Agriculture
    [130, 140, 125, 135, 100],  # Transport
    [55, 60, 53, 58, 50],       # Energy
    [190, 200, 180, 195, 170]   # Industrial
])

colors = ['#d62728', '#2ca02c', '#1f77b4', '#9467bd', '#ff7f0e', '#8c564b']

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.13
indices = np.arange(len(years))

for i, sector in enumerate(sectors):
    bar_positions = indices + i * bar_height
    ax.barh(bar_positions, emission_levels[i], bar_height, color=colors[i], label=sector)

ax.set_ylabel('Timeline', fontsize=14)
ax.set_xlabel('Emission of CO2 (TMT)', fontsize=14)
ax.set_title('Emission Trends in Greenlandia (2019-2017)', fontsize=16, fontweight='bold')
ax.set_yticks(indices + bar_height * len(sectors) / 2)
ax.set_yticklabels(years)

ax.legend(title='Category', loc='upper right', bbox_to_anchor=(1.12, 1), fontsize='large')

ax.xaxis.grid(True, linestyle='--', which='major', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()