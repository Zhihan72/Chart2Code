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

def create_radar_chart(ax, data, categories, color):
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    data = data + data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, fontweight='bold')

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = {
    'Phone A': 'blue', 
    'Phone B': 'green', 
    'Phone C': 'red', 
    'Phone D': 'purple'
}

for phone, specs in smartphones.items():
    create_radar_chart(ax, specs, parameters, colors[phone])

ax.set_title("Smartphone Comparison on Key Specifications", fontsize=14, fontweight='bold', pad=30)
plt.tight_layout()
plt.show()