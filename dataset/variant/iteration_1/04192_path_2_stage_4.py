import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

settlers_of_catan = [60, 65, 68, 70, 75, 77, 76, 80, 83, 85, 88]
ticket_to_ride = [55, 58, 60, 63, 66, 70, 72, 75, 78, 80, 83]
pandemic = [45, 50, 55, 57, 60, 62, 65, 68, 70, 75, 78]
carcassonne = [50, 53, 55, 60, 63, 65, 70, 72, 74, 76, 79]
terraforming_mars = [10, 15, 20, 25, 30, 35, 40, 47, 55, 62, 70]
gloomhaven = [5, 10, 15, 20, 30, 40, 55, 60, 70, 80, 85]
azul = [0, 5, 10, 15, 20, 25, 30, 40, 60, 70, 80]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, settlers_of_catan, color='red', linewidth=2)
ax.plot(years, ticket_to_ride, color='purple', linewidth=2)
ax.plot(years, pandemic, color='brown', linewidth=2)
ax.plot(years, carcassonne, color='green', linewidth=2)
ax.plot(years, terraforming_mars, color='blue', linewidth=2)
ax.plot(years, gloomhaven, color='pink', linewidth=2)
ax.plot(years, azul, color='orange', linewidth=2)

board_games = ['CATAN', 'RIDE', 'DEMIC', 'CARCAS', 'MAR', 'HAVEN', 'AZUL']
popularity_2010 = [60, 55, 45, 50, 10, 5, 0]
popularity_2020 = [88, 83, 78, 79, 70, 85, 80]
x = np.arange(len(board_games))
width = 0.35

ax_bar = ax.twinx()
ax_bar.barh(x - width/2, popularity_2010, width, color='navy', alpha=0.7)
ax_bar.barh(x + width/2, popularity_2020, width, color='skyblue', alpha=0.7)

ax.set_title("Trends of Board Games 2010-2020\nEvolution Overview", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Calendar Year", fontsize=14)
ax.set_ylabel("Score of Popularity", fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))

ax_bar.set_yticks(x)
ax_bar.set_yticklabels(board_games, fontsize=12)
ax_bar.set_xlabel("Score Value", fontsize=14)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()