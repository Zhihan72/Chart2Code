import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

species_names = ['R. Majestica', 'S. Radiant', 'W. Whisperer', 
                 'S. Faera', 'M. Howler']

species_data = [
    [30, 40, 300, 150],
    [50, 20, 150, 100],
    [60, 45, 400, 250],
    [35, 50, 350, 350],
    [45, 25, 280, 300]
]

longitudes = [data[0] for data in species_data]
latitudes = [data[1] for data in species_data]
populations = [data[2] for data in species_data]
impacts = [data[3] for data in species_data]

colors = ['#FF6347', '#FFFFE0', '#00FA9A', '#9932CC', '#FF8C00']
markers = ['o', 'v', '^', '>', 's']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i, species in enumerate(species_names):
    ax.scatter(longitudes[i], latitudes[i], populations[i], s=impacts[i], c=colors[i],
               label=species, alpha=0.7, edgecolors='w', marker=markers[i])

ax.set_xlabel('Longitude', fontsize=12, color='gray')
ax.set_ylabel('Latitude', fontsize=12, color='gray')
ax.set_zlabel('Population (K)', fontsize=12, color='gray')
ax.set_title('Biodiversity in TerraLuna', fontsize=16, color='navy', fontweight='bold')

ax.legend(title="Species", loc='upper right', fontsize=9, title_fontsize='10')
ax.grid(True, linestyle='--', alpha=0.7)
ax.view_init(elev=22, azim=30)

plt.subplots_adjust(left=0.1, right=0.8)
plt.show()