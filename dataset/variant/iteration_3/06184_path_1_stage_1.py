import matplotlib.pyplot as plt
import numpy as np

seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

apples = np.array([120, 80, 100, 90])
bananas = np.array([100, 150, 80, 60])
oranges = np.array([60, 70, 110, 130])
grapes = np.array([40, 100, 50, 30])
strawberries = np.array([70, 200, 90, 40])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15

positions_apples = np.arange(len(seasons))
positions_bananas = positions_apples + bar_width
positions_oranges = positions_apples + 2 * bar_width
positions_grapes = positions_apples + 3 * bar_width
positions_strawberries = positions_apples + 4 * bar_width

# Shuffle the color assignments
bars_apples = ax.bar(positions_apples, apples, bar_width, label='Apples', color='purple') # Changed from 'red'
bars_bananas = ax.bar(positions_bananas, bananas, bar_width, label='Bananas', color='orange') # Changed from 'yellow'
bars_oranges = ax.bar(positions_oranges, oranges, bar_width, label='Oranges', color='red') # Changed from 'orange'
bars_grapes = ax.bar(positions_grapes, grapes, bar_width, label='Grapes', color='pink') # Changed from 'purple'
bars_strawberries = ax.bar(positions_strawberries, strawberries, bar_width, label='Strawberries', color='yellow') # Changed from 'pink'

ax.set_title('Seasonal Fruit Consumption Trends in Hypothetical City', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Seasons', fontsize=12)
ax.set_ylabel('Fruit Consumption (kg)', fontsize=12)
ax.set_xticks(positions_apples + 2 * bar_width)
ax.set_xticklabels(seasons)

ax.grid(True, linestyle='--', alpha=0.5)

ax.legend(loc='upper left', fontsize=10)

bars = [bars_apples, bars_bananas, bars_oranges, bars_grapes, bars_strawberries]
for bar_set in bars:
    for bar in bar_set:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=9)

plt.tight_layout()

plt.show()