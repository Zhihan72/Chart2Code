import matplotlib.pyplot as plt
import numpy as np

# New tree species names
tree_species = ['Elm', 'Ash', 'Cedar', 'Fir', 'Sycamore', 'Aspen', 'Spruce']
sunlight_hours = np.array([4, 6, 5, 8, 2, 9, 3])
moisture_levels = np.array([800, 600, 700, 500, 1200, 400, 1300])
prevalence = np.array([200, 250, 180, 300, 220, 270, 320])

plt.figure(figsize=(12, 8))
scatter = plt.scatter(sunlight_hours, moisture_levels, s=prevalence, c=prevalence, cmap='viridis', edgecolor='black', alpha=0.8)

# Changed titles and labels
plt.title('Arboreal Types in Wilderwood', fontsize=16, fontweight='bold')
plt.xlabel('Sun Exposure Avg. (Hrs/Day)', fontsize=12, fontweight='bold')
plt.ylabel('Moisture Intake Avg. (mm/Year)', fontsize=12, fontweight='bold')

# Add a color bar with changed label
color_bar = plt.colorbar(scatter)
color_bar.set_label('Tree Presence Scale', rotation=270, labelpad=20)

# Annotations with changed species names
for i, species in enumerate(tree_species):
    plt.annotate(species, (sunlight_hours[i], moisture_levels[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='black')

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()