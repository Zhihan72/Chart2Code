import numpy as np
import matplotlib.pyplot as plt
from math import pi

parameters = ['Resolution', 'Battery Life', 'Processing Power', 'Camera Quality', 'Durability']
num_vars = len(parameters)

smartphones = {
    'Phone A': [8, 6, 9, 8, 7],
    'Phone B': [9, 7, 8, 6, 6],
    'Phone C': [7, 8, 6, 9, 9],
    'Phone D': [9, 8, 7, 6, 8]
}

def create_filled_radar_chart(ax, data, color):
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    data = data + data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([])

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['blue', 'green', 'red', 'purple']  # Different colors for each phone

for specs, color in zip(smartphones.values(), colors):
    create_filled_radar_chart(ax, specs, color)

plt.tight_layout()
plt.show()