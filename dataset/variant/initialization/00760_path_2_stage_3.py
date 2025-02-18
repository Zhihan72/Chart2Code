import matplotlib.pyplot as plt
import numpy as np

regions = ['Sunland', 'Windy Valley', 'Waterfront', 'Earthcore']
sunland_energy = [320, 300, 310, 305, 315, 330, 335, 325, 340, 330, 325, 335]
windy_valley_energy = [250, 260, 245, 255, 265, 270, 275, 260, 255, 250, 265, 270]
waterfront_energy = [180, 190, 185, 175, 195, 200, 205, 195, 200, 190, 185, 195]
earthcore_energy = [140, 135, 145, 140, 150, 155, 160, 155, 150, 145, 140, 155]

energy_data = [sunland_energy, windy_valley_energy, waterfront_energy, earthcore_energy]

fig, ax = plt.subplots(figsize=(12, 8))

boxplots = ax.boxplot(energy_data, vert=True, patch_artist=True, showmeans=True, notch=True)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set(facecolor=color, alpha=0.6)

# Removed customizations for whiskers, caps, medians, and means that are principally stylistic

ax.set_ylabel('Output Volume (Gigawatts)', fontsize=12)
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(regions, fontsize=12)

plt.show()