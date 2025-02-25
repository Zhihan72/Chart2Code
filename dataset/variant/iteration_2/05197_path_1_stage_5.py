import matplotlib.pyplot as plt
import numpy as np

kingdoms = ['Avalon', 'Eldoria', 'Valoria', 'Drakonia', 'Mystica']
events = ['Jousting', 'Archery', 'Melee Combat', 'Strategy Games', 'Performance Arts']

victories = np.array([
    [10, 15, 5, 7, 12],
    [12, 8, 9, 10, 5],
    [7, 14, 11, 8, 6],
    [9, 12, 10, 6, 10],
    [11, 10, 8, 9, 7]
])

colors = ['#d62728', '#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']

fig, ax = plt.subplots(figsize=(15, 9))
bar_height = 0.15
indices = np.arange(len(events))

for i, kingdom in enumerate(kingdoms):
    ax.barh(indices + i * bar_height, victories[i], bar_height, color=colors[i])

ax.set_yticks(indices + bar_height * (len(kingdoms) - 1) / 2)
ax.set_yticklabels(events)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()