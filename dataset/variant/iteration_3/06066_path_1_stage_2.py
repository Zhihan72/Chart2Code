import matplotlib.pyplot as plt
import numpy as np

boreal_temperatures = [7, 10, 12, 15, 17, 20, 22, 20, 18, 14, 10, 8]
temperate_temperatures = [12, 15, 18, 21, 24, 27, 29, 28, 26, 22, 18, 14]
tropical_temperatures = [22, 23, 24, 25, 26, 27, 28, 28, 27, 26, 24, 23]
data = [boreal_temperatures, temperate_temperatures, tropical_temperatures]

forest_zones = ['Boreal', 'Temperate', 'Tropical']
fig, ax = plt.subplots(figsize=(14, 8))

vparts = ax.violinplot(data, showmeans=False, showmedians=False, showextrema=False, vert=False)

consistent_color = '#556B2F'

for pc in vparts['bodies']:
    pc.set_facecolor(consistent_color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

for i, temp_data in enumerate(data):
    y = np.random.normal(i + 1, 0.04, size=len(temp_data))
    ax.scatter(temp_data, y, alpha=0.7, color='black', zorder=5)

for i, forest_data in enumerate(data):
    median_val = np.median(forest_data)
    ax.text(median_val + 0.5, i + 1, f'{median_val:.1f}', verticalalignment='center', fontsize=12, color='darkred', weight='bold')

ax.set_title('Seasonal Variations in Daily Average Temperatures\nAcross Different Forest Zones', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Average Daily Temperature (°C)', fontsize=12)
ax.set_yticks(range(1, len(forest_zones) + 1))
ax.set_yticklabels(forest_zones)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.tight_layout()

plt.show()