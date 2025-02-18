import matplotlib.pyplot as plt
import numpy as np

# Initial data
board_games = ['Settlers of Catan', 'Ticket to Ride', 'Pandemic', 'Carcassonne', 'Terraforming Mars']
popularity_2010 = [60, 55, 45, 50, 10]
popularity_2020 = [88, 83, 78, 79, 70]

# Sorting the data by popularity in 2020
sorted_indices = np.argsort(popularity_2020)[::-1]
sorted_board_games = [board_games[i] for i in sorted_indices]
sorted_popularity_2020 = [popularity_2020[i] for i in sorted_indices]

# Create a bar plot with sorted data
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(sorted_board_games, sorted_popularity_2020, color='midnightblue', alpha=0.7)

ax.set_title("Board Game Popularity in 2020", fontsize=16, fontweight='bold')
ax.set_xlabel("Popularity Score", fontsize=14)
ax.set_yticks(np.arange(len(board_games)))
ax.set_yticklabels(sorted_board_games, fontsize=12)

plt.tight_layout()
plt.show()