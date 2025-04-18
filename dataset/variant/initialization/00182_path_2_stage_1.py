import matplotlib.pyplot as plt
import numpy as np

# Define yields data for each planetary colony (in metric tons per hectare)
mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]
venus_yields = [18, 19, 17, 20, 19, 21, 22, 20, 19, 21, 18, 20]
titan_yields = [15, 14, 16, 13, 14, 15, 17, 13, 14, 16, 15, 14]

# Combine yields into a list for plotting
all_yields = [mars_yields, venus_yields, titan_yields]
colony_names = ['Mars', 'Venus', 'Titan']

# Create the horizontal box plot
plt.figure(figsize=(12, 8))
box = plt.boxplot(all_yields, vert=False, patch_artist=True, labels=colony_names, notch=True, whis=1.5)

# Customizing the appearance of the boxes
colors = ['#FF9999', '#66B3FF', '#FFCC99']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Additional plot styling
plt.title("Space Farming Yields:\nLunar Corn Across Planetary Colonies", fontsize=16, fontweight='bold')
plt.xlabel("Yield (metric tons per hectare)", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show plot with tight layout
plt.tight_layout()
plt.show()