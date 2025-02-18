import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Atk', 'Def', 'Mgc', 'Spd', 'HP']
num_vars = len(categories)

warrior = [8, 9, 2, 5, 10]
mage = [3, 4, 10, 6, 4]
rogue = [7, 5, 3, 10, 6]
ranger = [6, 6, 5, 8, 7]

data = [warrior, mage, rogue, ranger]
colors = ['red', 'blue', 'green', 'purple']

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar_chart(ax, data, color):
    data += data[:1]
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, data, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for idx, class_data in enumerate(data):
    plot_radar_chart(ax, class_data, colors[idx])

ax.set_yticks([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='black', weight='bold')

plt.tight_layout()
plt.show()