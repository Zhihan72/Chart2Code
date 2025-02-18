import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

years = np.array(['2050', '2051', '2052', '2053', '2054'])
destinations = ['Moon', 'Mars', 'Orbital Hotels']

tourists_data = np.array([
    [20, 25, 30, 35, 40],
    [5, 10, 15, 22, 30],
    [15, 20, 28, 36, 45],
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Alter colors and marker styles
colors = ['#4daf4a', '#e41a1c', '#377eb8']
markers = ['o', '^', 's']

for dest_idx, destination in enumerate(destinations):
    x_pos = np.arange(len(years))
    y_pos = np.full_like(x_pos, dest_idx)
    z_pos = np.zeros_like(x_pos)
    
    dz = tourists_data[dest_idx]
    ax.bar3d(x_pos, y_pos, z_pos, dx=0.3, dy=0.3, dz=dz, 
             color=colors[dest_idx], edgecolor='grey', linewidth=0.5, 
             linestyle='--', alpha=0.7, label=destination)
    ax.scatter(x_pos, y_pos, z_pos + dz, color=colors[dest_idx], 
               marker=markers[dest_idx], s=30)

ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=-60, ha='left', fontsize=8)
ax.set_yticks(np.arange(len(destinations)))
ax.set_yticklabels(destinations, fontsize=10)
ax.set_xlabel('Year', labelpad=15)
ax.set_ylabel('Destination', labelpad=15)
ax.set_zlabel('Tourists (Thousands)', labelpad=15)

ax.set_title('Space Tourism: Rise of Interplanetary Travel (2050-2054)', pad=40, fontsize=16, weight='bold')
ax.legend(title='Destinations', loc='upper right', bbox_to_anchor=(0.9, 0.1), fontsize=9)

ax.grid(True, linestyle='-', color='lightgrey', linewidth=0.7)

ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()