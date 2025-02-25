import matplotlib.pyplot as plt
import numpy as np

categories = ['Transmutation', 'Hex Casting', 'Elixir Mixing', 'Charming', 'Conjuring']
N = len(categories)

wizard_factions = {
    'Celestial Order': [7, 8, 6, 7, 9],
    'Secret Society': [5, 9, 6, 8, 6],
    'Sorcerer Alliance': [6, 7, 9, 9, 7],
    'Mystic Realm': [8, 8, 9, 6, 7]
}

data = {name: np.array(values + [values[0]]) for name, values in wizard_factions.items()}

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for (name, values), color in zip(data.items(), colors):
    ax.fill(angles, values, color=color, alpha=0.4)  # Ensure areas are filled

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_yticklabels([])
ax.set_ylim(0, 10)

plt.title('Magical Abilities by Faction', fontsize=16)

plt.show()