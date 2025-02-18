import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Tomatoes', 'Cucumbers', 'Carrots', 'Peppers', 'Zucchinis']
yields = {
    'Tomatoes': [15, 20, 22, 18, 25, 30, 35, 24, 28, 23, 19, 29, 31, 27, 21],
    'Cucumbers': [10, 15, 12, 18, 11, 17, 14, 20, 21, 16, 13, 19, 22, 10, 18],
    'Carrots': [9, 11, 13, 15, 14, 12, 10, 16, 18, 11, 14, 15, 17, 19, 12],
    'Peppers': [6, 8, 7, 11, 9, 12, 13, 10, 14, 12, 11, 9, 8, 13, 7],
    'Zucchinis': [20, 22, 24, 26, 28, 30, 25, 27, 23, 29, 21, 24, 26, 28, 22]
}

# Collect the yields data for each vegetable
data = [yields[veg] for veg in vegetables]

# Constructing a simple trend line that shows the average yield per vegetable type
average_yields = [np.mean(yields[veg]) for veg in vegetables]

# Plotting the graph
fig, ax = plt.subplots(figsize=(14, 8))

# Create the horizontal box plot
box = ax.boxplot(data, patch_artist=True, labels=vegetables, notch=True, vert=False, positions=range(1, len(vegetables) + 1), widths=0.6)

# Customize the box plot
colors = ['#FFDEAD', '#ADFF2F', '#F08080', '#9370DB', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
for whisker in box['whiskers']:
    whisker.set(color='black', linestyle='-', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
for median in box['medians']:
    median.set(color='red', linewidth=2)
for flier in box['fliers']:
    flier.set(markerfacecolor='orange', marker='o', markersize=6)

# Overlay scatter plot for average yields
ax.scatter(average_yields, range(1, len(vegetables) + 1), color='blue', s=100, zorder=3, label='Average Yield')

# Set titles and labels
ax.set_title('Fresh Harvest Urban Garden Initiative\nVegetable Yields Distribution (in kg)', fontsize=16, fontweight='bold')
ax.set_xlabel('Yield (Kg)', fontsize=12)
ax.set_ylabel('Vegetable Type', fontsize=12)

# Adding grid
ax.xaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax.set_axisbelow(True)

# Legend handling
color_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(color_patches + [plt.Line2D([0], [0], color='blue', marker='o', lw=0, markersize=10)],
          vegetables + ['Average Yield'], title='Legend', loc='upper left', fontsize=10, frameon=True)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()