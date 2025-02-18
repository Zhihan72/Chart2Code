import matplotlib.pyplot as plt
import numpy as np

activities = ['Travel', 'Exercise', 'Read', 'Social', 'Games', 'TV']
time_1980s = [10, 30, 45, 60, 15, 120]
time_2020s = [30, 60, 35, 50, 70, 100]

bar_width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

positions_1980s = np.arange(len(activities))
positions_2020s = [x + bar_width for x in positions_1980s]

ax.bar(positions_1980s, time_1980s, width=bar_width, color='#66c2a5', edgecolor='grey')
ax.bar(positions_2020s, time_2020s, width=bar_width, color='#8da0cb', edgecolor='grey')

ax.set_title('Leisure Time Trends', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Activity', fontsize=14, labelpad=15)
ax.set_ylabel('Time (min/day)', fontsize=14, labelpad=15)
ax.set_xticks([r + bar_width/2 for r in range(len(activities))])
ax.set_xticklabels(activities, rotation=45, ha='right', fontsize=12)

plt.tight_layout()
plt.show()