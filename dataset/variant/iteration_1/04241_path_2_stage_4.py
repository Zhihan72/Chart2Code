import matplotlib.pyplot as plt
import numpy as np

teams = ['Tennis', 'Soccer', 'Basketball', 'Swimming', 'Baseball']
games_played = [20, 22, 25, 28, 30]
won_games = [10, 13, 15, 18, 20]
draw_games = [2, 3, 3, 4, 2]

x = np.arange(len(teams))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(x - bar_width, games_played, bar_width, color='#ff9999')
ax.bar(x, won_games, bar_width, color='#66b3ff')
ax.bar(x + bar_width, draw_games, bar_width, color='#ffcc99')

ax.set_xticks(x)
ax.set_xticklabels(teams, fontsize=12)

# Randomly altered textual elements
ax.set_title('Achievements Comparison Chart', fontsize=14)
ax.set_xlabel('Sports Teams', fontsize=12)
ax.set_ylabel('Number of Matches', fontsize=12)

plt.tight_layout()
plt.show()