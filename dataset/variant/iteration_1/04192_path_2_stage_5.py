import matplotlib.pyplot as plt
import numpy as np

board_games = ['CATAN', 'RIDE', 'DEMIC', 'CARCAS', 'MAR', 'HAVEN', 'AZUL']
popularity_2010 = [60, 55, 45, 50, 10, 5, 0]
popularity_2020 = [88, 83, 78, 79, 70, 85, 80]
x = np.arange(len(board_games))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(x - width/2, popularity_2010, width, label='2010', color='navy', alpha=0.7)
ax.barh(x + width/2, popularity_2020, width, label='2020', color='skyblue', alpha=0.7)

ax.set_yticks(x)
ax.set_yticklabels(board_games, fontsize=12)
ax.set_xlabel("Score of Popularity", fontsize=14)
ax.set_title("Popularity of Board Games in 2010 vs 2020", fontsize=16, fontweight='bold', pad=20)
ax.legend()

plt.tight_layout()
plt.show()