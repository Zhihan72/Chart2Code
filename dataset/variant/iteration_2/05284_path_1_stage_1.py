import matplotlib.pyplot as plt
import numpy as np

activities = ['Entertainment', 'Other', 'Study', 'Sleep', 'Socializing', 'Sports']
weekday_hours = [3, 3, 6, 8, 2, 2]
weekend_hours = [4, 2, 2, 9, 4, 3]

x_positions = np.arange(len(activities))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(12, 8))

rects1 = ax.bar(x_positions - bar_width/2, weekday_hours, width=bar_width, label='Workday', color='skyblue', edgecolor='black')
rects2 = ax.bar(x_positions + bar_width/2, weekend_hours, width=bar_width, label='Offday', color='salmon', edgecolor='black')

ax.set_title('High School Activities: Morning vs Evening', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Activity Types', fontsize=14)
ax.set_ylabel('Time Allocated (hours)', fontsize=14)

ax.set_xticks(x_positions)
ax.set_xticklabels(activities, fontsize=12)

ax.legend(title='Period Type', title_fontsize='13', fontsize=11, loc='upper right')
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

add_labels(rects1)
add_labels(rects2)

plt.tight_layout()
plt.show()