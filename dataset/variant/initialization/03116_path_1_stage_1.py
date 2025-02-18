import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

species_names = ['Roseus Majestica', 'Sunbloom Radiant', 'Willow Whisperer', 
                 'Oak Heartbound', 'Skywing Faera', 'Moonlight Howler']
species_data = [
    [30, 40, 300, 150],
    [50, 20, 150, 100],
    [60, 45, 400, 250],
    [70, 55, 200, 200],
    [35, 50, 350, 350],
    [45, 25, 280, 300]
]

longitudes = [data[0] for data in species_data]
latitudes = [data[1] for data in species_data]
populations = [data[2] for data in species_data]
impacts = [data[3] for data in species_data]

colors = ['#FF6347', '#FFD700', '#8B4513', '#32CD32', '#4169E1', '#9370DB']
marker_styles = ['o', 'v', '^', '<', '>', 'd']  # Randomly chosen marker styles
line_styles = ['-', '--', '-.', ':']

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

for i, species in enumerate(species_names):
    ax.scatter(longitudes[i], latitudes[i], populations[i], s=impacts[i], c=colors[i],
               label=species, alpha=0.7, edgecolors='b', marker=marker_styles[i])

ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_zlabel('Population in Thousands', fontsize=12)
ax.set_title('Biodiversity Interaction in TerraLuna\nFlora and Fauna Dynamics', fontsize=16, fontweight='bold', pad=20)

ax.legend(title="Species", loc='upper right', fontsize=9, title_fontsize='10', frameon=True)

ax.grid(True, linestyle=line_styles[1])

ax.view_init(elev=20, azim=50)

plt.tight_layout()
plt.show()