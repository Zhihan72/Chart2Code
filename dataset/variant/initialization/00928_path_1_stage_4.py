import matplotlib.pyplot as plt
import numpy as np

regions = ['Am', 'Eur', 'AP']
coffee_types = ['Esp', 'Lat', 'CB']

# Consumption and price data
consumption_data = np.array([
    [25, 55, 20],
    [40, 25, 35],
    [50, 20, 30]
])

price_data = np.array([
    [3.5, 4.0, 3.0],
    [3.2, 2.5, 3.0],
    [4.8, 4.0, 4.5]
])

fig = plt.figure(figsize=(14, 8))

ax1 = fig.add_subplot(121, projection='3d')
xpos, ypos = np.meshgrid(np.arange(len(regions)), np.arange(len(coffee_types)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = consumption_data.flatten()
dx = dy = 0.5

colors = ['#8B4513', '#DEB887', '#D2B48C']

# Drawing 3D bars
for i in range(len(coffee_types)):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i], 
              color=colors[i], alpha=0.7, label=coffee_types[i], zsort='average')

ax1.set_xlabel('Reg', fontsize=12, labelpad=8)
ax1.set_ylabel('Types', fontsize=12, labelpad=8)
ax1.set_zlabel('%', fontsize=12, labelpad=8)
ax1.set_xticks(np.arange(len(regions)))
ax1.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax1.set_yticks(np.arange(len(coffee_types)))
ax1.set_yticklabels(coffee_types, fontsize=10)
ax1.set_zlim(0, 100)
ax1.set_title('Coffee Cons\n2023', fontsize=14, weight='bold', pad=15)
ax1.legend(title='Types', loc='upper right', fontsize=9)

ax2 = fig.add_subplot(122)
bar_width = 0.2
indices = np.arange(len(regions))

ax2.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

for i, coffee_type in enumerate(coffee_types):
    ax2.bar(indices + i * bar_width, price_data[:, i], bar_width,
            label=coffee_type, color=colors[i], alpha=0.7)

ax2.set_xlabel('Reg', fontsize=12)
ax2.set_ylabel('Price ($)', fontsize=12)
ax2.set_title('Avg Coffee Price', fontsize=14, weight='bold')
ax2.set_xticks(indices + bar_width)
ax2.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax2.legend(title='Types', fontsize=9)

plt.tight_layout()
plt.show()