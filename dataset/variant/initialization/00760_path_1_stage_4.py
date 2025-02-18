import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import seaborn as sns
from matplotlib.patches import Patch

sns.set_theme(style="darkgrid")

regions = ['Sol', 'Vent', 'Aqua', 'Geo', 'Bio', 'Hydro']
sol_energy = [320, 300, 310, 305, 315, 330, 335, 325, 340, 330, 325, 335]
vent_energy = [250, 260, 245, 255, 265, 270, 275, 260, 255, 250, 265, 270]
aqua_energy = [180, 190, 185, 175, 195, 200, 205, 195, 200, 190, 185, 195]
geo_energy = [140, 135, 145, 140, 150, 155, 160, 155, 150, 145, 140, 155]
bio_energy = [280, 275, 285, 290, 295, 305, 310, 300, 305, 310, 300, 295]
hydro_energy = [160, 155, 165, 160, 170, 175, 180, 175, 170, 165, 160, 175]

energy_data = [sol_energy, vent_energy, aqua_energy, geo_energy, bio_energy, hydro_energy]

fig, ax = plt.subplots(figsize=(12, 8))

boxplots = ax.boxplot(energy_data, vert=True, patch_artist=True, showmeans=True, widths=0.5)

new_colors = ['#4682B4', '#FF6347', '#DAA520', '#B8860B', '#8B4513', '#FF4500']
for patch, color in zip(boxplots['boxes'], new_colors):
    patch.set(facecolor=color, alpha=0.6)

for whisker in boxplots['whiskers']:
    whisker.set(color='cyan', linewidth=1.5, linestyle='-')
for cap in boxplots['caps']:
    cap.set(color='cyan', linewidth=1.5)
for median in boxplots['medians']:
    median.set(color='purple', linewidth=2)
for mean in boxplots['means']:
    mean.set(marker='x', color='red', markersize=8)

ax.set_title('Monthly Energy Production in 2023', fontsize=14, pad=10)
ax.set_ylabel('Energy (GWh)', fontsize=11)
ax.set_xticks(range(1, len(regions) + 1))
ax.set_xticklabels(regions, fontsize=11, rotation=45)

ax.yaxis.set_minor_locator(ticker.MultipleLocator(15))

ax.yaxis.grid(True, linestyle='-', alpha=0.5)
ax.xaxis.grid(True, linestyle='--', alpha=0.5)

legend_elements = [Patch(facecolor=color, edgecolor='black', label=region) for color, region in zip(new_colors, regions)]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1, 0.9), fontsize=9, title="Regions")

plt.tight_layout()
plt.show()