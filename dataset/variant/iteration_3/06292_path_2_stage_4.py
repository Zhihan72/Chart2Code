import matplotlib.pyplot as plt
import numpy as np

# Data for ocean temperatures
pacific_temps = [22, 24, 23, 23, 25, 26, 27, 24, 26, 28, 29, 30, 27, 25, 24, 28, 26, 23, 22, 29]
atlantic_temps = [20, 21, 22, 23, 22, 24, 25, 26, 23, 22, 21, 20, 22, 23, 24, 26, 27, 25, 23, 22]
indian_temps = [25, 27, 28, 29, 27, 26, 25, 24, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 26, 27]

temperature_data = [pacific_temps, atlantic_temps, indian_temps]
ocean_names = ['Pacific Waters', 'Atlantic Depths', 'Tropical Ocean']

fig, ax = plt.subplots(figsize=(14, 8))

box = ax.boxplot(temperature_data, vert=False, patch_artist=True, notch=False,
                 boxprops=dict(facecolor='pink', color='darkred'),
                 whiskerprops=dict(color='darkgreen', linestyle='-'),
                 capprops=dict(color='darkgreen'),
                 medianprops=dict(color='blue', linewidth=1.5),
                 flierprops=dict(marker='^', color='purple', alpha=0.6),
                 meanline=False, showmeans=True, meanprops=dict(marker='s', markerfacecolor='orange', markeredgecolor='orange', markersize=8))

colors = ['#FFC0CB', '#98FB98', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_xlabel('Heat Levels (°C)', fontsize=12)
ax.set_yticks([1, 2, 3])
ax.set_yticklabels(ocean_names)
ax.set_title('Oceanic Temperature Variations', fontsize=16, fontweight='bold', pad=20)

ax.legend([box["means"][0]], ['Average Measure'], loc='lower left', fontsize=10)

ax.grid(axis='y', linestyle=':', alpha=0.9)

plt.tight_layout()
plt.show()