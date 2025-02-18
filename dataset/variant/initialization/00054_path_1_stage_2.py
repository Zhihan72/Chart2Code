import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap

# Data preparation
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']
# Manually shuffled capacities within each continent group
capacities = np.array([
    [80, 40, 120, 200],    # Africa
    [500, 100, 300, 200],  # Asia
    [150, 250, 60, 300],   # Europe
    [240, 50, 100, 180],   # North America
    [90, 40, 160, 180],    # South America
    [70, 30, 100, 120],    # Oceania
])

# Bar positions
xpos, ypos = np.meshgrid(np.arange(len(continents)), np.arange(len(energy_sources)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Bar dimensions and capacities
dx = dy = 0.4
dz = capacities.flatten()

# Create the figure and 3D axes
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Color map for the bars
cmap = LinearSegmentedColormap.from_list('capacity_cmap', ['#ffeda0', '#f03b20'])
norm = plt.Normalize(dz.min(), dz.max())

# Plot each energy source
for i in range(len(energy_sources)):
    xi = xpos[ypos == i]
    yi = ypos[ypos == i]
    zi = dz[ypos == i]
    ax.bar3d(xi, yi, zpos[ypos == i], dx, dy, zi, color=cmap(norm(zi)), alpha=0.9)
    for x, y, z in zip(xi, yi, zi):
        ax.text(x, y, z + 5, f'{z}', ha='center', va='bottom', fontsize=8, color='black')

# Labels and title
ax.set_xlabel('Continent', labelpad=16)
ax.set_ylabel('Energy Source', labelpad=16)
ax.set_zlabel('Capacity (GW)', labelpad=16)
ax.set_title('Renewable Energy Projections for 2025\nAcross Different Continents and Sources', pad=20)

# Custom tick labels
ax.set_xticks(np.arange(len(continents)) + dx/2)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(np.arange(len(energy_sources)) + dy/2)
ax.set_yticklabels(energy_sources)

# View angle adjustment
ax.view_init(elev=25, azim=135)

# Grid
ax.grid(True, linestyle='--', alpha=0.5)

# Colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Capacity Color Scale')

# Auto-layout
plt.tight_layout()

# Show plot
plt.show()