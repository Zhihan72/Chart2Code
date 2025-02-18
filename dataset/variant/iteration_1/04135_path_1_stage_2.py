import matplotlib.pyplot as plt
import numpy as np

# Activities and altered time spent (in minutes) per day for each decade
activities = ['Reading', 'TV Watching', 'Video Games', 'Socializing', 'Physical Activity', 'Travel for Leisure']
time_1980s = [60, 10, 30, 45, 15, 120]  # Altered order for each decade
time_2000s = [45, 25, 80, 150, 40, 25]
time_2020s = [70, 35, 50, 60, 100, 30]

time_data = np.array([time_1980s, time_2000s, time_2020s])
decades = ['1980s', '2000s', '2020s']

bar_width = 0.25
fig, ax = plt.subplots(figsize=(14, 8))

positions_1980s = np.arange(len(activities))
positions_2000s = [x + bar_width for x in positions_1980s]
positions_2020s = [x + bar_width for x in positions_2000s]

uniform_color = '#1f77b4'

bars_1980s = ax.bar(positions_1980s, time_1980s, width=bar_width, color=uniform_color, edgecolor='grey', label='1980s')
bars_2000s = ax.bar(positions_2000s, time_2000s, width=bar_width, color=uniform_color, edgecolor='grey', label='2000s')
bars_2020s = ax.bar(positions_2020s, time_2020s, width=bar_width, color=uniform_color, edgecolor='grey', label='2020s')

ax.set_title('Evolution of Leisure Time Over Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Activities', fontsize=14, labelpad=15)
ax.set_ylabel('Average Time Spent (minutes per day)', fontsize=14, labelpad=15)
ax.set_xticks([r + bar_width for r in range(len(activities))])
ax.set_xticklabels(activities, rotation=45, ha='right', fontsize=12)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', fontsize=10, fontweight='bold')

add_labels(bars_1980s)
add_labels(bars_2000s)
add_labels(bars_2020s)

ax.legend(title='Decades', loc='upper left', fontsize=10, title_fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()