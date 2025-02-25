import matplotlib.pyplot as plt
import numpy as np
from math import pi

colonies = ['Colony A', 'Colony B', 'Colony C', 'Colony D']
attributes = ['Physical', 'Mental', 'Social', 'Artistic', 'Relaxation']

data = [
    [7, 9, 8, 6, 8],  # Colony A
    [6, 8, 7, 7, 9],  # Colony B
    [9, 7, 8, 6, 7],  # Colony C
    [8, 8, 6, 7, 8]   # Colony D
]

data = np.array(data)
num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Shuffle colors manually
colors = ['#33a02c', '#ff7f00', '#1f78b4', '#e31a1c']

line_styles = ['dashdot', 'dotted', 'dashed', 'solid']
marker_styles = ['o', 'v', '^', 's']
fill_opacities = [0.4, 0.2, 0.3, 0.5]

for i, colony_data in enumerate(data):
    values = colony_data.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle=line_styles[i], marker=marker_styles[i], label=colonies[i], color=colors[i])
    ax.fill(angles, values, color=colors[i], alpha=fill_opacities[i])

plt.xticks(angles[:-1], attributes, color='black', size=10, fontweight='bold')
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="darkgrey", size=8, fontweight='bold')
plt.ylim(0, 10)

plt.title("Galactic Leisure Survey:\nColony Leisure Activities Evaluation", size=14, color='darkblue', pad=20)

plt.legend(loc='lower left', bbox_to_anchor=(-0.1, 0), title="Colonies", fontsize='small', title_fontsize='11')

ax.grid(color='lightgrey', linestyle='-', linewidth=1)

plt.gca().spines['polar'].set_visible(True)
plt.gca().spines['polar'].set_edgecolor('grey')

plt.tight_layout()
plt.show()