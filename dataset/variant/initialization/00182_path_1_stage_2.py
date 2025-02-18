import matplotlib.pyplot as plt

# Define yields data for multiple groups
mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]
venus_yields = [18, 22, 19, 17, 23, 20, 21, 20, 18, 21, 19, 22]
jupiter_yields = [21, 24, 20, 18, 26, 23, 25, 22, 21, 23, 22, 25]

data = [mars_yields, venus_yields, jupiter_yields]

# Create the vertical box plot for multiple groups of data
plt.figure(figsize=(8, 8))
box = plt.boxplot(data, vert=True, patch_artist=True, notch=True, whis=1.5, labels=['Mars', 'Venus', 'Jupiter'])

# Customizing the appearance of the boxes
colors = ['#FF9999', '#66B3FF', '#99FF99']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Additional plot styling
plt.title("Space Farming Yields for Different Planets", fontsize=16, fontweight='bold')
plt.ylabel("Yield (metric tons per hectare)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot with tight layout
plt.tight_layout()
plt.show()