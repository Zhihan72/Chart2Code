import matplotlib.pyplot as plt
import numpy as np

# Backstory
# A fictional university is comparing the performance of its various sports teams over the past year.
# They want to see how many games each team played and how many they won, lost, or drew.

# Teams and their performance data
teams = ['Basketball', 'Soccer', 'Baseball', 'Swimming', 'Tennis']
games_played = [30, 28, 25, 20, 22]
won_games = [20, 18, 15, 10, 13]
lost_games = [8, 6, 7, 8, 6]
draw_games = [2, 4, 3, 2, 3]

# Positions on the x-axis
x = np.arange(len(teams))

# Bar width setting
bar_width = 0.2

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars
bars1 = ax.bar(x - bar_width, games_played, bar_width, label='Games Played', color='#ff9999', edgecolor='black')
bars2 = ax.bar(x, won_games, bar_width, label='Games Won', color='#66b3ff', edgecolor='black')
bars3 = ax.bar(x + bar_width, lost_games, bar_width, label='Games Lost', color='#99ff99', edgecolor='black')
bars4 = ax.bar(x + 2 * bar_width, draw_games, bar_width, label='Games Drawn', color='#ffcc99', edgecolor='black')

# Add titles and labels
ax.set_title('Annual Performance of University Sports Teams', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Teams', fontsize=12)
ax.set_ylabel('Number of Games', fontsize=12)

# Set y-ticks and x-ticks
ax.set_xticks(x)
ax.set_xticklabels(teams, fontsize=12)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add data labels on bars
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='black')

# Add the legend
ax.legend(loc='upper left', fontsize=12)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()