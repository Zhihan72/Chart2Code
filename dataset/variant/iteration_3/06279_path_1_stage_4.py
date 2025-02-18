import matplotlib.pyplot as plt
import numpy as np

categories = ['Storyline', 'Graphics', 'Audio', 'Replay Value', 'Difficulty', 'Controls', 'Community']
action_game = [8, 9, 7, 6, 8, 9, 7]
adventure_game = [9, 8, 9, 7, 5, 8, 8]
role_playing_game = [10, 8, 8, 9, 7, 8, 9]
sports_game = [6, 7, 8, 8, 6, 7, 5]

action_game += action_game[:1]
adventure_game += adventure_game[:1]
role_playing_game += role_playing_game[:1]
sports_game += sports_game[:1]

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
plt.ylim(0, 11)

genres = {
    'Action': ('#1f77b4', 'solid', 'o'),
    'Adventure': ('#ff7f0e', '--', '^'),
    'Role-Playing': ('#2ca02c', 'dashdot', 's'),
    'Sports': ('#9467bd', (0, (3, 1, 1, 1)), 'P')
}

datasets = [action_game, adventure_game, role_playing_game, sports_game]

for data, (color, linestyle, marker) in zip(datasets, genres.values()):
    ax.plot(angles, data, color=color, linewidth=2, linestyle=linestyle, marker=marker, markersize=6)
    ax.fill(angles, data, color=color, alpha=0.4)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, ha='center')
ax.set_yticklabels([])
ax.set_yticks([])
ax.spines['polar'].set_visible(False)
ax.grid(False)
plt.tight_layout()
plt.show()