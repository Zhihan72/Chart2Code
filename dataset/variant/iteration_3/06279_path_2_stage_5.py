import matplotlib.pyplot as plt
import numpy as np

categories = ['Story', 'Graph', 'Audio', 'Replay', 'Diff.', 'Ctrls', 'Comm.']
action_game = [8, 9, 7, 6, 8, 9, 7]
adventure_game = [9, 8, 9, 7, 5, 8, 8]
role_playing_game = [10, 8, 8, 9, 7, 8, 9]
sports_game = [6, 7, 8, 8, 6, 7, 5]

# Close the loop for each dataset
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
    'Act': '#ff7f0e',
    'Adv': '#2ca02c',
    'RPG': '#d62728',
    'SPT': '#1f77b4'
}

datasets = [action_game, adventure_game, role_playing_game, sports_game]

# Ensure each area within the radar chart is filled
for data, color in zip(datasets, genres.values()):
    ax.plot(angles, data, color=color, linewidth=1)
    ax.fill(angles, data, color=color, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='black', size=11)
ax.set_yticklabels([])

plt.tight_layout()
plt.show()