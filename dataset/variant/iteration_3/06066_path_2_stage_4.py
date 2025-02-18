import matplotlib.pyplot as plt
import numpy as np

temperate_temperatures = [12, 15, 18, 21, 24, 27, 29, 28, 26, 22, 18, 14]
tropical_temperatures = [22, 23, 24, 25, 26, 27, 28, 28, 27, 26, 24, 23]
data = [temperate_temperatures, tropical_temperatures]

fig, ax = plt.subplots(figsize=(14, 8))

vparts = ax.violinplot(data, vert=False, showmeans=False, showmedians=False, showextrema=False, widths=0.7)

shuffled_colors = ['#FFD700', '#8B4513']

for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(shuffled_colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

box = ax.boxplot(data, patch_artist=True, notch=True, vert=False, widths=0.2, showfliers=False)

for patch, color in zip(box['boxes'], shuffled_colors):
    patch.set_facecolor(color)
plt.setp(box['medians'], color='red', linewidth=2)
plt.setp(box['whiskers'], color='blue', linewidth=1.5, linestyle='--')
plt.setp(box['caps'], color='black', linewidth=1.5)

for i, temp_data in enumerate(data):
    y = np.random.normal(i + 1, 0.04, size=len(temp_data))
    ax.scatter(temp_data, y, alpha=0.7, color='black', zorder=5)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()