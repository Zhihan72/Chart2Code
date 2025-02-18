import matplotlib.pyplot as plt
import numpy as np

# Data with altered popularity scores, manually shuffled
games = ['Catan', 'Ticket', 'Pandemic', 'Carcassonne', 'Terraform']
popularity_2020 = [78, 88, 79, 83, 70]  # Shuffled values

# Sorting data by the new, altered popularity in 2020
sorted_indices = np.argsort(popularity_2020)[::-1]
sorted_games = [games[i] for i in sorted_indices]
sorted_popularity_2020 = [popularity_2020[i] for i in sorted_indices]

# Bar plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(sorted_games, sorted_popularity_2020, color='midnightblue', alpha=0.7)

ax.set_title("Game Pop. 2020", fontsize=16, fontweight='bold')
ax.set_xlabel("Score", fontsize=14)
ax.set_yticks(np.arange(len(games)))
ax.set_yticklabels(sorted_games, fontsize=12)

plt.tight_layout()
plt.show()