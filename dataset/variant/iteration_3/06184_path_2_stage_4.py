import matplotlib.pyplot as plt
import numpy as np

seasons = ['Spring', 'Sunniest', 'Fall', 'Snowfall']

apples = np.array([120, 80, 100, 90])
bananas = np.array([100, 150, 80, 60])
oranges = np.array([60, 70, 110, 130])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15

positions_apples = np.arange(len(seasons))
positions_bananas = positions_apples + bar_width
positions_oranges = positions_apples + 2 * bar_width

# Change bar colors and labels randomly
bars_apples = ax.bar(positions_apples, apples, bar_width, label='Fruit Club', color='green')
bars_bananas = ax.bar(positions_bananas, bananas, bar_width, label='Energy Source', color='orange')
bars_oranges = ax.bar(positions_oranges, oranges, bar_width, label='Vitamin C', color='purple')

# Change title style 
ax.set_title('Randomized Fruity Delight Data', fontsize=18, fontweight='bold', pad=25)
ax.set_xlabel('Season Shifts', fontsize=13)
ax.set_ylabel('Market Share (kg)', fontsize=13)

# Change x-ticks and labels style
ax.set_xticks(positions_apples + bar_width)
ax.set_xticklabels(seasons, fontsize=11, rotation=45)

# Change grid style
ax.grid(True, linestyle='-.', alpha=0.3)

# Move legend to a different location and change its style
ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)

# Annotate the bars with heights
bars = [bars_apples, bars_bananas, bars_oranges]
for bar_set in bars:
    for bar in bar_set:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4),  # Slightly adjust text position
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()