import matplotlib.pyplot as plt
import numpy as np

# Data for the regions
regions = ['North', 'South', 'West']
years = ['2019', '2020', '2021', '2022']

north_generation = np.array([25, 30, 25, 35])
south_generation = np.array([20, 25, 30, 30])
west_generation = np.array([15, 20, 35, 40])

# Normalize the data
baseline = (north_generation + south_generation + west_generation) / 3

north_diverging = north_generation - baseline
south_diverging = south_generation - baseline
west_diverging = west_generation - baseline

colors = ['#8c564b', '#e377c2', '#7f7f7f']
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(years))

# Plotting
ax.bar(x, north_diverging, color=colors[0], label='Zone A')
ax.bar(x, south_diverging, bottom=north_diverging, color=colors[1], label='Zone B')
ax.bar(x, west_diverging, bottom=north_diverging + south_diverging, color=colors[2], label='Zone C')

ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Offset from Typical Output (GWh)', fontsize=12)
ax.set_title('Comparative Solar Energy Outcome Across Zones', fontsize=16, fontweight='bold', style='italic')
ax.set_xticks(x)
ax.set_xticklabels(['19', '20', '21', '22']) # Shortened year labels
ax.legend(title='Zones', loc='upper left', frameon=False)
ax.yaxis.grid(True, linestyle=':', linewidth=1.5, alpha=0.5)

plt.show()