import matplotlib.pyplot as plt
import numpy as np

# Yield data
tomatoes_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53]
lettuce_yield = [30, 28, 32, 25, 31, 29, 27, 30, 28, 35]
carrots_yield = [40, 42, 45, 38, 47, 44, 39, 41, 43, 40]

# Combine data for plotting
data = [tomatoes_yield, lettuce_yield, carrots_yield]

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal box plot without style elements
box = ax.boxplot(data, vert=False, patch_artist=True,
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 notch=True)

# Set colors for each box
colors = ['orange', 'lightgreen', 'skyblue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Hide borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Remove labels
ax.set_xlabel("")
ax.set_ylabel("")

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()