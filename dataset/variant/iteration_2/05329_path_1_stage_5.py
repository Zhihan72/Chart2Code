import matplotlib.pyplot as plt
import numpy as np

attributes = ['Technology', 'Magic', 'Combat', 'Diplomacy', 'Hunting', 'Gathering']
civilizations = ['Wizards', 'Goblins', 'Elves', 'Orcs', 'Humans', 'Dwarves']

elves = [7, 8, 10, 4, 9, 6]
dwarves = [5, 4, 6, 10, 8, 9]
humans = [6, 7, 5, 7, 10, 8]
orcs = [8, 3, 2, 10, 5, 4]
goblins = [6, 7, 3, 8, 4, 6]
wizards = [5, 6, 10, 3, 9, 8]

data = np.array([wizards, goblins, elves, orcs, humans, dwarves])

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

data = np.concatenate((data, data[:, [0]]), axis=1)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

colors = ['#9467bd', '#1f77b4', '#8c564b', '#2ca02c', '#d62728', '#ff7f0e']
for idx, (label, color) in enumerate(zip(civilizations, colors)):
    ax.fill(angles, data[idx], color=color, alpha=0.25, label=label)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=13, fontweight='bold', color='darkslategray')

plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.tight_layout()
plt.show()