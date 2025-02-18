import matplotlib.pyplot as plt
import numpy as np

temperate_temperatures = [12, 15, 18, 21, 24, 27, 29, 28, 26, 22, 18, 14]
tropical_temperatures = [22, 23, 24, 25, 26, 27, 28, 28, 27, 26, 24, 23]
data = [temperate_temperatures, tropical_temperatures]

forest_zones = ['Temperate', 'Tropical']

fig, ax = plt.subplots(figsize=(14, 8))

vparts = ax.violinplot(data, vert=False, showmeans=False, showmedians=False, showextrema=False, widths=0.7)

colors = ['#8B4513', '#FFD700']

for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

box = ax.boxplot(data, patch_artist=True, notch=True, vert=False, widths=0.2, labels=forest_zones, showfliers=False)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.setp(box['medians'], color='red', linewidth=2)
plt.setp(box['whiskers'], color='blue', linewidth=1.5, linestyle='--')
plt.setp(box['caps'], color='black', linewidth=1.5)

for i, temp_data in enumerate(data):
    y = np.random.normal(i + 1, 0.04, size=len(temp_data))
    ax.scatter(temp_data, y, alpha=0.7, color='black', zorder=5)

for i, forest_data in enumerate(data):
    median_val = np.median(forest_data)
    ax.text(median_val + 0.5, i + 1, f'{median_val:.1f}', verticalalignment='center', fontsize=12, color='darkred', weight='bold')

ax.set_title('Seasonal Variations in Daily Average Temperatures\nAcross Different Forest Zones', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Average Daily Temperature (°C)', fontsize=12)
ax.set_ylabel('Forest Zones', fontsize=12)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(rotation=0, fontsize=11)

handles = [plt.Line2D([0], [0], color=color, lw=4, label=zone) for color, zone in zip(colors, forest_zones)]
ax.legend(handles=handles, title='Forest Zones', loc='upper left')

plt.tight_layout()
plt.show()