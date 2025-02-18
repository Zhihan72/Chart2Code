import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

species_names = ['R. Majestica', 'S. Radiant', 'W. Whisperer', 
                 'O. Heartbound', 'S. Faera', 'M. Howler']

species_data = [
    [30, 40, 300, 150],  # R. Majestica
    [50, 20, 150, 100],  # S. Radiant
    [60, 45, 400, 250],  # W. Whisperer
    [70, 55, 200, 200],  # O. Heartbound
    [35, 50, 350, 350],  # S. Faera
    [45, 25, 280, 300]   # M. Howler
]

longitudes = [data[0] for data in species_data]
latitudes = [data[1] for data in species_data]
populations = [data[2] for data in species_data]
impacts = [data[3] for data in species_data]

# New colors for the plot
colors = ['#E9967A', '#F0E68C', '#98FB98', '#6495ED', '#BA55D3', '#FF4500']

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

for i, species in enumerate(species_names):
    ax.scatter(longitudes[i], latitudes[i], populations[i], s=impacts[i], c=colors[i], label=species, alpha=0.6, edgecolors='k')

ax.set_xlabel('Long', fontsize=10)
ax.set_ylabel('Lat', fontsize=10)
ax.set_zlabel('Pop (K)', fontsize=10)
ax.set_title('Biodiversity in TerraLuna', fontsize=14, fontweight='bold', pad=20)

ax.legend(title="Species", loc='upper left', fontsize=10, title_fontsize='11', bbox_to_anchor=(1.1, 0.85))
ax.view_init(elev=15, azim=40)

plt.tight_layout()
plt.show()