import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Abbreviated habitat names
habitats = ["TropRF", "TempF", "BorF", "Mangr", "Savn"]
years = np.arange(2030, 2040)

mammals = np.array([
    [24, 22, 21, 30, 28, 27, 26, 25, 24, 23],
    [28, 29, 35, 29, 32, 31, 30, 34, 33, 32],
    [21, 23, 20, 24, 21, 25, 20, 22, 24, 22],
    [24, 22, 21, 20, 25, 24, 25, 23, 24, 23],
    [19, 21, 17, 23, 20, 21, 18, 16, 22, 15]
])

birds = np.array([
    [30, 31, 27, 25, 28, 30, 26, 29, 28, 32],
    [27, 22, 21, 20, 23, 24, 26, 21, 25, 20],
    [34, 32, 29, 35, 31, 28, 30, 32, 29, 33],
    [31, 33, 31, 35, 31, 34, 34, 30, 32, 32],
    [27, 25, 29, 30, 25, 28, 26, 24, 28, 30]
])

reptiles = np.array([
    [17, 13, 10, 16, 14, 15, 15, 11, 12, 13],
    [11, 10, 14, 13, 10, 12, 15, 11, 11, 10],
    [9, 12, 5, 13, 8, 6, 10, 11, 7, 10],
    [12, 13, 10, 15, 12, 13, 14, 14, 11, 10],
    [5, 8, 6, 5, 5, 7, 9, 7, 6, 8]
])

amphibians = np.array([
    [17, 19, 15, 14, 16, 16, 19, 20, 18, 17],
    [13, 10, 13, 15, 14, 12, 11, 10, 14, 11],
    [13, 10, 12, 10, 15, 11, 13, 11, 16, 14],
    [12, 11, 16, 14, 12, 10, 15, 14, 13, 10],
    [34, 33, 31, 31, 32, 33, 30, 35, 34, 32]
])

insects = np.array([
    [15, 16, 17, 16, 15, 15, 16, 16, 15, 16],
    [21, 20, 23, 22, 21, 21, 22, 21, 20, 21],
    [20, 30, 24, 22, 28, 18, 29, 23, 27, 24],
    [19, 20, 20, 20, 19, 19, 19, 20, 19, 19],
    [19, 11, 16, 14, 9, 12, 18, 16, 20, 13]
])

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

x_ticks = np.arange(len(habitats))
ax.set_xticks(x_ticks)
ax.set_xticklabels(habitats, rotation=45, ha='right', fontsize=10)

y_ticks = np.arange(len(years))
ax.set_yticks(y_ticks)
ax.set_yticklabels(years, fontsize=10)

ax.set_zlim(0, 100)
ax.set_zlabel('Biodiv (%)', fontsize=12)  # Shortened z-axis label

cmap = cm.get_cmap('Set3')
colors = [cmap(i) for i in range(len(habitats))]
bar_width = 0.4

species_data = [mammals, birds, reptiles, amphibians, insects]
species_names = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects']

for j, habitat in enumerate(habitats):
    bottom = np.zeros_like(years)
    for i, species in enumerate(species_data):
        x_pos = np.ones_like(years) * x_ticks[j]
        y_pos = years - years[0]
        z_pos = bottom
        dz = species[j]
        
        ax.bar3d(x_pos, y_pos, z_pos, bar_width, 1, dz, color=colors[i], alpha=0.8, label=species_names[i] if j == 0 else "")
        bottom += dz

ax.text(x_ticks[0], years[5] - years[0], bottom[5], 'Peak\nReptiles', color='black', fontsize=9)

plt.title("Biodiv Trends\nAcross Habitats (2030-39)", fontsize=14, pad=30, loc='left')  # Shortened title
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Groups', fontsize=10)  # Shortened legend title

ax.view_init(elev=20., azim=-35)

plt.tight_layout()

plt.show()