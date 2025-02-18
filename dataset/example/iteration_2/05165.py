import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This plot shows the levels of water quality in different rivers across five regions over the past year.
# Each region has multiple rivers, and the water quality is measured on a scale of 0 to 100 (higher is better).

# Region and river data
regions = ['North', 'East', 'South', 'West', 'Central']
north_rivers = [85, 87, 90, 88, 83, 82, 85, 90, 95, 89]
east_rivers = [78, 75, 80, 72, 74, 79, 76, 77, 75, 78]
south_rivers = [88, 80, 85, 87, 83, 84, 86, 82, 85, 88]
west_rivers = [65, 62, 70, 68, 72, 71, 69, 64, 66, 67]
central_rivers = [90, 88, 92, 91, 89, 95, 93, 94, 90, 92]

# Combining data
river_qualities = [north_rivers, east_rivers, south_rivers, west_rivers, central_rivers]

# Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Box plot creation
box = ax.boxplot(river_qualities, patch_artist=True, notch=False, vert=True,
                 boxprops=dict(facecolor='#fafad2', color='black'),
                 medianprops=dict(color='red'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 flierprops=dict(marker='o', color='black', alpha=0.5))

# Set custom colors for each box
colors = ['#87CEFA', '#98FB98', '#FFA07A', '#DDA0DD', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Title and labels
ax.set_title('Water Quality Levels in Major Rivers Across Regions\nEnvironmental Research Report for 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Water Quality Score (0-100)', fontsize=12)
ax.set_xticks(np.arange(1, len(regions) + 1))
ax.set_xticklabels(regions, rotation=45, ha='right')

# Adding background info as text annotation
ax.text(0.95, 0.02, "Analyzed Time Period: Jan - Dec 2023\n\nHigh-quality water promotes healthy\n ecosystems and human well-being.",
        transform=ax.transAxes, fontsize=10, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='aliceblue', alpha=0.3))

# Grid for readability
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()