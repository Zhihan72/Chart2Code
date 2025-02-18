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

bar_width = 0.2

indices = np.arange(len(events))

for i, kingdom in enumerate(kingdoms):
    ax.bar(indices + i * bar_width, victories[i], bar_width, color=colors[i])

ax.set_xticks(indices + bar_width * (len(kingdoms)-1) / 2)
ax.set_xticklabels([])

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

plt.show()