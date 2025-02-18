import matplotlib.pyplot as plt
import numpy as np

cities = ["Nu Yok", "Lauren", "Ticko", "Paris", "Tronto", "Berland", "Singa"]
parks_per_square_mile = np.array([3.2, 4.1, 2.8, 5.0, 3.5, 4.5, 3.7])
average_rainfall = np.array([49.9, 23.8, 60.4, 25.3, 32.1, 22.7, 92.0])

positions = np.arange(len(cities))
bar_width = 0.6

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

bars = ax1.bar(positions, parks_per_square_mile, color=color_map, width=bar_width, alpha=0.8, edgecolor='red', label='Parks p. SM')

for bar, height in zip(bars, parks_per_square_mile):
    ax1.text(bar.get_x() + bar.get_width()/2, height - 0.1, f'{height:.1f}', ha='center', va='bottom', color='yellow', fontsize=10)

ax2 = ax1.twinx()
ax2.plot(positions, average_rainfall, color='purple', marker='s', linestyle='--', linewidth=2, label='Avg Rainfall')
ax2.set_ylabel('Rainfall measure', fontsize=12, color='purple')

ax1.set_xticks(positions)
ax1.set_xticklabels(cities, rotation=30, ha='right')
ax1.set_xlabel('Metropolis', fontsize=12)
ax1.set_ylabel('Parks Sq.Mile', fontsize=12)
ax1.set_ylim(0, max(parks_per_square_mile) + 2)
ax1.grid(axis='x', linestyle=':', alpha=0.5)

plt.title('Urban Green & Raindrops (2023)', fontsize=16, fontweight='bold', pad=15)

plt.tight_layout()

ax1.legend(loc='lower right')
ax2.legend(loc='upper left')

plt.show()