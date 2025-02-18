import matplotlib.pyplot as plt
import numpy as np

# New species names
species = np.array([
    "Shadow Goblins", "Bog Creatures", "Highland Dragons", 
    "Stream Spirits", "Cloud Leviathans", "Frost Serpents",
    "Arid Colossi", "Woodland Ogres", "Dale Fairies"
])

avg_altitudes = np.array([-200, 0, 3500, 50, 10000, 4500, 50, 300, 200])
avg_sizes = np.array([1, 7, 20, 0.7, 30, 15, 10, 3, 1.5])

# Same color set, retaining consistency
colors = ['magenta', 'cyan', 'yellow', 'black', 'red', 'purple', 'lime', 'navy', 'teal']

plt.figure(figsize=(14, 8))
plt.scatter(avg_altitudes, avg_sizes, s=avg_sizes * 70, c=colors, alpha=0.6)

for i, species_name in enumerate(species):
    plt.text(avg_altitudes[i] + 200, avg_sizes[i], species_name, fontsize=9, ha='center', color='darkred')

# Modified axis labels
plt.xlabel('Habitual Elevation (meters)', fontsize=12)
plt.ylabel('Creature Dimensions (meters)', fontsize=12)
plt.tight_layout()

plt.show()