import matplotlib.pyplot as plt
import numpy as np

# Defining species names
species = np.array([
    "Sky Whales", "Mountain Dragons", "Valley Elves", 
    "Forest Trolls", "River Sprites",
    "Ice Wyrms", "Cave Goblins", "Swamp Beasts"
])

# Average altitudes of occurrence in meters
avg_altitudes = np.array([10000, 3500, 200, 300, 50, 4500, -200, 0])

# Average sizes of the species in meters
avg_sizes = np.array([30, 20, 1.5, 3, 0.7, 15, 1, 7])

# Colors based on habitat
colors = ['skyblue', 'orange', 'green', 'forestgreen', 'blue', 'slateblue', 'brown', 'olive']

plt.figure(figsize=(14, 8))

# Scatter plot: Average altitude vs Average size
plt.scatter(avg_altitudes, avg_sizes, s=avg_sizes * 70, c=colors, alpha=0.6, edgecolor='k')

# Adding species labels at slightly adjusted positions
for i, species_name in enumerate(species):
    plt.text(avg_altitudes[i] + 200, avg_sizes[i], species_name, fontsize=9, ha='center', color='darkred')

# Title and labels
plt.title('Exploring Fantasy World: \nAverage Altitudes and Sizes of Species', fontsize=16, fontweight='bold')
plt.xlabel('Average Altitude of Occurrence (meters)', fontsize=12)
plt.ylabel('Average Size of Species (meters)', fontsize=12)

# Grid and layout adjustments
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()