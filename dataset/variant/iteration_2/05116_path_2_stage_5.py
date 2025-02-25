import matplotlib.pyplot as plt
import numpy as np

categories = ['Alchemy', 'Spell Casting', 'Potion Brewing', 'Enchanting', 'Summoning']
N = len(categories)

wizard_factions = {
    'Elemental Guild': [6, 9, 7, 7, 8],
    'Mystic Union': [9, 6, 6, 8, 5],
    'Arcane Brotherhood': [9, 7, 6, 9, 7],
    'Ethereal Domain': [8, 6, 8, 7, 9]
}

data = {name: np.array(values + [values[0]]) for name, values in wizard_factions.items()}
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

new_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Random stylistic alterations
marker_styles = ['o', 's', 'd', '^']  # Different marker shapes
line_styles = ['-', '--', '-.', ':']  # Various line styles

for (name, values), color, marker, line in zip(data.items(), new_colors, marker_styles, line_styles):
    ax.fill(angles, values, color=color, alpha=0.3)  # Adjusted alpha
    ax.plot(angles, values, color=color, linewidth=2, linestyle=line, marker=marker)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='#333')
ax.set_yticklabels([])
ax.set_ylim(0, 10)

# Randomly altering grid and border
ax.grid(True, linestyle='--', color='#ccc', linewidth=1.5)  # Custom grid style
ax.spines['polar'].set_visible(False)  # Hide the border line

# Randomized legend with no frame
ax.legend(wizard_factions.keys(), loc='upper right', bbox_to_anchor=(1.1, 1.1), frameon=False)

plt.tight_layout()
plt.show()