import numpy as np
import matplotlib.pyplot as plt

# Backstory: Comparing the Major Powers of Legendary Wizards from Different Realms
# Categories: Intelligence, Spell Power, Healing Ability, Defense Skill, Summoning Skill
categories = ['Intelligence', 'Spell Power', 'Healing Ability', 'Defense Skill', 'Summoning Skill']
num_vars = len(categories)

# Data for each wizard - Scores are out of 10
wizards = {
    'Merlin': [9, 10, 8, 7, 9],
    'Gandalf': [8, 9, 7, 8, 10],
    'Dumbledore': [10, 8, 9, 7, 8],
    'Morgana': [7, 9, 8, 10, 7],
    'Saruman': [8, 7, 9, 7, 9]
}

# Add the first score to the end to close the circle for the radar chart
for wizard in wizards:
    wizards[wizard] += wizards[wizard][:1]

# Calculate angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 9), subplot_kw={'polar': True})

# Radar chart for detailed comparison
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

ax.set_title("Comparing the Powers of Legendary Wizards\nFrom Different Realms", size=14, weight='bold')

# Bar chart for average scores
ax2 = axs[1]
average_scores = {wizard: np.mean(wizards[wizard][:-1]) for wizard in wizards}
ax2.bar(average_scores.keys(), average_scores.values(), color=colors)
ax2.set_ylim(0, 10)
ax2.set_title("Average Power Scores per Wizard", size=14, weight='bold')
ax2.set_ylabel('Average Score', size=12)
ax2.set_xticklabels(average_scores.keys(), rotation=45, ha='right', fontsize=12)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()