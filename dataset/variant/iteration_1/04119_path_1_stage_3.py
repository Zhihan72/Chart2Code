import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

battle_royale = np.array([5, 7, 10, 15, 20, 25, 35, 45, 55, 60, 65])
MOBA = np.array([20, 23, 25, 27, 30, 32, 35, 38, 40, 45, 48])
FPS = np.array([15, 18, 20, 22, 23, 25, 28, 30, 33, 36, 40])
sports = np.array([10, 12, 13, 15, 18, 20, 23, 27, 30, 33, 35])
strategy = np.array([8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26])
racing = np.array([3, 5, 7, 9, 12, 15, 18, 21, 25, 30, 35])
puzzle = np.array([2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 18])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, battle_royale, MOBA, FPS, sports, strategy, racing, puzzle,
             labels=['Battle Royale', 'MOBA', 'FPS', 'Sports', 'Strategy', 'Racing', 'Puzzle'],
             colors=['#66b2ff'],  # Use the same color for all data groups
             alpha=0.8)
ax.set_title('Global Esports Engagement (2015-2025)\nGrowth Across Different Genres', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Engagement (Millions)', fontsize=14)
ax.legend(loc='upper left', title='Esports Genres', fontsize=11)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()