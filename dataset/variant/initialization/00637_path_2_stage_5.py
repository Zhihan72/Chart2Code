import matplotlib.pyplot as plt
import numpy as np

bodies = ['Mars', 'Europa', 'Titan', 'Ganymede', 'Callisto', 'Mercury', 'Venus', 'Phobos', 'Deimos', 'Enceladus']
distances = np.array([225, 628, 1221, 1070, 1182, 77, 42, 78, 76, 583])

# Randomly shuffled stylistic elements
markers = ['o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H']
line_styles = ['-', '--', '-.', ':']
colors = ['tomato', 'mediumseagreen', 'deepskyblue', 'orange', 'slateblue', 'darkorchid', 'gold', 'dodgerblue', 'crimson', 'lime']

# In this case, using one unique marker, line style and color pattern
fig, ax = plt.subplots(figsize=(14, 9))
ax.barh(bodies, distances, color=colors, edgecolor='black', linestyle=line_styles[0], linewidth=1.5)

# Adding randomly styled grid and borders
ax.grid(True, which='major', linestyle=line_styles[1], linewidth=0.7, alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_title('Distance to Celestial Bodies', fontsize=16, fontweight='bold')
ax.set_xlabel('Distance (Million km)', fontsize=12, fontstyle='italic')
ax.set_ylabel('Celestial Bodies', fontsize=12, rotation=0, labelpad=40)

# Adding randomized legend
legend_labels = ['Target' for _ in bodies]
ax.legend(legend_labels, loc='lower right', title='Legend', facecolor='whitesmoke')

plt.tight_layout()
plt.show()