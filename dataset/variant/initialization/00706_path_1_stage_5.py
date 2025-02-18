import matplotlib.pyplot as plt
import numpy as np

cities = ["Nu Yok", "Lauren", "Ticko", "Paris", "Tronto", "Berland", "Singa"]
parks_per_square_mile = np.array([3.2, 4.1, 2.8, 5.0, 3.5, 4.5, 3.7])
average_rainfall = np.array([49.9, 23.8, 60.4, 25.3, 32.1, 22.7, 92.0])

positions = np.arange(len(cities))
bar_height = 0.6

fig, ax1 = plt.subplots(figsize=(14, 8))

color_map = np.array([
    [0.5, 0.0, 0.5, 1.0],
    [0.7, 0.0, 0.7, 1.0],
    [0.3, 0.0, 0.3, 1.0],
    [0.9, 0.0, 0.4, 1.0],
    [0.6, 0.0, 0.6, 1.0],
    [0.8, 0.0, 0.5, 1.0],
    [0.4, 0.0, 0.4, 1.0],
])

bars = ax1.barh(positions, parks_per_square_mile, color=color_map, height=bar_height, alpha=0.8, edgecolor='red', label='Parks p. SM')

for bar, width in zip(bars, parks_per_square_mile):
    ax1.text(width - 0.2, bar.get_y() + bar.get_height()/2, f'{width:.1f}', ha='right', va='center', color='yellow', fontsize=10)

ax2 = ax1.twiny()
ax2.plot(average_rainfall, positions, color='purple', marker='s', linestyle='--', linewidth=2, label='Avg Rainfall')
ax2.set_xlabel('Rainfall measure', fontsize=12, color='purple')

ax1.set_yticks(positions)
ax1.set_yticklabels(cities)
ax1.set_ylabel('Metropolis', fontsize=12)
ax1.set_xlabel('Parks Sq.Mile', fontsize=12)
ax1.set_xlim(0, max(parks_per_square_mile) + 2)
ax1.grid(axis='y', linestyle=':', alpha=0.5)

plt.title('Urban Green & Raindrops (2023)', fontsize=16, fontweight='bold', pad=15)

plt.tight_layout()

ax1.legend(loc='upper right')
ax2.legend(loc='lower left')

plt.show()