import matplotlib.pyplot as plt
import numpy as np

activities = ['Reading', 'TV Watching', 'Video Games', 'Socializing', 'Physical Activity', 'Travel for Leisure']
time_1980s = [60, 10, 30, 45, 15, 120]
time_2000s = [45, 25, 80, 150, 40, 25]
time_2020s = [70, 35, 50, 60, 100, 30]

time_data = np.array([time_1980s, time_2000s, time_2020s])
decades = ['1980s', '2000s', '2020s']

bar_height = 0.25
fig, ax = plt.subplots(figsize=(14, 8))

positions_1980s = np.arange(len(activities))
positions_2000s = [x + bar_height for x in positions_1980s]
positions_2020s = [x + bar_height for x in positions_2000s]

uniform_color = '#1f77b4'

bars_1980s = ax.barh(positions_1980s, time_1980s, height=bar_height, color=uniform_color, edgecolor='grey', label='1980s')
bars_2000s = ax.barh(positions_2000s, time_2000s, height=bar_height, color=uniform_color, edgecolor='grey', label='2000s')
bars_2020s = ax.barh(positions_2020s, time_2020s, height=bar_height, color=uniform_color, edgecolor='grey', label='2020s')

ax.set_title('Evolution of Leisure Time Over Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Activities', fontsize=14, labelpad=15)
ax.set_xlabel('Average Time Spent (minutes per day)', fontsize=14, labelpad=15)
ax.set_yticks([r + bar_height for r in range(len(activities))])
ax.set_yticklabels(activities, fontsize=12)

def add_labels(bars):
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=10, fontweight='bold')

add_labels(bars_1980s)
add_labels(bars_2000s)
add_labels(bars_2020s)

ax.legend(title='Decades', loc='upper right', fontsize=10, title_fontsize=12)
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()