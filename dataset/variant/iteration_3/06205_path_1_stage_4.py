import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'West']
years = ['2019', '2020', '2021', '2022']

north_generation = np.array([25, 30, 25, 35])
south_generation = np.array([20, 25, 30, 30])
west_generation = np.array([15, 20, 35, 40])

# Normalize data with respect to an average for diverging effect
baseline = (north_generation + south_generation + west_generation) / 3

north_diverging = north_generation - baseline
south_diverging = south_generation - baseline
west_diverging = west_generation - baseline

colors = ['#8c564b', '#e377c2', '#7f7f7f']
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(years))

# Plot diverging bar chart
ax.bar(x, north_diverging, color=colors[0], label='North')
ax.bar(x, south_diverging, bottom=north_diverging, color=colors[1], label='South')
ax.bar(x, west_diverging, bottom=north_diverging + south_diverging, color=colors[2], label='West')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Deviation from Average Generation (GWh)', fontsize=12)
ax.set_title('Diverging Solar Power Generation by Region Relative to Average', fontsize=16, fontweight='bold', style='italic')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(title='Regions', loc='upper left', frameon=False)
ax.yaxis.grid(True, linestyle=':', linewidth=1.5, alpha=0.5)

plt.show()