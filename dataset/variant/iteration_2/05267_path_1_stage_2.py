import matplotlib.pyplot as plt
import numpy as np

tree_species = ['Oak', 'Pine', 'Maple', 'Birch', 'Redwood', 'Willow', 'Sequoia']
sunlight_hours = np.array([4, 6, 5, 8, 2, 9, 3])
moisture_levels = np.array([800, 600, 700, 500, 1200, 400, 1300])
prevalence = np.array([200, 250, 180, 300, 220, 270, 320])

plt.figure(figsize=(12, 8))
scatter = plt.scatter(sunlight_hours, moisture_levels, s=prevalence, c=prevalence, cmap='plasma', alpha=0.8)

plt.title('Tree Distribution in the Forest of Eldoria', fontsize=16, fontweight='bold')
plt.xlabel('Average Sunlight Exposure (Hours/Day)', fontsize=12, fontweight='bold')
plt.ylabel('Average Moisture Levels (mm/Year)', fontsize=12, fontweight='bold')

for i, species in enumerate(tree_species):
    plt.annotate(species, (sunlight_hours[i], moisture_levels[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='black')

plt.tight_layout()
plt.show()