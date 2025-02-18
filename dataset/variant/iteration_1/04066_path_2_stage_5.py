import numpy as np
import matplotlib.pyplot as plt
from math import pi

centers = ['Dragon', 'Tiger', 'Eagle', 'Panther', 'Wolf', 'Falcon', 'Shark']
parameters = ['Str', 'Agil', 'Def', 'Endur', 'Flex']

data = np.array([
    [90, 80, 85, 70, 95],
    [88, 75, 80, 85, 90],
    [85, 85, 90, 80, 82],
    [80, 90, 78, 70, 88],
    [95, 85, 80, 78, 92],
    [82, 78, 88, 85, 90],
    [88, 82, 80, 90, 85]
])

num_vars = len(parameters)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

def plot_center(data, color):
    values = data.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=color)
    ax.fill(angles, values, color=color, alpha=0.25)

colors = ['orange', 'purple', 'brown', 'pink', 'lime', 'cyan', 'magenta']

for idx, center_data in enumerate(data):
    plot_center(center_data, colors[idx])

plt.xticks(angles[:-1], parameters, color='grey', size=10)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
plt.ylim(0, 100)
plt.title('Martial Arts Center Eval', size=14, color='darkred', weight='bold', position=(0.5, 1.1))
plt.tight_layout()
plt.show()