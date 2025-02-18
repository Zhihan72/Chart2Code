import matplotlib.pyplot as plt
import numpy as np

teams = ['Basketball', 'Soccer', 'Baseball', 'Swimming', 'Tennis']
games_played = [30, 28, 25, 20, 22]
won_games = [21, 17, 14, 13, 15]
lost_games = [7, 7, 8, 5, 5]
draw_games = [2, 4, 3, 2, 2]

# Sort the data based on games played in descending order
sorted_indices = np.argsort(games_played)[::-1]
teams = [teams[i] for i in sorted_indices]
games_played = [games_played[i] for i in sorted_indices]
won_games = [won_games[i] for i in sorted_indices]
lost_games = [lost_games[i] for i in sorted_indices]
draw_games = [draw_games[i] for i in sorted_indices]

x = np.arange(len(teams))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(12, 8))

# Applying a new set of colors
ax.bar(x - bar_width, games_played, bar_width, color='#e6194b', edgecolor='black', linestyle='-.')
ax.bar(x, won_games, bar_width, color='#3cb44b', edgecolor='black', hatch='/')
ax.bar(x + bar_width, lost_games, bar_width, color='#ffe119', edgecolor='black', linestyle=':')
ax.bar(x + 2 * bar_width, draw_games, bar_width, color='#4363d8', edgecolor='black', hatch='\\')

# Customized grid
ax.yaxis.grid(True, linestyle='-', linewidth=1.0, color='grey', alpha=0.5)
ax.legend(['Games Played', 'Won Games', 'Lost Games', 'Draw Games'], loc='upper right', title='Game Stats')

# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()