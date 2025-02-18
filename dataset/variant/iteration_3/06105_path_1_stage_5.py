import numpy as np
import matplotlib.pyplot as plt

categories = ['Intelligence', 'Spell Power', 'Healing Ability', 'Defense Skill', 'Summoning Skill']
num_vars = len(categories)

wizards = {
    'Merlin': [10, 8, 7, 9, 9],
    'Gandalf': [9, 8, 10, 7, 8],
    'Dumbledore': [8, 9, 7, 8, 10],
    'Morgana': [10, 7, 9, 7, 8],
    'Saruman': [7, 9, 9, 7, 8]
}

for wizard in wizards:
    wizards[wizard] += wizards[wizard][:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, axs = plt.subplots(2, 1, figsize=(9, 18), subplot_kw={'polar': True})

# Radar chart
ax = axs[0]
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_yticks([])
single_color = 'royalblue'

for score in wizards.values():
    ax.fill(angles, score, color=single_color, alpha=0.3)

# Bar chart
ax2 = axs[1]
average_scores = {wizard: np.mean(wizards[wizard][:-1]) for wizard in wizards}
ax2.bar(average_scores.keys(), average_scores.values(), color=single_color)
ax2.set_ylim(0, 10)
ax2.set_xticklabels([])

plt.tight_layout()
plt.show()