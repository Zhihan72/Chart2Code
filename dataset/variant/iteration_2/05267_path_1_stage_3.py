import matplotlib.pyplot as plt
import numpy as np

tree_species = ['Oak', 'Pine', 'Maple', 'Birch', 'Redwood', 'Willow', 'Sequoia']
sunlight_hours = np.array([4, 6, 5, 8, 2, 9, 3])
prevalence = np.array([200, 250, 180, 300, 220, 270, 320])

plt.figure(figsize=(12, 8))
horizontal_bar = plt.barh(tree_species, sunlight_hours, color=plt.cm.plasma(prevalence/max(prevalence)))

plt.title('Average Sunlight Exposure for Tree Species in Eldoria', fontsize=16, fontweight='bold')
plt.xlabel('Average Sunlight Exposure (Hours/Day)', fontsize=12, fontweight='bold')
plt.ylabel('Tree Species', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()