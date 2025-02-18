import matplotlib.pyplot as plt
import numpy as np

temperate_temperatures = [12, 15, 18, 21, 24, 27, 29, 28, 26, 22, 18, 14]
tropical_temperatures = [22, 23, 24, 25, 26, 27, 28, 28, 27, 26, 24, 23]
data = [temperate_temperatures, tropical_temperatures]

fig, ax = plt.subplots(figsize=(14, 8))

vparts = ax.violinplot(data, vert=False, showmeans=False, showmedians=False, showextrema=False, widths=0.7)

# Manually assigned colors
colors = ['#FFD700', '#8B4513']

for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('none')
    pc.set_alpha(0.7)

box = ax.boxplot(data, patch_artist=True, notch=True, vert=False, widths=0.2, showfliers=False)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Remove the setting for medians, whiskers, and caps

for i, temp_data in enumerate(data):
    y = np.random.normal(i + 1, 0.04, size=len(temp_data))
    ax.scatter(temp_data, y, alpha=0.7, color='black', zorder=5)

# Remove the grids
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()