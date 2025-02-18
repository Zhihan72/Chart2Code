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

# Change subplot grid to 2 rows and 1 column
fig, axs = plt.subplots(2, 1, figsize=(12, 12), subplot_kw={'polar': True} if len(axs) > 1 else {})

ax = axs[0]
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='grey', size=12)
ax.set_rlabel_position(0)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], color="grey", size=10)
ax.set_ylim(0, 10)

colors = ['crimson', 'royalblue', 'forestgreen', 'darkorange', 'purple']

for i, (wizard, score) in enumerate(wizards.items()):
    ax.plot(angles, score, linewidth=2, linestyle='solid', label=wizard, color=colors[i])
    ax.fill(angles, score, color=colors[i], alpha=0.1)

ax.set_title("Powers of Wizards", size=14, weight='bold')

# Convert the second subplot to a standard plot
fig.delaxes(axs[1])
ax2 = fig.add_subplot(2, 1, 2)

average_scores = {wizard: np.mean(wizards[wizard][:-1]) for wizard in wizards}
ax2.bar(average_scores.keys(), average_scores.values(), color=colors)
ax2.set_ylim(0, 10)
ax2.set_title("Avg Scores", size=14, weight='bold')
ax2.set_ylabel('Avg Score', size=12)
ax2.set_xticklabels(average_scores.keys(), rotation=45, ha='right', fontsize=12)

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

plt.tight_layout()
plt.show()