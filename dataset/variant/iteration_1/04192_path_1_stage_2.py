import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

settlers_of_catan = [60, 65, 68, 70, 75, 77, 76, 80, 83, 85, 88]
ticket_to_ride = [55, 58, 60, 63, 66, 70, 72, 75, 78, 80, 83]
pandemic = [45, 50, 55, 57, 60, 62, 65, 68, 70, 75, 78]
carcassonne = [50, 53, 55, 60, 63, 65, 70, 72, 74, 76, 79]
terraforming_mars = [10, 15, 20, 25, 30, 35, 40, 47, 55, 62, 70]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, settlers_of_catan, label='Settlers of Catan', color='royalblue', linestyle='-.', marker='o')
ax.plot(years, ticket_to_ride, label='Ticket to Ride', color='darkorange', linestyle='-', marker='x')
ax.plot(years, pandemic, label='Pandemic', color='forestgreen', linestyle='--', marker='s')
ax.plot(years, carcassonne, label='Carcassonne', color='purple', linestyle=':', marker='d')
ax.plot(years, terraforming_mars, label='Terraforming Mars', color='crimson', linestyle='-', marker='^')

board_games = ['Settlers of Catan', 'Ticket to Ride', 'Pandemic', 'Carcassonne', 'Terraforming Mars']
popularity_2010 = [60, 55, 45, 50, 10]
popularity_2020 = [88, 83, 78, 79, 70]
x = np.arange(len(board_games))
width = 0.35

ax_bar = ax.twinx()
ax_bar.barh(x - width/2, popularity_2010, width, label='2010', color='slategray', alpha=0.5)
ax_bar.barh(x + width/2, popularity_2020, width, label='2020', color='midnightblue', alpha=0.5)

ax.set_title("Board Game Popularity Trends from 2010 to 2020", fontsize=16, pad=20, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Popularity Score", fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))
ax.legend(loc='lower right', fontsize=12, frameon=False)

ax_bar.set_yticks(x)
ax_bar.set_yticklabels(board_games, fontsize=12)
ax_bar.set_xlabel("Popularity Score", fontsize=14)
ax_bar.legend(loc='upper right', fontsize=12, frameon=False)

ax.grid(True, linestyle='-', linewidth=0.5, color='gray', alpha=0.4)

plt.tight_layout(rect=[0, 0, 0.9, 1])

plt.show()