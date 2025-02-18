import matplotlib.pyplot as plt
import numpy as np

civilizations = ['Elves', 'Dwarves', 'Humans', 'Orcs']
attributes = ['Hunting', 'Gathering', 'Magic', 'Combat', 'Diplomacy', 'Technology']

elves = [7, 8, 10, 4, 9, 6]
dwarves = [5, 4, 6, 10, 8, 9]
humans = [6, 7, 5, 7, 10, 8]
orcs = [8, 3, 2, 10, 5, 4]

data = np.array([elves, dwarves, humans, orcs])

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]
data = np.concatenate((data, data[:, [0]]), axis=1)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

single_color = '#1f77b4'
for idx, label in enumerate(civilizations):
    ax.plot(angles, data[idx], linewidth=2, linestyle='solid', color=single_color)
    ax.fill(angles, data[idx], color=single_color, alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=13, fontweight='bold', color='darkslategray')

plt.tight_layout()
plt.show()