import matplotlib.pyplot as plt
import numpy as np

kingdoms = ['Avalon', 'Eldoria', 'Valoria', 'Drakonia']
events = ['Jousting', 'Archery', 'Melee Combat', 'Strategy Games', 'Performance Arts']

victories = np.array([
    [10, 15, 5, 7, 12],
    [12, 8, 9, 10, 5],
    [7, 14, 11, 8, 6],
    [9, 12, 10, 6, 10]
])

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig, ax = plt.subplots(figsize=(15, 9))

bar_height = 0.2

indices = np.arange(len(events))

for i, kingdom in enumerate(kingdoms):
    ax.barh(indices + i * bar_height, victories[i], bar_height, color=colors[i], label=kingdom)

ax.set_yticks(indices + bar_height * (len(kingdoms)-1) / 2)
ax.set_yticklabels(events)

ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()

plt.tight_layout()

plt.show()