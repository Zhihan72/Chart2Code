import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Backstory: Explore the data on the daily average temperatures observed in the Boreal, Temperate, and Tropical forests
# to analyze the seasonal variations. The zones represent different types of forests that are affected differently by 
# global climatic conditions.

# Data: Average daily temperatures (in °C) for each forest type
boreal_temperatures = [7, 10, 12, 15, 17, 20, 22, 20, 18, 14, 10, 8]
temperate_temperatures = [12, 15, 18, 21, 24, 27, 29, 28, 26, 22, 18, 14]
tropical_temperatures = [22, 23, 24, 25, 26, 27, 28, 28, 27, 26, 24, 23]
data = [boreal_temperatures, temperate_temperatures, tropical_temperatures]

# Forest zones
forest_zones = ['Boreal', 'Temperate', 'Tropical']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Violin plot for forest temperature data
vparts = ax.violinplot(data, showmeans=False, showmedians=False, showextrema=False, widths=0.7)

# Color scheme for different forest types
colors = ['#556B2F', '#8B4513', '#FFD700']

# Customize the appearance of the violin plots
for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

# Box plot to show detailed distribution
box = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.2, labels=forest_zones, showfliers=False)

# Modify box plot colors according to the forest zones
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.setp(box['medians'], color='red', linewidth=2)
plt.setp(box['whiskers'], color='blue', linewidth=1.5, linestyle='--')
plt.setp(box['caps'], color='black', linewidth=1.5)

# Scatter plot for individual data points in the violin plot
for i, temp_data in enumerate(data):
    x = np.random.normal(i + 1, 0.04, size=len(temp_data))
    ax.scatter(x, temp_data, alpha=0.7, color='black', zorder=5)

# Annotate median values
for i, forest_data in enumerate(data):
    median_val = np.median(forest_data)
    ax.text(i + 1, median_val + 1, f'{median_val:.1f}', horizontalalignment='center', fontsize=12, color='darkred', weight='bold')

# Add title and labels
ax.set_title('Seasonal Variations in Daily Average Temperatures\nAcross Different Forest Zones', fontsize=16, weight='bold', pad=20)
ax.set_ylabel('Average Daily Temperature (°C)', fontsize=12)
ax.set_xlabel('Forest Zones', fontsize=12)

# Grid and layout adjustments
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Custom Legend
handles = [plt.Line2D([0], [0], color=color, lw=4, label=zone) for color, zone in zip(colors, forest_zones)]
ax.legend(handles=handles, title='Forest Zones', loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()