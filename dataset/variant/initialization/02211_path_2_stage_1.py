import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define continents and renewable energy types
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_types = ['Solar', 'Wind', 'Hydro', 'Bioenergy']

# Modified renewable energy percentages after random alteration
energy_percentages = np.array([
    [25, 35, 10, 30],  # Africa (shuffled)
    [25, 15, 40, 20],  # Asia (shuffled)
    [15, 40, 20, 25],  # Europe (shuffled)
    [25, 10, 35, 30],  # North America (shuffled)
    [15, 35, 20, 30],  # South America (shuffled)
    [50, 10, 20, 20]   # Oceania (same)
])

# Create a figure for the 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_positions = np.arange(len(continents))
y_positions = np.arange(len(energy_types))
xpos, ypos = np.meshgrid(x_positions, y_positions)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

dz = energy_percentages.flatten()
dx = dy = 0.8
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=np.repeat(colors, len(continents)))

ax.set_xlabel('Continents')
ax.set_ylabel('Energy Types')
ax.set_zlabel('Percentage')
ax.set_title('Mapping the Future:\nRenewable Energy Adoption Across the Continents (2050 Projections)', 
             fontsize=14, fontweight='bold', pad=20)

ax.set_xticks(x_positions)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(y_positions)
ax.set_yticklabels(energy_types)

legend_labels = ['Solar', 'Wind', 'Hydro', 'Bioenergy']
color_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(color_patches, legend_labels, loc='upper left', bbox_to_anchor=(1.05, 1), title="Energy Types")

plt.tight_layout()
plt.show()