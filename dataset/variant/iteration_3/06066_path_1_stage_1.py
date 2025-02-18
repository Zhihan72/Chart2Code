import matplotlib.pyplot as plt
import numpy as np

# Average daily temperatures (in °C) for each forest type
boreal_temperatures = [7, 10, 12, 15, 17, 20, 22, 20, 18, 14, 10, 8]
temperate_temperatures = [12, 15, 18, 21, 24, 27, 29, 28, 26, 22, 18, 14]
tropical_temperatures = [22, 23, 24, 25, 26, 27, 28, 28, 27, 26, 24, 23]
data = [boreal_temperatures, temperate_temperatures, tropical_temperatures]

# Forest zones
forest_zones = ['Boreal', 'Temperate', 'Tropical']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Transpose the data to align with a horizontal violin plot
vparts = ax.violinplot(data, showmeans=False, showmedians=False, showextrema=False, vert=False)

# Color scheme for different forest types
colors = ['#556B2F', '#8B4513', '#FFD700']

# Customize the appearance of the violin plots
for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

# Scatter plot for individual data points
for i, temp_data in enumerate(data):
    y = np.random.normal(i + 1, 0.04, size=len(temp_data))
    ax.scatter(temp_data, y, alpha=0.7, color='black', zorder=5)

# Annotate median values
for i, forest_data in enumerate(data):
    median_val = np.median(forest_data)
    ax.text(median_val + 0.5, i + 1, f'{median_val:.1f}', verticalalignment='center', fontsize=12, color='darkred', weight='bold')

# Add title and labels
ax.set_title('Seasonal Variations in Daily Average Temperatures\nAcross Different Forest Zones', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Average Daily Temperature (°C)', fontsize=12)
ax.set_yticks(range(1, len(forest_zones) + 1))
ax.set_yticklabels(forest_zones)

# Grid and layout adjustments
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Custom Legend
handles = [plt.Line2D([0], [0], color=color, lw=4, label=zone) for color, zone in zip(colors, forest_zones)]
ax.legend(handles=handles, title='Forest Zones', loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()