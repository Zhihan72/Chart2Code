import matplotlib.pyplot as plt
import numpy as np

# Yields of different fruits (in tons) from four different orchards over 10 years
apple_yield = [30, 35, 40, 32, 33, 36, 38, 37, 34, 31]
orange_yield = [25, 28, 22, 26, 29, 24, 21, 27, 23, 26]
pear_yield = [15, 17, 13, 18, 16, 14, 19, 12, 16, 15]
cherry_yield = [10, 13, 9, 11, 14, 8, 7, 10, 12, 13]

# Combine data into a list for the box plot
data = [apple_yield, orange_yield, pear_yield, cherry_yield]

# Labels for the different fruits
fruit_labels = ['Apples', 'Oranges', 'Pears', 'Cherries']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the box plot
boxplot = ax.boxplot(data, vert=True, patch_artist=True, labels=fruit_labels, widths=0.6, notch=True)

# Manually shuffled colors for each fruit box
colors = ['#FFD700', '#FF69B4', '#FF6347', '#90EE90']  # New order of colors
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, and medians
for whisker in boxplot['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')

for cap in boxplot['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)

for median in boxplot['medians']:
    median.set(color='black', linewidth=2)

# Title and labels
ax.set_title("Orchard Productivity Comparison (2010-2020)\nAnnual Yield (in tons) of Different Fruits", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Types of Fruits', fontsize=12)
ax.set_ylabel('Annual Yield (in tons)', fontsize=12)

# Add grids for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Adding annotations for outliers
for i, line in enumerate(boxplot['fliers']):
    y = line.get_ydata()
    x = line.get_xdata()
    for (xi, yi) in zip(x, y):
        ax.text(xi, yi, f'{yi}', va='bottom', ha='right', fontsize=8, color=colors[i % len(colors)], alpha=0.8)

# Adjust the layout to avoid overlapping and to ensure everything fits well
plt.tight_layout()

# Display the chart
plt.show()