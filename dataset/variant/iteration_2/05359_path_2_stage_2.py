import matplotlib.pyplot as plt
import numpy as np

activities = ['Social', 'Games', 'E-Learn', 'TV', 'eBooks', 'Calls']
average_hours_lockdown = np.array([15, 10, 25, 30, 5, 20])
average_hours_prelockdown = np.array([5, 8, 10, 15, 3, 6])

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.35
index = np.arange(len(activities))

lockdown_colors = ['orange', 'teal', 'skyblue', 'lightgreen', 'yellow', 'coral']
prelockdown_colors = ['purple', 'red', 'cyan', 'pink', 'grey', 'blue']

bar1 = ax.bar(index, average_hours_lockdown, bar_width, label='Lockdown', color=lockdown_colors, edgecolor='gray')
bar2 = ax.bar(index + bar_width, average_hours_prelockdown, bar_width, label='Prelockdown', color=prelockdown_colors, edgecolor='gray')

ax.set_title('Screen Time by Activity: Lockdown vs Prelockdown', fontsize=15, fontweight='bold')
ax.set_xlabel('Activity', fontsize=12)
ax.set_ylabel('Avg Hours/Week', fontsize=12)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(activities, fontsize=10, rotation=30, ha='right')
ax.legend(fontsize=10)

for bar_group in [bar1, bar2]:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height}', ha='center', va='bottom', fontsize=10)

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()