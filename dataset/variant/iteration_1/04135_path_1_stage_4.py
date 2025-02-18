import matplotlib.pyplot as plt
import numpy as np

activities = ['Reading', 'TV Watching', 'Video Games', 'Socializing', 'Physical Activity', 'Travel for Leisure']
time_1980s = [60, 10, 30, 45, 15, 120]
time_2000s = [45, 25, 80, 150, 40, 25]
time_2020s = [70, 35, 50, 60, 100, 30]

bar_height = 0.25
fig, ax = plt.subplots(figsize=(14, 8))

positions_1980s = np.arange(len(activities))
positions_2000s = [x + bar_height for x in positions_1980s]
positions_2020s = [x + bar_height for x in positions_2000s]

uniform_color = '#1f77b4'

ax.barh(positions_1980s, time_1980s, height=bar_height, color=uniform_color, edgecolor='grey')
ax.barh(positions_2000s, time_2000s, height=bar_height, color=uniform_color, edgecolor='grey')
ax.barh(positions_2020s, time_2020s, height=bar_height, color=uniform_color, edgecolor='grey')

ax.set_yticks([])  # Remove y-ticks
ax.set_xticks([])  # Remove x-ticks

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()