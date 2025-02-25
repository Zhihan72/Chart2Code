import matplotlib.pyplot as plt
import numpy as np

# Define the civilizations and their corresponding skills' values
civilizations = ['Elves', 'Dwarves', 'Humans', 'Orcs', 'Goblins', 'Wizards']
attributes = ['Hunting', 'Gathering', 'Magic', 'Combat', 'Diplomacy', 'Technology']

elves = [7, 8, 10, 4, 9, 6]
dwarves = [5, 4, 6, 10, 8, 9]
humans = [6, 7, 5, 7, 10, 8]
orcs = [8, 3, 2, 10, 5, 4]
goblins = [6, 7, 3, 8, 4, 6]
wizards = [5, 6, 10, 3, 9, 8]

data = np.array([elves, dwarves, humans, orcs, goblins, wizards])

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

data = np.concatenate((data, data[:, [0]]), axis=1)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
plt.title('Survival Skills of Fantasy Civilizations', size=18, weight='bold', pad=20, color='peru')

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
for idx, (label, color) in enumerate(zip(civilizations, colors)):
    ax.plot(angles, data[idx], linewidth=2, linestyle='solid', label=label, color=color)
    ax.fill(angles, data[idx], color=color, alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=13, fontweight='bold', color='darkslategray')

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, title='Civilizations')

plt.tight_layout()
plt.show()