import matplotlib.pyplot as plt
import numpy as np

# Data
celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Asteroids']
missions_data = {
    'Orbiters': [30, 40, 25, 50, 60, 10],
    'Landers': [20, 10, 45, 10, 5, 20],
    'Flybys': [50, 50, 30, 40, 35, 70]
}

# Creating a figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# X and Y positions for bars
x_pos = np.arange(len(celestial_bodies))
y_pos = np.arange(len(missions_data))

# Bar dimensions
bar_width = 0.2
bar_depth = 0.4

# Colors for mission types
colors = ['#FF5733', '#33FFCE', '#335BFF'] 

# Plot each mission type
for idx, (mission_type, percentages) in enumerate(missions_data.items()):
    x_offset = bar_width * idx  # Shifting each type on X-axis
    ax.bar3d(x_pos + x_offset, idx, [0] * len(percentages), bar_width, bar_depth, percentages,
             color=colors[idx], alpha=0.7)

# Remove axis labels, titles, and legend
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlim(0, len(celestial_bodies))
ax.set_ylim(0, len(missions_data))
ax.set_zlim(0, 100)

# Adjust layout to prevent overlap
plt.tight_layout()

# Viewing angle adjustments
ax.view_init(elev=25, azim=120)

# Display plot
plt.show()