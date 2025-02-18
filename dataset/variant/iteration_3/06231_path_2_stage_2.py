import matplotlib.pyplot as plt
import numpy as np

species = np.array([
    "Sky Whales", "Mountain Dragons", "Valley Elves", 
    "Forest Trolls", "River Sprites",
    "Ice Wyrms", "Cave Goblins", "Swamp Beasts"
])

avg_altitudes = np.array([10000, 3500, 200, 300, 50, 4500, -200, 0])
avg_sizes = np.array([30, 20, 1.5, 3, 0.7, 15, 1, 7])
colors = ['skyblue', 'orange', 'green', 'forestgreen', 'blue', 'slateblue', 'brown', 'olive']

plt.figure(figsize=(14, 8))

plt.scatter(avg_altitudes, avg_sizes, s=avg_sizes * 70, c=colors, alpha=0.7, marker='^', edgecolor='grey')

for i, species_name in enumerate(species):
    plt.text(avg_altitudes[i] + 200, avg_sizes[i], species_name, fontsize=10, ha='right', color='darkblue')

plt.title('Exploring Fantasy World: \nAltitudes & Sizes of Species', fontsize=15, fontstyle='italic')

plt.xlabel('Altitude of Occurrence (meters)', fontsize=11, fontweight='light')
plt.ylabel('Size of Species (meters)', fontsize=11, fontweight='light')

# Added legend with size representation
legend_sizes = [1, 10, 30]
legend_labels = ['1m', '10m', '30m']
markers = [plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='grey', markersize=s*1.5) for s in legend_sizes]
plt.legend(markers, legend_labels, title='Size (m)', loc='upper left', frameon=False)

# Removed border lines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.grid(True, linestyle=':', linewidth=0.8, alpha=0.5)
plt.tight_layout()

plt.show()