import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy generation
energy_data = np.array([
    [200, 150, 100, 50],  # Europe
    [300, 200, 250, 30],  # Asia
    [250, 220, 180, 40],  # North America
    [120, 100, 300, 20],  # South America
    [180, 90, 70, 10]     # Africa
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar colors
colors = ['#ffcc99', '#99ff99', '#66b3ff', '#ff6666']

# Bar positions
xpos, ypos = np.meshgrid(np.arange(energy_data.shape[0]), np.arange(energy_data.shape[1]), indexing='ij')
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

dx = dy = 0.7

# Plotting each layer of the stack
for i in range(len(colors)):
    dz = energy_data[:, i]
    ax.bar3d(xpos[i::energy_data.shape[1]], ypos[i::energy_data.shape[1]], zpos[i::energy_data.shape[1]],
             dx, dy, dz, color=colors[i], alpha=0.8)
    zpos[i::energy_data.shape[1]] += dz

# Viewing angle for better visibility
ax.view_init(elev=30, azim=120)

plt.tight_layout()
plt.show()