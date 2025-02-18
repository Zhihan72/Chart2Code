import matplotlib.pyplot as plt
import numpy as np

activities = ['Entertainment', 'Other', 'Study', 'Sleep', 'Sports']
weekday_hours = [3, 3, 6, 8, 2]
weekend_hours = [4, 2, 2, 9, 3]

y_positions = np.arange(len(activities))
bar_height = 0.35

fig, ax = plt.subplots(figsize=(12, 8))

rects1 = ax.barh(y_positions - bar_height/2, weekday_hours, height=bar_height, label='Weekday', color='skyblue', edgecolor='darkred', hatch='x')
rects2 = ax.barh(y_positions + bar_height/2, weekend_hours, height=bar_height, label='Weekend', color='salmon', edgecolor='darkred', hatch='/')

ax.set_title('High School Activities: Weekday vs Weekend', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Activity Types', fontsize=14)
ax.set_xlabel('Time Allocated (hours)', fontsize=14)

ax.set_yticks(y_positions)
ax.set_yticklabels(activities, fontsize=12)

ax.legend(title='Time Period', title_fontsize='13', fontsize=11, loc='upper left')
ax.xaxis.grid(True, linestyle=':', linewidth=1, alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

def add_labels(rects):
    for rect in rects:
        width = rect.get_width()
        ax.annotate(f'{width}',
                    xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=10, fontweight='bold')

add_labels(rects1)
add_labels(rects2)

plt.tight_layout()
plt.show()