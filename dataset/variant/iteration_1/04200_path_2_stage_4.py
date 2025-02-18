import matplotlib.pyplot as plt
import numpy as np

matches = np.array(['Match 1', 'Match 2', 'Match 3'])
player_a_runs = np.array([50, 75, 65])
player_b_runs = np.array([60, 80, 70])
background_score = [20, 20, 20]

fig, ax = plt.subplots(figsize=(10, 6))

player_colors = ['crimson', 'seagreen']
marker_styles = ['o', 'v']  # circle, triangle down
border_styles = ['-', '--', ':']  # solid, dashed, dotted

ax.scatter(matches, player_a_runs, color=player_colors[0], marker=marker_styles[0], s=100, edgecolor='grey')
ax.scatter(matches, player_b_runs, color=player_colors[1], marker=marker_styles[1], s=100, edgecolor='grey')

ax.plot(matches, background_score, linestyle=border_styles[1], color='grey', linewidth=2)

avg_runs = np.mean([player_a_runs, player_b_runs], axis=0)
ax.scatter(matches, avg_runs, color='royalblue', marker='D', s=200, edgecolor='brown', alpha=0.5)

ax.set_xticks(matches)
ax.set_xticklabels(matches, rotation=45)

ax.grid(True, linestyle=border_styles[2], alpha=0.3)

ax.legend(['Background Score', 'Player A', 'Player B', 'Average'], loc='upper left', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()