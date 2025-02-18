import matplotlib.pyplot as plt
import numpy as np

species = np.array([
    "Sky Whales", "Mountain Dragons", "Valley Elves", 
    "Forest Trolls", "River Sprites",
    "Ice Wyrms", "Cave Goblins", "Swamp Beasts"
])

avg_altitudes = np.array([10000, 3500, 200, 300, 50, 4500, -200, 0])
avg_sizes = np.array([30, 20, 1.5, 3, 0.7, 15, 1, 7])
new_colors = ['red', 'blue', 'purple', 'cyan', 'magenta', 'pink', 'coral', 'gold']

plt.figure(figsize=(14, 8))

plt.scatter(avg_altitudes, avg_sizes, s=avg_sizes * 70, c=new_colors, alpha=0.7, marker='^', edgecolor='grey')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.grid(True, linestyle=':', linewidth=0.8, alpha=0.5)
plt.tight_layout()

plt.show()