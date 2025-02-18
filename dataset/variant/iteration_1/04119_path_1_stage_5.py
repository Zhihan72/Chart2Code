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
             colors=['#66b2ff', '#ff6666', '#66ff66', '#ff66ff', '#ffff66', '#66ffff', '#ff9966'],
             alpha=0.7)

lines = ['-', '--', '-.', ':', '-', '--', '-.']
markers = ['o', 'v', '^', '<', '>', 's', 'p']

for i, data in enumerate([battle_royale, MOBA, FPS, sports, strategy, racing, puzzle]):
    ax.plot(years, data, lines[i], marker=markers[i], label=f'Data {i+1}')

ax.grid(True, linestyle='-.', alpha=0.8, color='gray')

ax.legend(title='Game Types', loc='upper left', fontsize=9, title_fontsize='10', frameon=True, shadow=True)
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.tight_layout()
plt.show()