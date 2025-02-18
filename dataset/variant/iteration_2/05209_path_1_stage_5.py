import matplotlib.pyplot as plt
import numpy as np

sectors = ['Waste Mgmt', 'Residential', 'Agriculture', 'Transport', 'Energy', 'Industrial']
years = ['2019', '2017', '2020', '2018', '2021']
emission_levels = np.array([
    [44, 50, 40, 47, 35],
    [110, 120, 108, 115, 90],
    [70, 80, 65, 75, 55],
    [130, 140, 125, 135, 100],
    [55, 60, 53, 58, 50],
    [190, 200, 180, 195, 170]
])

colors = ['#d62728', '#2ca02c', '#1f77b4', '#9467bd', '#ff7f0e', '#8c564b']
markers = ['^', 'o', 's', 'd', 'v', 'x']
line_styles = ['-', '--', '-.', ':', '-', '--']

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.13
indices = np.arange(len(years))

for i, sector in enumerate(sectors):
    bar_positions = indices + i * bar_height
    ax.barh(bar_positions, emission_levels[i], bar_height, color=colors[i], label=sector, edgecolor='black', linestyle=line_styles[i])

ax.set_ylabel('Timeline', fontsize=14)
ax.set_xlabel('Emission of CO2 (TMT)', fontsize=14)
ax.set_title('Emission Trends in Greenlandia (2019-2017)', fontsize=16, fontweight='bold')
ax.set_yticks(indices + bar_height * len(sectors) / 2)
ax.set_yticklabels(years)

ax.legend(title='Category', loc='center left', bbox_to_anchor=(1, 0.5), fontsize='medium', shadow=True, markerscale=1.5)
ax.xaxis.grid(True, linestyle=':', linewidth=1, alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()