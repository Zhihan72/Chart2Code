import matplotlib.pyplot as plt
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

ecosystems = ["Jungle", "Savanna", "Arid Land", "Ocean"]

fig, ax = plt.subplots(1, 1, figsize=(12, 8))

box_color = 'lightblue'
line_color = 'darkblue'

boxplots = ax.boxplot(biomass_data, patch_artist=True, vert=False,
                    boxprops=dict(facecolor=box_color, color=line_color),
                    whiskerprops=dict(color=line_color, linestyle='-.', linewidth=1.5),
                    capprops=dict(color=line_color, linestyle='-'),
                    medianprops=dict(color='orange', linewidth=3),
                    flierprops=dict(marker='x', color=line_color, alpha=0.5, markersize=7))

ax.set_yticklabels(ecosystems)
ax.set_title('Ecosystem Biomass Levels in Different Climates', fontsize=18, fontweight='bold', pad=15)
ax.set_ylabel('Ecological Zones', fontsize=12, fontstyle='italic')
ax.set_xlabel('Biomass Index', fontsize=12, fontstyle='italic')
ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.6)

legend_elements = [Patch(facecolor=box_color, label='Biomass')]
ax.legend(handles=legend_elements, title='Biomes', loc='lower right', fontsize=11)

annotations = [
    ('Max in late Year', 320, 1, 'Jungle'),
    ('Max in late Year', 195, 2, 'Savanna'),
    ('Max in late Year', 78, 3, 'Arid Land'),
    ('Max in late Year', 215, 4, 'Ocean'),
]

for text, x, y, ecosystem in annotations:
    ax.annotate(text, xy=(x, y), xytext=(x + 20, y + 0.2),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='gray'),
                fontsize=9, color='blue')

plt.tight_layout()
plt.show()