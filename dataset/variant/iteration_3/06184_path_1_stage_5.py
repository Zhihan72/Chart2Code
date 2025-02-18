import matplotlib.pyplot as plt
import numpy as np

seasons = ['Spr', 'Sum', 'Aut', 'Win']

apples = np.array([120, 80, 100, 90])
bananas = np.array([100, 150, 80, 60])
oranges = np.array([60, 70, 110, 130])
grapes = np.array([40, 100, 50, 30])
strawberries = np.array([70, 200, 90, 40])
pears = np.array([50, 60, 70, 90])
kiwis = np.array([130, 110, 140, 160])

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.1

positions_apples = np.arange(len(seasons))
positions_bananas = positions_apples + bar_height
positions_oranges = positions_apples + 2 * bar_height
positions_grapes = positions_apples + 3 * bar_height
positions_strawberries = positions_apples + 4 * bar_height
positions_pears = positions_apples + 5 * bar_height
positions_kiwis = positions_apples + 6 * bar_height

bars_apples = ax.barh(positions_apples, apples, bar_height,
                      label='Apl', color='green', edgecolor='black', linestyle='dotted')
bars_bananas = ax.barh(positions_bananas, bananas, bar_height,
                       label='Ban', color='blue', edgecolor='black', linestyle='dashdot')
bars_oranges = ax.barh(positions_oranges, oranges, bar_height,
                       label='Org', color='purple', edgecolor='black', linestyle='dashed')
bars_grapes = ax.barh(positions_grapes, grapes, bar_height,
                      label='Grp', color='cyan', edgecolor='black', linestyle='solid')
bars_strawberries = ax.barh(positions_strawberries, strawberries, bar_height,
                            label='Str', color='magenta', edgecolor='black', linestyle='solid')
bars_pears = ax.barh(positions_pears, pears, bar_height,
                     label='Prs', color='orange', edgecolor='black', linestyle='dotted')
bars_kiwis = ax.barh(positions_kiwis, kiwis, bar_height,
                     label='Kiw', color='brown', edgecolor='black', linestyle='dashed')

ax.set_title('Fruit Consumption', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Season', fontsize=12, fontweight='light')
ax.set_xlabel('Consumption (kg)', fontsize=12, fontweight='light')
ax.set_yticks(positions_apples + 3 * bar_height)
ax.set_yticklabels(seasons, fontsize=10, style='italic')

ax.legend(loc='upper right', fontsize=10, frameon=True, shadow=True, borderpad=1)

bars = [bars_apples, bars_bananas, bars_oranges, bars_grapes, bars_strawberries, bars_pears, bars_kiwis]
for bar_set in bars:
    for bar in bar_set:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),
                    textcoords='offset points',
                    ha='left', va='center', fontsize=9)

plt.tight_layout()

plt.show()