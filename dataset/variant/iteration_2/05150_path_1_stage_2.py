import numpy as np
import matplotlib.pyplot as plt

abilities = ['Spell Power', 'Mana Efficiency', 'Versatility', 'Ritual Complexity', 'Defense', 'Mobility']
num_vars = len(abilities)

arcane_discs_data = {
    'Elemental Magic': [8, 7, 6, 5, 8, 7],
    'Necromancy': [6, 5, 7, 8, 8, 4],
    'Divination': [7, 8, 5, 3, 6, 5],
    'Enchantments': [8, 6, 9, 7, 5, 6],
    'Illusions': [6, 7, 7, 4, 6, 9]
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = ['blue', 'red', 'green', 'purple', 'orange']
for idx, (discipline, ratings) in enumerate(arcane_discs_data.items()):
    ratings += ratings[:1]
    ax.fill(angles, ratings, alpha=0.25, color=colors[idx])
    ax.plot(angles, ratings, linewidth=2, color=colors[idx])

plt.xticks(angles[:-1], abilities, color='slategray', size=12)
ax.set_ylim(0, 10)
plt.yticks(range(1, 10), map(str, range(1, 10)), color="slategray", size=10)

plt.title('Comparative Analysis of Arcane Disciplines', size=18, color='indigo', pad=20)

plt.tight_layout()
plt.show()