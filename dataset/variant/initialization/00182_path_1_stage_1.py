import matplotlib.pyplot as plt

# Define yields data for a single group
mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]

# Create the vertical box plot for a single group of data
plt.figure(figsize=(6, 8))
box = plt.boxplot(mars_yields, vert=True, patch_artist=True, notch=True, whis=1.5)

# Customizing the appearance of the box
box['boxes'][0].set_facecolor('#FF9999')

# Additional plot styling
plt.title("Space Farming Yield for Mars", fontsize=16, fontweight='bold')
plt.ylabel("Yield (metric tons per hectare)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot with tight layout
plt.tight_layout()
plt.show()