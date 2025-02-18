import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

forest_biomass = [250, 270, 300, 320, 240, 260, 290, 310, 230, 250, 280, 300, 220, 230, 240, 260]
grassland_biomass = [180, 185, 190, 195, 175, 180, 185, 190, 170, 175, 180, 185, 165, 170, 175, 180]
desert_biomass = [70, 72, 75, 78, 65, 68, 70, 73, 60, 63, 65, 68, 55, 58, 60, 63]
marine_biomass = [200, 205, 210, 215, 195, 200, 205, 210, 190, 195, 200, 205, 185, 190, 195, 200]

biomass_data = [
    forest_biomass,
    grassland_biomass,
    desert_biomass,
    marine_biomass
]

ecosystems = ["Forest", "Grassland", "Desert", "Marine"]

fig, ax = plt.subplots(1, 1, figsize=(12, 8))

boxplots = ax.boxplot(biomass_data, patch_artist=True,
                    boxprops=dict(facecolor='lightgreen', color='purple'),
                    whiskerprops=dict(color='purple', linestyle='-.', linewidth=1.5),
                    capprops=dict(color='purple', linestyle='-'),
                    medianprops=dict(color='orange', linewidth=3),
                    flierprops=dict(marker='x', color='green', alpha=0.5, markersize=7))

colors = ['lightcoral', 'palegreen', 'lightsalmon', 'lightsteelblue']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

ax.set_xticklabels(ecosystems)

ax.set_title('Biomass Variation Across Ecosystems \n Over a Year', fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel('Ecosystems', fontsize=12, fontstyle='italic')
ax.set_ylabel('Biomass (Arbitrary Units)', fontsize=12, fontstyle='italic')

ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.6)

legend_elements = [Patch(facecolor=color, label=ecosystem) for color, ecosystem in zip(colors, ecosystems)]
ax.legend(handles=legend_elements, title='Ecosystems', loc='lower right', fontsize=11)

annotations = [
    ('Peak in Q4', forest_biomass.index(320), 320, 'forest'),
    ('Peak in Q4', grassland_biomass.index(195), 195, 'grassland'),
    ('Peak in Q4', desert_biomass.index(78), 78, 'desert'),
    ('Peak in Q4', marine_biomass.index(215), 215, 'marine'),
]

for text, x, y, ecosystem in annotations:
    ecosystem_idx = ecosystems.index(ecosystem.capitalize())
    ax.annotate(text, xy=(ecosystem_idx + 1, y), xytext=(ecosystem_idx + 1.5, y + 10),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='gray'),
                fontsize=9, color='blue')

plt.tight_layout()
plt.show()