import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# Define city parks and wildlife categories
parks = ['Liberty Park', 'Greenfield Park', 'Central Park', 'Riverside Park']
wildlife_categories = ['Mammals', 'Reptiles', 'Birds']

# Wildlife observation data
observations_data = np.array([
    [95, 70, 60],   # Riverside Park
    [150, 50, 35],  # Liberty Park
    [85, 90, 55],   # Greenfield Park
    [120, 80, 45]   # Central Park
])

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Plotting specifications
num_parks = len(parks)
num_wildlife_categories = len(wildlife_categories)
colors = plt.cm.viridis(np.linspace(0.2, 0.8, num_wildlife_categories))

# Plot each park's data
for i in range(num_parks):
    x_positions = np.arange(num_wildlife_categories)
    y_positions = [i] * num_wildlife_categories
    z_positions = np.zeros(num_wildlife_categories)
    
    # Bar plot
    ax.bar3d(
        x_positions, y_positions, z_positions, 
        dx=0.4, dy=0.4, dz=observations_data[i], 
        color=colors, alpha=0.9, edgecolor='k'
    )
    
    # Add annotations
    for j in range(num_wildlife_categories):
        ax.text(
            x_positions[j], y_positions[j], observations_data[i, j] + 3,
            f'{observations_data[i, j]}', ha='center', va='bottom', fontsize=8, color='black'
        )

# Set axis labels and title
ax.set_xlabel('Animal Category', labelpad=15, fontsize=11)
ax.set_ylabel('Park Names', labelpad=15, fontsize=11)
ax.set_zlabel('Total Encounters', labelpad=15, fontsize=11)
ax.set_title('Nature Exploration:\nPark Animal Sightings (Year 2023)', pad=30, fontsize=14)

# Set ticks and labels
ax.set_xticks(np.arange(num_wildlife_categories))
ax.set_xticklabels(wildlife_categories, rotation=20, ha='right', fontsize=10)
ax.set_yticks(np.arange(num_parks))
ax.set_yticklabels(parks, fontsize=10)

# Customize the grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Manually create legend
legend_handles = [Patch(color=colors[i], label=wildlife_categories[i]) for i in range(num_wildlife_categories)]
ax.legend(handles=legend_handles, loc='upper left', fontsize=10, title="Animal Types", title_fontsize=12, edgecolor='k')

# Adjust view angle for optimal visibility
ax.view_init(elev=35, azim=45)

# Adjust layout for optimal fit
plt.tight_layout()

# Display the plot
plt.show()