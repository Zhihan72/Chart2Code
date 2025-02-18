import numpy as np
import matplotlib.pyplot as plt

categories = ['Intel', 'Spell', 'Healing', 'Defense', 'Summon']
num_vars = len(categories)

wizards = {
    'Merlin': [9, 10, 8, 7, 9],
    'Gandalf': [8, 9, 7, 8, 10],
    'Dumbledore': [10, 8, 9, 7, 8],
    'Morgana': [7, 9, 8, 10, 7],
    'Saruman': [8, 7, 9, 7, 9]
}

for wizard in wizards:
    wizards[wizard] += wizards[wizard][:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, axs = plt.subplots(2, 1, figsize=(12, 12), subplot_kw={'polar': True})

ax = axs[0]
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='navy', size=10)
ax.set_rlabel_position(0)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], color="darkred", size=8)
ax.set_ylim(0, 10)

colors = ['darkcyan', 'maroon', 'olive', 'teal', 'indigo']
markers = ['o', 's', 'd', '^', 'v']
linestyles = ['-', '--', '-.', ':', '-']

for i, (wizard, score) in enumerate(wizards.items()):
    ax.plot(angles, score, linewidth=1.5, linestyle=linestyles[i], label=wizard, color=colors[i], marker=markers[i])
    ax.fill(angles, score, color=colors[i], alpha=0.1)

ax.set_title("Powers of Wizards", size=16, weight='extra bold')
ax.grid(color='gray', linestyle='--', linewidth=0.5)

fig.delaxes(axs[1])
ax2 = fig.add_subplot(2, 1, 2)

average_scores = {wizard: np.mean(wizards[wizard][:-1]) for wizard in wizards}
ax2.barh(list(average_scores.keys()), list(average_scores.values()), color=colors, edgecolor='black', hatch='//')
ax2.set_xlim(0, 10)
ax2.set_title("Avg Scores", size=16, weight='bold')
ax2.set_xlabel('Avg Score', size=12)
ax2.set_yticklabels(average_scores.keys(), fontsize=10)

ax.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1), fontsize=9)

plt.tight_layout()
plt.show()