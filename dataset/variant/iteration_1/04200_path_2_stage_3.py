import matplotlib.pyplot as plt
import numpy as np

matches = np.array(['Match 1', 'Match 2', 'Match 3'])
player_a_runs = np.array([50, 75, 65])
player_b_runs = np.array([60, 80, 70])
player_c_runs = np.array([45, 55, 60])
background_score = [20, 20, 20]

fig, ax = plt.subplots(figsize=(10, 6))

# Altered stylistic elements
player_colors = ['crimson', 'seagreen', 'navy']
marker_styles = ['o', 'v', 's']  # circle, triangle down, square
border_styles = ['-', '--', ':']  # solid, dashed, dotted

# Use different colors, marker styles, and border styles for each player
ax.scatter(matches, player_a_runs, color=player_colors[0], marker=marker_styles[0], s=100, edgecolor='grey')
ax.scatter(matches, player_b_runs, color=player_colors[1], marker=marker_styles[1], s=100, edgecolor='grey')
ax.scatter(matches, player_c_runs, color=player_colors[2], marker=marker_styles[2], s=100, edgecolor='grey')

# Change background line style
ax.plot(matches, background_score, linestyle=border_styles[1], color='grey', linewidth=2)

avg_runs = np.mean([player_a_runs, player_b_runs, player_c_runs], axis=0)
# Alter legend appearance and marker for average runs
ax.scatter(matches, avg_runs, color='royalblue', marker='D', s=200, edgecolor='brown', alpha=0.5)

ax.set_xticks(matches)
ax.set_xticklabels(matches, rotation=45)

# Alter grid style
ax.grid(True, linestyle=border_styles[2], alpha=0.3)

# Adding legend with altered fonts and positions
ax.legend(['Background Score', 'Player A', 'Player B', 'Player C', 'Average'], loc='upper left', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()