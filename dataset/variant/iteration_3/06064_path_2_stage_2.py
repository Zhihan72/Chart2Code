import numpy as np
import matplotlib.pyplot as plt

categories = ['Strength', 'Speed', 'Intelligence', 'Endurance', 'Agility', 'Healing']
num_vars = len(categories)

team_abilities = {
    'Team Alpha': [85, 70, 95, 60, 75, 80],
    'Team Beta': [70, 60, 85, 80, 65, 90],
    'Team Gamma': [90, 85, 75, 70, 80, 60],
    'Team Delta': [95, 85, 70, 75, 90, 85]
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

custom_colors = ['magenta', 'cyan', 'lime', 'orange']

for (team, abilities), color in zip(team_abilities.items(), custom_colors):
    abilities += abilities[:1]
    ax.plot(angles, abilities, color=color, linewidth=2, marker='o', label=team)

plt.xticks(angles[:-1], categories, color='navy', size=12)
ax.set_ylim(0, 100)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=10)

plt.title('Superhero Team Comparison\nBased on Abilities', size=18, color='darkred', y=1.1, weight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11, title='Teams')

plt.tight_layout()
plt.show()