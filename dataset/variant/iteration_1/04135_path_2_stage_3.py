import matplotlib.pyplot as plt
import numpy as np

activities = ['Travel', 'Exercise', 'Read', 'Social', 'Games', 'TV']
time_1980s = [10, 30, 45, 60, 15, 120]
time_2000s = [25, 40, 25, 80, 45, 150]
time_2020s = [30, 60, 35, 50, 70, 100]

bar_width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

positions_1980s = np.arange(len(activities))
positions_2000s = [x + bar_width for x in positions_1980s]
positions_2020s = [x + bar_width for x in positions_2000s]

bars_1980s = ax.bar(positions_1980s, time_1980s, width=bar_width, color='#66c2a5', edgecolor='grey', label='1980s')
bars_2000s = ax.bar(positions_2000s, time_2000s, width=bar_width, color='#fc8d62', edgecolor='grey', label='2000s')
bars_2020s = ax.bar(positions_2020s, time_2020s, width=bar_width, color='#8da0cb', edgecolor='grey', label='2020s')

ax.set_title('Leisure Time Trends', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Activity', fontsize=14, labelpad=15)
ax.set_ylabel('Time (min/day)', fontsize=14, labelpad=15)
ax.set_xticks([r + bar_width for r in range(len(activities))])
ax.set_xticklabels(activities, rotation=45, ha='right', fontsize=12)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', fontsize=10, fontweight='bold')

add_labels(bars_1980s)
add_labels(bars_2000s)
add_labels(bars_2020s)

ax.legend(title='Decade', loc='upper left', fontsize=10, title_fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()