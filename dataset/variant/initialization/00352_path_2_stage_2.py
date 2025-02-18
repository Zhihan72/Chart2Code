import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

islands = ['Avalon', 'Eldoria', 'Lumina', 'Noxterra', 'Vespera']
elements = ['Mana', 'Ether', 'Elixir', 'Aura']

percentage_data = np.array([
    [30, 25, 20, 25],
    [20, 30, 35, 15],
    [25, 25, 30, 20],
    [15, 35, 25, 25],
    [35, 15, 20, 30]
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_pos, y_pos = np.meshgrid(np.arange(len(islands)), np.arange(len(elements)), indexing='ij')
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

width = 0.4
depth = 0.6

# Changed color scheme
colors = ['#FFA07A', '#20B2AA', '#9370DB', '#FF4500']

for i, color in enumerate(colors):
    ax.bar3d(x_pos[y_pos == i], y_pos[y_pos == i], z_pos[y_pos == i], 
             width, depth, percentage_data[:, i], 
             color=color, alpha=0.8)

ax.set_xlabel('Islands', fontsize=10, fontweight='bold', color='grey')
ax.set_ylabel('Magical Elements', fontsize=10, fontweight='bold', color='grey')
ax.set_zlabel('Abundance (%)', fontsize=10, fontweight='bold', color='grey')

ax.set_xticks(np.arange(len(islands)))
ax.set_xticklabels(islands, rotation=30, ha='right')
ax.set_yticks(np.arange(len(elements)))
ax.set_yticklabels(elements)

ax.set_title('Magical Element Distribution in Fantasia', fontsize=16, fontweight='bold', pad=30, color='navy')

ax.set_zlim(0, 40)

# Removed the legend since it wasn't configured properly without a handles/labels setup
# If needed, proper legend configurations should be added
# ax.legend(title="Elements", loc='best')

ax.grid(True, linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()