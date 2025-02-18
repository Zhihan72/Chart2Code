import matplotlib.pyplot as plt

mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]

plt.figure(figsize=(6, 8))
box = plt.boxplot(mars_yields, vert=True, patch_artist=True, notch=True, whis=1.5)

# Customizing the appearance of the box with a shuffled color
colors = ['#FF9999', '#99FF99', '#9999FF']
selected_color = colors[1]  # Simulating a shuffled color by selecting a different index
for patch in box['boxes']:
    patch.set_facecolor(selected_color)

plt.title("Lunar Corn Yields in Mars Colony", fontsize=16, fontweight='bold')
plt.ylabel("Metric Tons per Hectare", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()