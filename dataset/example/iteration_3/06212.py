import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing Ecosystem Health Through Biomass Variation
# This study aims to understand the health of different ecosystems (Forest, Wetland, Grassland, Desert, Marine)
# by examining the variations in biomass distributions across these ecosystems over a year.

# Biomass data (in arbitrary units) for each ecosystem over four quarters
forest_biomass = [250, 270, 300, 320, 240, 260, 290, 310, 230, 250, 280, 300, 220, 230, 240, 260]
wetland_biomass = [150, 155, 160, 165, 140, 145, 150, 155, 135, 140, 145, 150, 130, 135, 140, 145]
grassland_biomass = [180, 185, 190, 195, 175, 180, 185, 190, 170, 175, 180, 185, 165, 170, 175, 180]
desert_biomass = [70, 72, 75, 78, 65, 68, 70, 73, 60, 63, 65, 68, 55, 58, 60, 63]
marine_biomass = [200, 205, 210, 215, 195, 200, 205, 210, 190, 195, 200, 205, 185, 190, 195, 200]

# Aggregating data for Box Plot
biomass_data = [
    forest_biomass,
    wetland_biomass,
    grassland_biomass,
    desert_biomass,
    marine_biomass
]

# Labels for each ecosystem
ecosystems = ["Forest", "Wetland", "Grassland", "Desert", "Marine"]

# Create subplots
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Plotting the boxplots
boxplots = ax.boxplot(biomass_data, patch_artist=True,
                    boxprops=dict(facecolor='lightblue', color='darkblue'),
                    whiskerprops=dict(color='darkblue'),
                    capprops=dict(color='darkblue'),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(marker='o', color='red', alpha=0.5))

# Customizing colors for each box
colors = ['lightgreen', 'lightcoral', 'lightskyblue', 'lightgoldenrodyellow', 'lightpink']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Adding ecosystem labels
ax.set_xticklabels(ecosystems)

# Titles and labels
ax.set_title('Ecosystem Health Analysis \n Biomass Variation Across Different Ecosystems Over a Year', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Ecosystems', fontsize=14)
ax.set_ylabel('Biomass (Arbitrary Units)', fontsize=14)

# Customizing grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend manually
legend_elements = [Patch(facecolor=color, label=ecosystem) for color, ecosystem in zip(colors, ecosystems)]
ax.legend(handles=legend_elements, title='Ecosystems', loc='upper right', fontsize=10)

# Adding annotations for each ecosystem with the maximum variation's quarter
annotations = [
    ('Highest in Q4', forest_biomass.index(320), 320, 'forest'),
    ('Highest in Q4', wetland_biomass.index(165), 165, 'wetland'),
    ('Highest in Q4', grassland_biomass.index(195), 195, 'grassland'),
    ('Highest in Q4', desert_biomass.index(78), 78, 'desert'),
    ('Highest in Q4', marine_biomass.index(215), 215, 'marine'),
]

# Applying the annotations
for text, x, y, ecosystem in annotations:
    ecosystem_idx = ecosystems.index(ecosystem.capitalize())
    ax.annotate(text, xy=(ecosystem_idx + 1, y), xytext=(ecosystem_idx + 1.5, y + 20),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
                fontsize=10, color='black')

# Automatically adjust for better appearance
plt.tight_layout()

# Display the plot
plt.show()