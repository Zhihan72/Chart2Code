import matplotlib.pyplot as plt
import numpy as np

activities = ['Study', 'Sports', 'Entertainment', 'Socializing', 'Sleep', 'Other']
weekday_hours = [6, 2, 3, 2, 8, 3]
weekend_hours = [2, 3, 4, 4, 9, 2]
hybrid_hours = [4, 3, 3.5, 3, 8.5, 2.5]

x_positions = np.arange(len(activities))
bar_width = 0.25

fig, ax = plt.subplots(figsize=(12, 8))

rects1 = ax.bar(x_positions - bar_width, weekday_hours, width=bar_width, label='Weekday', color='darkgreen', edgecolor='black')
rects2 = ax.bar(x_positions, weekend_hours, width=bar_width, label='Weekend', color='darkorange', edgecolor='black')
rects3 = ax.bar(x_positions + bar_width, hybrid_hours, width=bar_width, label='Hybrid', color='royalblue', edgecolor='black')

ax.set_title('Average Time Spent on Various Activities by High School Students\nWeekday vs Weekend vs Hybrid', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Activities', fontsize=14)
ax.set_ylabel('Average Time Spent (hours)', fontsize=14)
ax.set_xticks(x_positions)
ax.set_xticklabels(activities, fontsize=12)
ax.legend(title='Day Type', title_fontsize='13', fontsize=11, loc='upper right')
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
add_labels(rects3)

plt.tight_layout()
plt.show()