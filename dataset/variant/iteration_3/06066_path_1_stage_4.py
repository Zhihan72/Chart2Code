import matplotlib.pyplot as plt
import numpy as np

boreal_temps = [7, 10, 12, 15, 17, 20, 22, 20, 18, 14, 10, 8]
temperate_temps = [12, 15, 18, 21, 24, 27, 29, 28, 26, 22, 18, 14]
tropical_temps = [22, 23, 24, 25, 26, 27, 28, 28, 27, 26, 24, 23]
subtropical_temps = [18, 20, 22, 24, 26, 28, 30, 30, 28, 24, 22, 20]
data = [boreal_temps, temperate_temps, tropical_temps, subtropical_temps]

zones = ['Boreal', 'Temp.', 'Trop.', 'Subtrop.']
fig, ax = plt.subplots(figsize=(14, 8))

vparts = ax.violinplot(data, showmeans=False, showmedians=False, showextrema=False, vert=False)

color = '#556B2F'

for pc in vparts['bodies']:
    pc.set_facecolor(color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

for i, temp_data in enumerate(data):
    y = np.full(len(temp_data), i + 1) + 0.04 * np.random.randn(len(temp_data))
    ax.scatter(temp_data, y, alpha=0.7, color='black', zorder=5)

for i, forest_data in enumerate(data):
    median_val = np.median(forest_data)
    ax.text(median_val + 0.5, i + 1, f'{median_val:.1f}', verticalalignment='center', fontsize=12, color='darkred', weight='bold')

ax.set_title('Seasonal Temp. Variations\nby Forest Zone', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Avg Temp (°C)', fontsize=12)
ax.set_yticks(range(1, len(zones) + 1))
ax.set_yticklabels(zones)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.tight_layout()

plt.show()