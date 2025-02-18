import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

species_names = ['Roseus Majestica', 'Sunbloom Radiant', 'Willow Whisperer', 
                 'Oak Heartbound', 'Skywing Faera', 'Moonlight Howler']
species_data = [
    [40, 50, 200, 100],  # Values manually shuffled
    [20, 60, 300, 150],
    [45, 35, 150, 250],
    [55, 70, 250, 200],
    [60, 45, 350, 300],
    [25, 30, 400, 350]
]

longitudes = [data[0] for data in species_data]
latitudes = [data[1] for data in species_data]
populations = [data[2] for data in species_data]
impacts = [data[3] for data in species_data]

colors = ['#FFD700', '#32CD32', '#9370DB', '#8B4513', '#FF6347', '#4169E1']  # Shuffled color list
marker_styles = ['v', 'o', '^', '<', '>', 'd']  # Shuffled marker styles
line_styles = ['--', '-.', '-', ':']  # Kept the same to adhere to the requirement

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

for i, species in enumerate(species_names):
    ax.scatter(longitudes[i], latitudes[i], populations[i], s=impacts[i], c=colors[i],
               label=species, alpha=0.7, edgecolors='b', marker=marker_styles[i])

ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_zlabel('Population in Thousands', fontsize=12)
ax.set_title('Biodiversity Interaction in TerraLuna\nFlora and Fauna Dynamics', 
             fontsize=16, fontweight='bold', pad=20)

ax.legend(title="Species", loc='upper right', fontsize=9, title_fontsize='10', frameon=True)

ax.grid(True, linestyle=line_styles[1])

ax.view_init(elev=20, azim=50)

plt.tight_layout()
plt.show()