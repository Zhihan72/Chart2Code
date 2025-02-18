import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Monthly Climate Variations in Different Cities
# The goal is to compare the temperature variability within a month in five different cities globally.

# Cities
cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Cairo']

# Monthly temperature data (in Celsius) for each city
temperatures = [
    [5, 6, 8, 7, 6, 5, 7, 8, 9, 4, 5, 5, 6, 7, 8, 5, 6, 7, 10, 6, 7, 5, 8, 9],        # New York
    [7, 8, 10, 9, 8, 8, 9, 10, 11, 8, 9, 8, 10, 9, 8, 9, 10, 11, 10, 9, 8, 10, 9, 8], # London
    [12, 13, 12, 15, 13, 14, 13, 14, 15, 13, 14, 15, 13, 12, 14, 16, 13, 14, 15, 13, 14, 15, 13, 14], # Tokyo
    [18, 20, 19, 21, 22, 18, 20, 17, 20, 21, 19, 17, 18, 19, 20, 18, 19, 17, 20, 19, 21, 17, 18, 20], # Sydney
    [23, 25, 22, 24, 23, 25, 24, 23, 24, 25, 22, 24, 23, 24, 22, 25, 23, 24, 25, 23, 24, 25, 22, 23]  # Cairo
]

# Create the horizontal box plot with customized appearance
fig, ax = plt.subplots(figsize=(14, 8))
bplot = ax.boxplot(temperatures, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='wheat', color='chocolate', linewidth=1.5),
                   whiskerprops=dict(color='chocolate', linewidth=1.5),
                   capprops=dict(color='chocolate', linewidth=1.5),
                   medianprops=dict(color='red', linewidth=1.5),
                   flierprops=dict(markerfacecolor='chocolate', marker='o', markersize=6, alpha=0.6))

# Set y-tick labels
ax.set_yticklabels(cities, fontsize=12)

# Set title and labels with adjusted font sizes
ax.set_title('Comparative Analysis of Monthly Temperature Variations\nAcross Different Cities', fontsize=16, fontweight='bold')
ax.set_xlabel('Temperature (Celsius)', fontsize=14)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Customize the appearance of each box with distinct colors
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightpink', 'lightyellow']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Automatically adjust layout to prevent any overlap
plt.tight_layout()

# Display the plot
plt.show()