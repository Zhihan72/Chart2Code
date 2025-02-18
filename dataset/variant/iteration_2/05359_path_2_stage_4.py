import matplotlib.pyplot as plt
import numpy as np

activities = ['Games', 'E-Learn', 'eBooks', 'Social', 'TV', 'Calls']
average_hours_lockdown = np.array([10, 25, 5, 15, 30, 20])
average_hours_prelockdown = np.array([8, 10, 3, 5, 15, 6])

fig, ax = plt.subplots(figsize=(12, 7))

bar_height = 0.35
index = np.arange(len(activities))

lockdown_colors = ['teal', 'skyblue', 'yellow', 'orange', 'lightgreen', 'coral']
prelockdown_colors = ['red', 'cyan', 'grey', 'purple', 'pink', 'blue']

bar1 = ax.barh(index, average_hours_lockdown, bar_height, label='Lockdown', color=lockdown_colors, edgecolor='gray')
bar2 = ax.barh(index + bar_height, average_hours_prelockdown, bar_height, label='Prelockdown', color=prelockdown_colors, edgecolor='gray')

ax.set_title('Screen Time by Activity: Lockdown vs Prelockdown', fontsize=15, fontweight='bold')
ax.set_ylabel('Activity', fontsize=12)
ax.set_xlabel('Avg Hours/Week', fontsize=12)
ax.set_yticks(index + bar_height / 2)
ax.set_yticklabels(activities, fontsize=10, va='center')
ax.legend(fontsize=10)

for bar_group in [bar1, bar2]:
    for bar in bar_group:
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=10)

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()