import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# New Biomass data (in arbitrary units) for Urban ecosystem over four quarters
urban_biomass = [50, 55, 60, 65, 47, 53, 58, 63, 45, 50, 55, 60, 40, 45, 50, 55]

# Updated dataset for Box Plot
biomass_data = [
    [250, 270, 300, 320, 240, 260, 290, 310, 230, 250, 280, 300, 220, 230, 240, 260], # Forest
    [150, 155, 160, 165, 140, 145, 150, 155, 135, 140, 145, 150, 130, 135, 140, 145], # Wetland
    [180, 185, 190, 195, 175, 180, 185, 190, 170, 175, 180, 185, 165, 170, 175, 180], # Grassland
    [70, 72, 75, 78, 65, 68, 70, 73, 60, 63, 65, 68, 55, 58, 60, 63], # Desert
    [200, 205, 210, 215, 195, 200, 205, 210, 190, 195, 200, 205, 185, 190, 195, 200], # Marine
    urban_biomass
]

# Updated labels for each ecosystem
ecosystems = ["Forest", "Wetland", "Grassland", "Desert", "Marine", "Urban"]

# Create Figure and Axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot
boxplots = ax.boxplot(biomass_data, patch_artist=True,
                    boxprops=dict(facecolor='lightblue', color='darkblue'),
                    whiskerprops=dict(color='darkblue'),
                    capprops=dict(color='darkblue'),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(marker='o', color='red', alpha=0.5))

# Colors
colors = ['lightgreen', 'lightcoral', 'lightskyblue', 'lightgoldenrodyellow', 'lightpink', 'lightgray']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Labels
ax.set_xticklabels(ecosystems)
ax.set_title('Ecosystem Health Analysis \n Biomass Variation Across Different Ecosystems Over a Year', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Ecosystems', fontsize=14)
ax.set_ylabel('Biomass (Arbitrary Units)', fontsize=14)

# Grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legend
legend_elements = [Patch(facecolor=color, label=ecosystem) for color, ecosystem in zip(colors, ecosystems)]
ax.legend(handles=legend_elements, title='Ecosystems', loc='upper right', fontsize=10)

# Annotations
annotations = [
    ('Highest in Q4', 3, 320, 'forest'), # Index of 3 corresponds to Q4 for Forest
    ('Highest in Q4', 3, 165, 'wetland'),
    ('Highest in Q4', 3, 195, 'grassland'),
    ('Highest in Q4', 3, 78, 'desert'),
    ('Highest in Q4', 3, 215, 'marine'),
    ('Highest in Q4', 3, 65, 'urban')
]

for text, x, y, ecosystem in annotations:
    ecosystem_idx = ecosystems.index(ecosystem.capitalize())
    ax.annotate(text, xy=(ecosystem_idx + 1, y), xytext=(ecosystem_idx + 1.5, y + 20),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
                fontsize=10, color='black')

plt.tight_layout()
plt.show()