import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

categories = ['Intellect', 'Physical', 'Emotional', 'Spiritual', 'Social']
aries = [8, 7, 5, 6, 7]
taurus = [6, 6, 8, 7, 7]
gemini = [9, 6, 5, 6, 8]
cancer = [5, 5, 9, 6, 8]
leo = [7, 8, 6, 5, 8]

zodiac_data = np.array([aries, taurus, gemini, cancer, leo])

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar(ax, data, colors):
    for idx, d in enumerate(data):
        values = d.tolist()
        values += values[:1]
        ax.plot(angles, values, color=colors[idx], linewidth=2)
        ax.fill(angles, values, color=colors[idx], alpha=0.25)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#ff5733', '#4CAF50', '#2196F3', '#FFC107', '#9C27B0']
plot_radar(ax, zodiac_data, colors)

plt.xticks(angles[:-1], categories, color='dimgray', size=10)

ax.set_yticklabels([])
ax.set_ylim(0, 10)
for y in range(2, 11, 2):
    ax.add_patch(Circle((0,0), y, transform=ax.transData._b, color='lightgrey', alpha=0.2, zorder=0))

plt.tight_layout()
plt.show()