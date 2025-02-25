import matplotlib.pyplot as plt
import numpy as np

categories = ['Alchemy', 'Spell Casting', 'Potion Brewing', 'Enchanting', 'Summoning']
N = len(categories)

wizard_factions = {
    'Elemental Guild': [8, 7, 6, 9, 7],
    'Mystic Union': [6, 9, 5, 8, 6],
    'Arcane Brotherhood': [7, 6, 9, 7, 9],
    'Ethereal Domain': [9, 8, 7, 6, 8]
}

data = {name: np.array(values + [values[0]]) for name, values in wizard_factions.items()}
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# New colors for each faction
new_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for (name, values), color in zip(data.items(), new_colors):
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_ylim(0, 10)

plt.tight_layout()
plt.show()