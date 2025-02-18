import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

years = np.array(['50', '51', '52', '53', '54'])
destinations = ['Moon', 'Mars', 'Orbit']

tourists_data = np.array([
    [40, 20, 35, 30, 25], 
    [10, 15, 22, 30, 5],   
    [28, 36, 15, 20, 45], 
])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

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
ax.set_yticklabels(destinations, fontsize=9)
ax.set_xlabel('Yr', labelpad=10)
ax.set_ylabel('Dest', labelpad=10)
ax.set_zlabel('Tourists', labelpad=10)

ax.set_title('Space Tourism (2050-54)', pad=30, fontsize=14, weight='bold')
ax.legend(title='Sites', loc='upper right', bbox_to_anchor=(0.9, 0.1), fontsize=8)

ax.grid(True, linestyle='-', color='lightgrey', linewidth=0.7)

ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()