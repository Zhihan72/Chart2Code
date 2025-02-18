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

# Changed order of colors
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:purple', 'tab:orange']

# Altering line styles and marker types
line_styles = ['-', '--', '-.', ':', '-']
marker_types = ['o', 's', '^', 'D', 'p']

for (discipline, ratings), color, line_style, marker in zip(arcane_discs_data.items(), colors, line_styles, marker_types):
    ratings += ratings[:1]
    ax.fill(angles, ratings, color=color, alpha=0.25)
    ax.plot(angles, ratings, color=color, linestyle=line_style, linewidth=2, marker=marker)

plt.xticks(angles[:-1], abilities, color='slateblue', size=12)
ax.set_ylim(0, 10)
plt.yticks(range(1, 10), map(str, range(1, 10)), color="slateblue", size=10)

plt.title('Comparative Analysis of Arcane Disciplines', size=18, color='darkgreen', pad=20)
# Moved legend position and removed its title
ax.legend(loc='upper right', fontsize=10)

# Turn on grid for clarity
ax.xaxis.grid(True, linestyle=':', linewidth=1)
ax.yaxis.grid(True, linestyle=':', linewidth=1)

# Changed border thickness and color
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_color('navy')
ax.spines['polar'].set_linewidth(1.5)

plt.tight_layout()
plt.show()