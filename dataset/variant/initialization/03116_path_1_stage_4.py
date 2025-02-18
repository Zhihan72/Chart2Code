import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

species_names = ['Moonlight Howler', 'Sunbloom Radiant', 'Skywing Faera', 
                 'Willow Whisperer', 'Roseus Majestica', 'Oak Heartbound']
species_data = [
    [60, 45, 350, 300],
    [20, 60, 300, 150],
    [45, 35, 150, 250],
    [55, 70, 250, 200],
    [40, 50, 200, 100],
    [25, 30, 400, 350]
]

longitudes = [data[0] for data in species_data]
latitudes = [data[1] for data in species_data]
populations = [data[2] for data in species_data]
impacts = [data[3] for data in species_data]

consistent_color = '#8B4513'
marker_styles = ['v', 'o', '^', '<', '>', 'd']

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

for i, species in enumerate(species_names):
    ax.scatter(longitudes[i], latitudes[i], populations[i], s=impacts[i], c=consistent_color,
               label=species, alpha=0.7, edgecolors='b', marker=marker_styles[i])

ax.set_xlabel('Latitude Range', fontsize=12)
ax.set_ylabel('Longitude Span', fontsize=12)
ax.set_zlabel('Habitants Count', fontsize=12)
ax.set_title('Ecological Patterns in TerraLuna\nPlant and Creature Routes', 
             fontsize=16, fontweight='bold', pad=20)

ax.legend(title="Creature Groups", loc='upper right', fontsize=9, title_fontsize='10', frameon=True)

ax.grid(True, linestyle='-.')

ax.view_init(elev=20, azim=50)

plt.tight_layout()
plt.show()