import matplotlib.pyplot as plt
import numpy as np

# Data setup
percentage_data = np.array([
    [30, 40, 20, 10],  # Ancient Archives
    [25, 35, 30, 10],  # Renaissance Repository
    [40, 20, 20, 20],  # Modern Manuscript Collection
])

# Create figure and 3D axes
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar positions
xpos, ypos = np.meshgrid(np.arange(4), np.arange(3))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Define bar sizes
dx = dy = 0.8
dz = percentage_data.flatten()

single_color = '#66B3FF'

# Plot bars
for i in range(len(xpos)):
    ax.bar3d(xpos[i], ypos[i], zpos[i], dx, dy, dz[i], 
             color=single_color, zsort='average')

# Customize the axes
ax.set_zlim(0, 50)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()