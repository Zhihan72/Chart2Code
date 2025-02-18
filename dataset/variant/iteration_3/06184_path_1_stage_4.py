import matplotlib.pyplot as plt
import numpy as np

seasons = ['Spr', 'Sum', 'Aut', 'Win']

apples = np.array([120, 80, 100, 90])
bananas = np.array([100, 150, 80, 60])
oranges = np.array([60, 70, 110, 130])
grapes = np.array([40, 100, 50, 30])
strawberries = np.array([70, 200, 90, 40])
pears = np.array([50, 60, 70, 90])  # New fruit data
kiwis = np.array([130, 110, 140, 160])  # New fruit data

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.1  # Adjusted for the new data series

positions_apples = np.arange(len(seasons))
positions_bananas = positions_apples + bar_width
positions_oranges = positions_apples + 2 * bar_width
positions_grapes = positions_apples + 3 * bar_width
positions_strawberries = positions_apples + 4 * bar_width
positions_pears = positions_apples + 5 * bar_width
positions_kiwis = positions_apples + 6 * bar_width

bars_apples = ax.bar(positions_apples, apples, bar_width, 
                     label='Apl', color='green', edgecolor='black', linestyle='dotted')
bars_bananas = ax.bar(positions_bananas, bananas, bar_width, 
                      label='Ban', color='blue', edgecolor='black', linestyle='dashdot')
bars_oranges = ax.bar(positions_oranges, oranges, bar_width, 
                      label='Org', color='purple', edgecolor='black', linestyle='dashed')
bars_grapes = ax.bar(positions_grapes, grapes, bar_width, 
                     label='Grp', color='cyan', edgecolor='black', linestyle='solid')
bars_strawberries = ax.bar(positions_strawberries, strawberries, bar_width, 
                           label='Str', color='magenta', edgecolor='black', linestyle='solid')
bars_pears = ax.bar(positions_pears, pears, bar_width, 
                    label='Prs', color='orange', edgecolor='black', linestyle='dotted')
bars_kiwis = ax.bar(positions_kiwis, kiwis, bar_width, 
                    label='Kiw', color='brown', edgecolor='black', linestyle='dashed')

ax.set_title('Fruit Consumption', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Season', fontsize=12, fontweight='light')
ax.set_ylabel('Consumption (kg)', fontsize=12, fontweight='light')
ax.set_xticks(positions_apples + 3 * bar_width)
ax.set_xticklabels(seasons, fontsize=10, style='italic')

ax.legend(loc='upper right', fontsize=10, frameon=True, shadow=True, borderpad=1)

bars = [bars_apples, bars_bananas, bars_oranges, bars_grapes, bars_strawberries, bars_pears, bars_kiwis]
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