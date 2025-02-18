import matplotlib.pyplot as plt
import numpy as np
from math import pi

colonies = ['Colony A', 'Colony B', 'Colony C']
attributes = ['Physical', 'Mental', 'Social', 'Artistic', 'Relaxation']

data = [
    [7, 9, 8, 6, 8],  # Colony A
    [6, 8, 7, 7, 9],  # Colony B
    [9, 7, 8, 6, 7]   # Colony C
]

data = np.array(data)

num_attributes = len(attributes)

angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# New set of colors
colors = ['#ff7f0e', '#2ca02c', '#d62728']  # Changed colors

for i, colony_data in enumerate(data):
    values = colony_data.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=colonies[i], color=colors[i])
    ax.fill(angles, values, color=colors[i], alpha=0.25)

plt.xticks(angles[:-1], attributes, color='grey', size=10, fontweight='bold')

ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8, fontweight='bold')
plt.ylim(0, 10)

plt.title("Galactic Leisure Survey:\nColony Leisure Activities Evaluation", size=14, color='navy', pad=20)

plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Colonies", fontsize='medium', title_fontsize='13')

plt.tight_layout()
plt.show()