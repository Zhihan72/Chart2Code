import numpy as np
import matplotlib.pyplot as plt

categories = ['Endurance', 'Agility', 'Healing', 'Strength', 'Speed', 'Intelligence']
num_vars = len(categories)

team_abilities = {
    'Beta Squad': [70, 60, 85, 80, 65, 90],
    'Alpha Force': [85, 70, 95, 60, 75, 80],
    'Gamma Group': [90, 85, 75, 70, 80, 60],
    'Delta Unit': [95, 85, 70, 75, 90, 85],
    'Omega Crew': [80, 75, 85, 90, 60, 85],
    'Epsilon League': [65, 80, 70, 75, 85, 95]
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2']

for idx, (team, abilities) in enumerate(team_abilities.items()):
    abilities += abilities[:1]
    ax.plot(angles, abilities, color=colors[idx], linewidth=2, marker='o')

plt.xticks(angles[:-1], categories, color='navy', size=12)
ax.set_ylim(0, 100)

plt.title('Heroic Team Skills Chart\nDiverse Units Assessment', size=18, color='darkred', y=1.1, weight='bold')

plt.tight_layout()
plt.show()