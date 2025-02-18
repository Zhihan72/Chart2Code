import matplotlib.pyplot as plt
import numpy as np

# Story: Climate Change Impact on Crop Yields
# This study examines the distribution of wheat, corn, and rice yields across three agricultural regions
# (North America, Europe, and Asia) for the year 2022. The goal is to visualize the variability and
# distribution to draw insights about the impact of climate change on these crops.

# Define regions and crops
regions = ['North America', 'Europe', 'Asia']
crops = ['Wheat', 'Corn', 'Rice']

# Data representing crop yields (in tons per hectare) for 2022
# North America data
wheat_na = [3.2, 3.5, 3.6, 4.0, 4.2, 3.9, 4.1, 3.8, 4.0, 3.7]
corn_na = [10.5, 11.0, 11.2, 10.8, 10.9, 11.1, 10.7, 10.8, 11.3, 10.9]
rice_na = [7.8, 8.0, 7.9, 8.2, 8.3, 8.1, 8.0, 7.8, 8.2, 8.1]

# Europe data
wheat_eu = [5.5, 5.4, 5.6, 5.7, 5.8, 5.5, 5.6, 5.4, 5.7, 5.5]
corn_eu = [9.0, 8.8, 8.9, 9.2, 9.1, 8.7, 9.0, 9.1, 8.8, 8.9]
rice_eu = [6.5, 6.6, 6.7, 6.5, 6.8, 6.4, 6.6, 6.5, 6.6, 6.7]

# Asia data
wheat_as = [3.8, 3.9, 4.0, 4.1, 4.2, 4.0, 4.1, 3.9, 4.0, 4.1]
corn_as = [5.5, 5.6, 5.7, 5.6, 5.5, 5.7, 5.6, 5.5, 5.4, 5.6]
rice_as = [9.2, 9.3, 9.1, 9.2, 9.3, 9.1, 9.2, 9.0, 9.3, 9.1]

# Organize the data for the box plot
data_wheat = [wheat_na, wheat_eu, wheat_as]
data_corn = [corn_na, corn_eu, corn_as]
data_rice = [rice_na, rice_eu, rice_as]

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

# Titles and labels
axes[0].set_title('Wheat Yields in 2022', fontsize=14, fontweight='bold')
axes[1].set_title('Corn Yields in 2022', fontsize=14, fontweight='bold')
axes[2].set_title('Rice Yields in 2022', fontsize=14, fontweight='bold')

# Plot Wheat Yields
box_wheat = axes[0].boxplot(data_wheat, vert=True, patch_artist=True, labels=regions, notch=True)
for patch in box_wheat['boxes']:
    patch.set_facecolor('#FF9999')
axes[0].set_ylabel('Yield (tons per hectare)', fontsize=12)

# Plot Corn Yields
box_corn = axes[1].boxplot(data_corn, vert=True, patch_artist=True, labels=regions, notch=True)
for patch in box_corn['boxes']:
    patch.set_facecolor('#99FF99')
axes[1].set_xlabel('Regions', fontsize=12)

# Plot Rice Yields
box_rice = axes[2].boxplot(data_rice, vert=True, patch_artist=True, labels=regions, notch=True)
for patch in box_rice['boxes']:
    patch.set_facecolor('#66B3FF')

# Add grid
for ax in axes:
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.set_axisbelow(True)

# Common title
fig.suptitle('Climate Change Impact on Crop Yields in 2022', fontsize=16, fontweight='bold', y=0.98)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show plot
plt.show()