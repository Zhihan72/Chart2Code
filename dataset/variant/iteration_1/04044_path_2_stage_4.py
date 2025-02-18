import numpy as np
import matplotlib.pyplot as plt
from math import pi

parameters = ['Res', 'Batt', 'Proc', 'Cam', 'Dur']
num_vars = len(parameters)

smartphones = {
    'A': [8, 7, 9, 8, 6],
    'B': [7, 6, 9, 6, 8],
    'C': [9, 8, 7, 9, 7],
    'D': [6, 8, 8, 7, 9]
}

colors = ['blue', 'green', 'red', 'purple']

def create_filled_radar_chart(ax, data, categories, color):
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, fontweight='bold')

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for phone, specs in zip(smartphones.keys(), smartphones.values()):
    create_filled_radar_chart(ax, specs, parameters, colors.pop(0))

ax.set_title("Phone Spec Comparison", fontsize=14, fontweight='bold', pad=30)
ax.spines['polar'].set_visible(False)
plt.show()