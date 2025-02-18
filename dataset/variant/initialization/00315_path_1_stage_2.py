import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# Data setup
parks = ['Liberty Park', 'Greenfield Park', 'Central Park', 'Riverside Park']
wildlife_categories = ['Mammals', 'Reptiles', 'Birds']

observations_data = np.array([
    [95, 70, 60],
    [150, 50, 35],
    [85, 90, 55],
    [120, 80, 45]
])

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Parameters
num_parks = len(parks)
num_wildlife_categories = len(wildlife_categories)
colors = plt.cm.plasma(np.linspace(0.3, 0.9, num_wildlife_categories))  # Color palette

# Loop through parks
for i in range(num_parks):
    x_positions = np.arange(num_wildlife_categories)  # Wildlife categories
    y_positions = [i] * num_wildlife_categories  # Same park index
    z_positions = np.zeros(num_wildlife_categories)  # Base of bars

    # Loop through wildlife categories to assign colors individually
    for j in range(num_wildlife_categories):
        ax.bar3d(
            x_positions[j], y_positions[j], z_positions[j], 
            dx=0.4, dy=0.4, dz=observations_data[i, j], 
            color=colors[j], alpha=0.8, edgecolor='b'
        )
        # Add text annotation for each bar
        ax.text(
            x_positions[j], y_positions[j], observations_data[i, j] + 3,
            f'{observations_data[i, j]}', ha='center', va='bottom', fontsize=8, color='black'
        )

# Set labels and title
ax.set_xlabel('Animal Category', labelpad=15, fontsize=11)
ax.set_ylabel('Park Names', labelpad=15, fontsize=11)
ax.set_zlabel('Total Encounters', labelpad=15, fontsize=11)
ax.set_title('Nature Exploration:\nPark Animal Sightings (Year 2023)', pad=30, fontsize=14, fontweight='bold')

# Customize ticks
ax.set_xticks(np.arange(num_wildlife_categories))
ax.set_xticklabels(wildlife_categories, rotation=20, ha='right', fontsize=10, style='italic')
ax.set_yticks(np.arange(num_parks))
ax.set_yticklabels(parks, fontsize=10, fontstyle='oblique')

# Grid styling
ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.3)

# Legend
legend_handles = [Patch(color=colors[i], label=wildlife_categories[i]) for i in range(num_wildlife_categories)]
ax.legend(handles=legend_handles, loc='upper right', fontsize=10, title="Animal Types", title_fontsize=12, frameon=False)

# Adjust viewing angle
ax.view_init(elev=40, azim=30)

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()