import matplotlib.pyplot as plt
import numpy as np

tree_species = ['Elm', 'Ash', 'Cedar', 'Fir', 'Sycamore', 'Aspen', 'Spruce']
sunlight_hours = np.array([4, 6, 5, 8, 2, 9, 3])
moisture_levels = np.array([800, 600, 700, 500, 1200, 400, 1300])
prevalence = np.array([200, 250, 180, 300, 220, 270, 320])

plt.figure(figsize=(12, 8))

# Altered stylistic elements for randomness
scatter = plt.scatter(sunlight_hours, moisture_levels, s=prevalence, c=prevalence, cmap='plasma', edgecolor='green', alpha=0.7, marker='<')

plt.title('Arboreal Categories in Wilderwood', fontsize=18, fontweight='heavy', color='navy')
plt.xlabel('Sunlight Duration (Hrs/Day)', fontsize=14, fontweight='bold', color='darkred')
plt.ylabel('Water Absorbance (mm/Year)', fontsize=14, fontweight='bold', color='darkgreen')

color_bar = plt.colorbar(scatter)
color_bar.set_label('Presence Metric', rotation=270, labelpad=15, fontsize=11, color='purple')

for i, species in enumerate(tree_species):
    plt.annotate(species, (sunlight_hours[i], moisture_levels[i]), 
                 textcoords="offset points", xytext=(-5,10), ha='right', fontsize=10, color='dodgerblue', fontstyle='italic')

plt.grid(True, linestyle='-.', linewidth=0.75, color='lightgrey')
plt.tight_layout()
plt.show()