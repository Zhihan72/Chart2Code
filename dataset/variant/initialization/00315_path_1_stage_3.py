import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# Data setup
parks = ['Liberty Park', 'Greenfield Park', 'Central Park', 'Riverside Park']
wildlife_categories = ['Mammals', 'Reptiles', 'Birds']

# Manually altered observations data
observations_data = np.array([
    [88, 76, 64],
    [142, 58, 40],
    [90, 84, 50],
    [115, 85, 49]
])

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

num_parks = len(parks)
num_wildlife_categories = len(wildlife_categories)
colors = plt.cm.plasma(np.linspace(0.3, 0.9, num_wildlife_categories))

for i in range(num_parks):
    x_positions = np.arange(num_wildlife_categories)
    y_positions = [i] * num_wildlife_categories
    z_positions = np.zeros(num_wildlife_categories)

    for j in range(num_wildlife_categories):
        ax.bar3d(
            x_positions[j], y_positions[j], z_positions[j], 
            dx=0.4, dy=0.4, dz=observations_data[i, j], 
            color=colors[j], alpha=0.8, edgecolor='b'
        )
        ax.text(
            x_positions[j], y_positions[j], observations_data[i, j] + 3,
            f'{observations_data[i, j]}', ha='center', va='bottom', fontsize=8, color='black'
        )

ax.set_xlabel('Animal Category', labelpad=15, fontsize=11)
ax.set_ylabel('Park Names', labelpad=15, fontsize=11)
ax.set_zlabel('Total Encounters', labelpad=15, fontsize=11)
ax.set_title('Nature Exploration:\nPark Animal Sightings (Year 2023)', pad=30, fontsize=14, fontweight='bold')

ax.set_xticks(np.arange(num_wildlife_categories))
ax.set_xticklabels(wildlife_categories, rotation=20, ha='right', fontsize=10, style='italic')
ax.set_yticks(np.arange(num_parks))
ax.set_yticklabels(parks, fontsize=10, fontstyle='oblique')

ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.3)

legend_handles = [Patch(color=colors[i], label=wildlife_categories[i]) for i in range(num_wildlife_categories)]
ax.legend(handles=legend_handles, loc='upper right', fontsize=10, title="Animal Types", title_fontsize=12, frameon=False)

ax.view_init(elev=40, azim=30)
plt.tight_layout()
plt.show()