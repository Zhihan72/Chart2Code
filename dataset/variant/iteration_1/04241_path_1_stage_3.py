import matplotlib.pyplot as plt
import numpy as np

# Teams and their performance data
teams = ['Basketball', 'Soccer', 'Baseball', 'Swimming', 'Tennis']
games_played = [30, 28, 25, 20, 22]
won_games = [21, 17, 14, 13, 15]  # Altered won games values
lost_games = [7, 7, 8, 5, 5]      # Altered lost games values
draw_games = [2, 4, 3, 2, 2]      # Altered draw games values

# Sort the data based on games played in descending order
sorted_indices = np.argsort(games_played)[::-1]
teams = [teams[i] for i in sorted_indices]
games_played = [games_played[i] for i in sorted_indices]
won_games = [won_games[i] for i in sorted_indices]
lost_games = [lost_games[i] for i in sorted_indices]
draw_games = [draw_games[i] for i in sorted_indices]

# Positions on the x-axis
x = np.arange(len(teams))

# Bar width setting
bar_width = 0.2

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars
ax.bar(x - bar_width, games_played, bar_width, color='#ff9999', edgecolor='black')
ax.bar(x, won_games, bar_width, color='#66b3ff', edgecolor='black')
ax.bar(x + bar_width, lost_games, bar_width, color='#99ff99', edgecolor='black')
ax.bar(x + 2 * bar_width, draw_games, bar_width, color='#ffcc99', edgecolor='black')

# Enable grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()