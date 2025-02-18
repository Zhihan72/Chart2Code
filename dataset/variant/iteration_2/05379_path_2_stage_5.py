import matplotlib.pyplot as plt
import numpy as np
from math import pi

colonies = ['Colony A', 'Colony B', 'Colony C', 'Colony D']
attributes = ['Physical', 'Mental', 'Social', 'Artistic', 'Relaxation']

# Manually altered data, mixing some values between colonies while keeping the same structure.
data = [
    [6, 8, 7, 8, 9],  # Colony A (originally Colony B's order)
    [8, 7, 6, 9, 7],  # Colony B (originally Colony D's order)
    [9, 9, 8, 6, 7],  # Colony C (originally Colony C's order but with increased Mental)
    [7, 7, 8, 6, 8]   # Colony D (originally Colony A's order)
]

data = np.array(data)
num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#33a02c', '#ff7f00', '#1f78b4', '#e31a1c']
fill_opacities = [0.4, 0.2, 0.3, 0.5]

for i, colony_data in enumerate(data):
    values = colony_data.tolist()
    values += values[:1]
    ax.fill(angles, values, color=colors[i], alpha=fill_opacities[i])

ax.set_yticklabels([])
ax.set_xticklabels([])

ax.grid(color='lightgrey', linestyle='-', linewidth=1)

plt.gca().spines['polar'].set_visible(True)
plt.gca().spines['polar'].set_edgecolor('grey')

plt.tight_layout()
plt.show()