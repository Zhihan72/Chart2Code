import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Magic', 'Speed', 'Defense', 'Attack', 'Health']
num_vars = len(categories)

# Manually altered data values to introduce randomness while keeping the structure
warrior = [7, 8, 3, 6, 9]
mage = [4, 5, 9, 5, 5]
rogue = [6, 6, 2, 9, 7]
ranger = [5, 7, 4, 7, 8]

data = [warrior, mage, rogue, ranger]
classes = ['Ranger', 'Warrior', 'Mage', 'Rogue']
colors = ['cyan', 'pink', 'orange', 'olive']

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_fill_area_radar_chart(ax, data, color, label):
    data += data[:1]
    ax.fill(angles, data, color=color, alpha=0.3, label=label)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for idx, class_data in enumerate(data):
    plot_fill_area_radar_chart(ax, class_data, colors[idx], classes[idx])

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels([str(i) for i in range(2, 12, 2)], color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='black', weight='bold')

ax.yaxis.grid(True, color='lightblue', linestyle='-')
ax.spines['polar'].set_visible(False)

plt.title('RPG Class Stats:\nA Randomized Visualization', size=14, weight='bold', pad=20)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=9, frameon=False)

plt.tight_layout()

plt.show()