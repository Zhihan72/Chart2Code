import numpy as np
import matplotlib.pyplot as plt
from math import pi

centers = ['WolfPack', 'PantherHeart', 'PhoenixFlame', 'DragonForce', 'EagleStrike', 'TigerClaw']
parameters = ['Flexibility', 'Self-defense', 'Strength Training', 'Agility Training', 'Endurance']

data = np.array([
    [95, 70, 90, 80, 95],
    [82, 70, 88, 75, 90],
    [85, 80, 85, 85, 82],
    [90, 90, 80, 85, 88],
    [80, 70, 85, 85, 92],
    [88, 76, 82, 88, 90]
])

num_vars = len(parameters)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

def plot_center(data, color, label):
    values = data.tolist()
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.25, label=label)

colors = ['c', 'm', 'k', 'r', 'b', 'y']

for idx, center_data in enumerate(data):
    plot_center(center_data, colors[idx], centers[idx])

plt.xticks(angles[:-1], parameters, color='red', size=9, fontweight='heavy')

plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="blue", size=7, fontstyle='italic')
plt.ylim(0, 100)

plt.title('Centers Performance Check', size=16, color='purple', weight='light', position=(0.5, 1.1))

plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.05), title='Centers Evaluated', fancybox=False)

ax.spines['polar'].set_visible(False)

plt.tight_layout()
plt.show()