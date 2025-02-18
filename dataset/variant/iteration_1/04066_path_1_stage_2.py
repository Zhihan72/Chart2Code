import numpy as np
import matplotlib.pyplot as plt
from math import pi

centers = ['DragonForce', 'TigerClaw', 'EagleStrike', 'PantherHeart', 'WolfPack', 'PhoenixFlame']
parameters = ['Strength Training', 'Agility Training', 'Self-defense', 'Endurance', 'Flexibility']

data = np.array([
    [90, 80, 85, 70, 95],
    [88, 75, 80, 85, 90],
    [85, 85, 90, 80, 82],
    [80, 90, 78, 70, 88],
    [95, 85, 80, 78, 92],
    [82, 88, 87, 76, 90]
])

num_vars = len(parameters)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

def plot_center(data, color, label):
    values = data.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1.5, linestyle='dashdot', color=color, marker='o', label=label)
    ax.fill(angles, values, color=color, alpha=0.1)

colors = ['r', 'c', 'm', 'k', 'b', 'y']

for idx, center_data in enumerate(data):
    plot_center(center_data, colors[idx], centers[idx])

plt.xticks(angles[:-1], parameters, color='orange', size=9, fontweight='heavy')

plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="green", size=7, fontstyle='italic')
plt.ylim(0, 100)

plt.title('Training Centers Evaluation', size=16, color='navy', weight='light', position=(0.5, 1.1))

plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.05), title='Centers', fancybox=True)

ax.spines['polar'].set_visible(False)

plt.tight_layout()
plt.show()