import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

agencies = ['NASA', 'ESA', 'Roscosmos', 'ISRO']
years = ['2010', '2015', '2020']

success_rates = np.array([
    [85, 90, 95],  # NASA
    [75, 85, 88],  # ESA
    [80, 83, 89],  # Roscosmos
    [70, 78, 85]   # ISRO (made-up data)
])

xpos, ypos = np.meshgrid(np.arange(len(years)), np.arange(len(agencies)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = success_rates.flatten()

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['navy', 'royalblue', 'deepskyblue', 'dodgerblue']

for i, color in enumerate(colors):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i],
             dx=0.3, dy=0.3, dz=dz[ypos == i], color=color, alpha=0.7, label=agencies[i])

ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(agencies)))
ax.set_yticklabels(agencies, fontsize=10)
ax.set_zlim(0, 100)
ax.set_zlabel('Success %', fontsize=10)
ax.set_title("Space Mission Success (2010-2020)", fontsize=14, weight='bold', loc='center')
ax.view_init(elev=30, azim=220)
ax.xaxis.pane.set_visible(False)
ax.yaxis.pane.set_visible(False)
ax.zaxis.pane.set_edgecolor('gray')
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', which='both')
ax.legend(loc='upper left', bbox_to_anchor=(0.8, 0.9), title='Agencies', fontsize=10)

plt.tight_layout()
plt.show()