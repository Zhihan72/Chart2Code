import matplotlib.pyplot as plt
import numpy as np

seasons = ['Spring', 'Sunniest', 'Fall', 'Snowfall']

apples = np.array([120, 80, 100, 90])
bananas = np.array([100, 150, 80, 60])
oranges = np.array([60, 70, 110, 130])

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15

positions_apples = np.arange(len(seasons))
positions_bananas = positions_apples + bar_height
positions_oranges = positions_apples + 2 * bar_height

bars_apples = ax.barh(positions_apples, apples, bar_height, label='Fruit Club', color='green')
bars_bananas = ax.barh(positions_bananas, bananas, bar_height, label='Energy Source', color='orange')
bars_oranges = ax.barh(positions_oranges, oranges, bar_height, label='Vitamin C', color='purple')

ax.set_title('Randomized Fruity Delight Data', fontsize=18, fontweight='bold', pad=25)
ax.set_ylabel('Season Shifts', fontsize=13)
ax.set_xlabel('Market Share (kg)', fontsize=13)

ax.set_yticks(positions_apples + bar_height)
ax.set_yticklabels(seasons, fontsize=11)

ax.grid(True, linestyle='-.', alpha=0.3)

ax.legend(loc='lower right', fontsize=12, frameon=True, shadow=True)

bars = [bars_apples, bars_bananas, bars_oranges]
for bar_set in bars:
    for bar in bar_set:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(4, 0),  # Slightly adjust text position
                    textcoords='offset points',
                    ha='left', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()