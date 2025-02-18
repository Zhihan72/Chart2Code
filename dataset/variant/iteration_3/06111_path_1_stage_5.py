import matplotlib.pyplot as plt
import numpy as np

regions = ['N', 'S', 'E', 'W']
reusable_bags = [950, 1100, 800, 1200]

# Sort the data
sorted_indices = np.argsort(reusable_bags)[::-1]  # Descending order
sorted_regions = [regions[i] for i in sorted_indices]
sorted_bags = [reusable_bags[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(sorted_regions))

ax.barh(y_pos, sorted_bags, color='#ff6f61', edgecolor='black', linestyle='-', hatch='/')

ax.set_yticks(y_pos)
ax.set_yticklabels(sorted_regions, fontsize=11)
ax.set_xlabel('Units', fontsize=11)
ax.set_title('Sorted Reusable Bags Impact', fontsize=14, fontweight='bold', pad=15)

for i in range(len(sorted_regions)):
    ax.text(sorted_bags[i] + 20, i, str(sorted_bags[i]), va='center', color='black', fontsize=9)

plt.tight_layout()
plt.show()