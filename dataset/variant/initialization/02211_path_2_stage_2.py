import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_types = ['Solar', 'Wind', 'Hydro', 'Bioenergy']

energy_percentages = np.array([
    [25, 35, 10, 30], 
    [25, 15, 40, 20], 
    [15, 40, 20, 25],  
    [25, 10, 35, 30],  
    [15, 35, 20, 30],  
    [50, 10, 20, 20]   
])

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

# Changed line styles and marker shapes
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=np.repeat(colors, len(continents)), edgecolor='black', linestyle='dashed')

ax.set_xlabel('Continents')
ax.set_ylabel('Energy Types')
ax.set_zlabel('Percentage')
ax.set_title('Mapping the Future:\nRenewable Energy Adoption Across the Continents (2050 Projections)', 
             fontsize=14, fontweight='bold', pad=20)

ax.set_xticks(x_positions)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(y_positions)
ax.set_yticklabels(energy_types)

# Altered legend's position and style
legend_labels = ['Solar', 'Wind', 'Hydro', 'Bioenergy']
color_patches = [plt.Line2D([0], [0], color=color, linewidth=4, linestyle='dotted') for color in colors]
ax.legend(color_patches, legend_labels, loc='lower right', title="Energy Types", fontsize=9)

# Adding gridlines
ax.grid(True, linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()