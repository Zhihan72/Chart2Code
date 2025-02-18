import numpy as np
import matplotlib.pyplot as plt

categories = ['Intelligence', 'Spell Power', 'Healing Ability', 'Defense Skill', 'Summoning Skill']
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

# Create figure with subplots in 2 rows and 1 column
fig, axs = plt.subplots(2, 1, figsize=(9, 18), subplot_kw={'polar': True})

# Radar chart
ax = axs[0]
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks([])  # Remove the axis labels
ax.set_yticks([])  # Remove the radial ticks 

colors = ['crimson', 'royalblue', 'forestgreen', 'darkorange', 'purple']

for i, (wizard, score) in enumerate(wizards.items()):
    ax.plot(angles, score, linewidth=2, linestyle='solid', color=colors[i])
    ax.fill(angles, score, color=colors[i], alpha=0.1)

# Bar chart
ax2 = axs[1]
average_scores = {wizard: np.mean(wizards[wizard][:-1]) for wizard in wizards}
ax2.bar(average_scores.keys(), average_scores.values(), color=colors)
ax2.set_ylim(0, 10)

# Remove x tick labels
ax2.set_xticklabels([])

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()