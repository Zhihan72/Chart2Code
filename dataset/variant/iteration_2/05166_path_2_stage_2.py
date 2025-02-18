import matplotlib.pyplot as plt
import numpy as np

age_groups = ["Children", "Teenagers", "Young Adults", "Adults", "Seniors"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
activity_data = np.array([
    [40, 50, 45, 55, 60, 70, 80],  # Children
    [30, 35, 40, 45, 50, 60, 65],  # Teenagers
    [35, 40, 45, 50, 55, 65, 70],  # Young Adults
    [25, 30, 35, 40, 35, 45, 50],  # Adults
    [20, 25, 20, 15, 25, 30, 35]   # Seniors
])

x = np.arange(len(days_of_week))
bar_width = 0.15

fig, ax = plt.subplots(figsize=(14, 8))

for i, age_group in enumerate(age_groups):
    ax.bar(x + i * bar_width, activity_data[i], bar_width)

ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Average Daily Activity (Minutes)', fontsize=14)
ax.set_title('Weekly Physical Activity Levels Across Different Age Groups', fontsize=16, fontweight='bold')
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(days_of_week)

for i, age_group in enumerate(age_groups):
    for j, activity in enumerate(activity_data[i]):
        ax.text(x[j] + i * bar_width, activity + 1, f'{activity}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()

plt.savefig("weekly_activity_levels.png")
plt.show()