import numpy as np
import matplotlib.pyplot as plt

categories = ['Str', 'Spd', 'Int', 'End', 'Agi', 'Heal']
num_vars = len(categories)

team_abilities = {
    'Alpha': [85, 70, 95, 60, 75, 80],
    'Beta': [70, 60, 85, 80, 65, 90],
    'Gamma': [90, 85, 75, 70, 80, 60],
    'Delta': [95, 85, 70, 75, 90, 85],
    # Added new data series
    'Epsilon': [78, 88, 82, 90, 77, 85],
    'Zeta': [65, 95, 78, 82, 84, 79]
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for team, abilities in team_abilities.items():
    abilities += abilities[:1]
    ax.plot(angles, abilities, linewidth=2, marker='o')

plt.xticks(angles[:-1], categories, color='black', size=12)
ax.set_ylim(0, 100)
plt.yticks([20, 40, 60, 80, 100], [])

plt.title('Team Abilities', size=18, color='black', y=1.1, weight='bold')

plt.tight_layout()
plt.show()