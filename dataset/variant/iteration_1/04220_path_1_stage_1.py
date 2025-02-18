import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Attack', 'Defense', 'Magic', 'Speed', 'Health']
num_vars = len(categories)

warrior = [8, 9, 2, 5, 10]
mage = [3, 4, 10, 6, 4]
rogue = [7, 5, 3, 10, 6]
ranger = [6, 6, 5, 8, 7]

data = [warrior, mage, rogue, ranger]
classes = ['Warrior', 'Mage', 'Rogue', 'Ranger']
colors = ['orange', 'cyan', 'olive', 'pink']

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create a function to plot radar charts with random stylistic changes
def plot_radar_chart(ax, data, color, label):
    data += data[:1]
    linestyle_options = ['dashed', 'dashdot', 'dotted']
    marker_options = ['o', 's', 'x', '^']
    
    ax.plot(angles, data, color=color, linewidth=1.5, linestyle=linestyle_options[0], marker=marker_options[0], label=label)
    ax.fill(angles, data, color=color, alpha=0.3)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for idx, class_data in enumerate(data):
    plot_radar_chart(ax, class_data, colors[idx], classes[idx])

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels([str(i) for i in range(2, 12, 2)], color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='black', weight='bold')

# Introduce stylistic changes to the grid and borders
ax.yaxis.grid(True, color='lightblue', linestyle='-')
ax.spines['polar'].set_visible(False)

plt.title('Attributes of RPG Classes\nA Comparative Study', size=14, weight='bold', pad=20)

# Add a legend with altered position and style
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=9, frameon=False)

plt.tight_layout()

plt.show()