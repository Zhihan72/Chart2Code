import matplotlib.pyplot as plt

# Define yields data for a single planetary colony (in metric tons per hectare)
mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]

# Create the vertical box plot for Mars yields
plt.figure(figsize=(6, 8))
box = plt.boxplot(mars_yields, vert=True, patch_artist=True, notch=True, whis=1.5)

# Customizing the appearance of the box
colors = ['#FF9999']
for patch in box['boxes']:
    patch.set_facecolor(colors[0])

# Plot styling
plt.title("Lunar Corn Yields in Mars Colony", fontsize=16, fontweight='bold')
plt.ylabel("Metric Tons per Hectare", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()