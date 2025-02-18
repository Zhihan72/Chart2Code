import matplotlib.pyplot as plt
import numpy as np

teams = ['Swimming', 'Tennis', 'Baseball', 'Soccer', 'Basketball']
games_played = [20, 22, 25, 28, 30]
won_games = [10, 13, 15, 18, 20]
lost_games = [8, 6, 7, 6, 8]
draw_games = [2, 3, 3, 4, 2]

x = np.arange(len(teams))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars without stylistic borders
ax.bar(x - bar_width, games_played, bar_width, color='#ff9999')
ax.bar(x, won_games, bar_width, color='#66b3ff')
ax.bar(x + bar_width, lost_games, bar_width, color='#99ff99')
ax.bar(x + 2 * bar_width, draw_games, bar_width, color='#ffcc99')

# Remove titles, labels, and grid
ax.set_xticks(x)
ax.set_xticklabels(teams, fontsize=12)

plt.tight_layout()
plt.show()