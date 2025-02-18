import numpy as np
import matplotlib.pyplot as plt

categories = ['Endurance', 'Agility', 'Healing', 'Strength', 'Speed', 'Intelligence']  # Randomly altered categories
num_vars = len(categories)

team_abilities = {
    'Beta Squad': [70, 60, 85, 80, 65, 90],  # Renamed team
    'Alpha Force': [85, 70, 95, 60, 75, 80],  # Renamed team
    'Gamma Group': [90, 85, 75, 70, 80, 60],  # Renamed team
    'Delta Unit': [95, 85, 70, 75, 90, 85],  # Renamed team
    'Omega Crew': [80, 75, 85, 90, 60, 85],  # Renamed team
    'Epsilon League': [65, 80, 70, 75, 85, 95]  # Renamed team
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2']

for idx, (team, abilities) in enumerate(team_abilities.items()):
    abilities += abilities[:1]
    ax.plot(angles, abilities, color=colors[idx], linewidth=2, marker='o', label=team)

plt.xticks(angles[:-1], categories, color='navy', size=12)
ax.set_ylim(0, 100)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=10)

plt.title('Heroic Team Skills Chart\nDiverse Units Assessment', size=18, color='darkred', y=1.1, weight='bold')  # Altered title
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11, title='Hero Teams')  # Altered legend title

plt.tight_layout()
plt.show()