import matplotlib.pyplot as plt
import numpy as np

species = np.array([
    "Sky Whales", "Mountain Dragons", "Valley Elves", 
    "Desert Giants", "Forest Trolls", "River Sprites",
    "Ice Wyrms", "Cave Goblins", "Swamp Beasts"
])

avg_altitudes = np.array([10000, 3500, 200, 50, 300, 50, 4500, -200, 0])
avg_sizes = np.array([30, 20, 1.5, 10, 3, 0.7, 15, 1, 7])
colors = ['skyblue', 'orange', 'green', 'sandybrown', 'forestgreen', 'blue', 'slateblue', 'brown', 'olive']

plt.figure(figsize=(14, 8))
plt.scatter(avg_altitudes, avg_sizes, s=avg_sizes * 70, c=colors, alpha=0.6)

for i, species_name in enumerate(species):
    plt.text(avg_altitudes[i] + 200, avg_sizes[i], species_name, fontsize=9, ha='center', color='darkred')

plt.xlabel('Average Altitude of Occurrence (meters)', fontsize=12)
plt.ylabel('Average Size of Species (meters)', fontsize=12)
plt.tight_layout()

plt.show()