import matplotlib.pyplot as plt
import numpy as np

age_groups = ["Infants", "Tweens", "Millennials", "Elders", "Preteens"]  # Randomly altered group labels
days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]  # Randomly altered day labels
activity_data = np.array([
    [40, 50, 45, 55, 60, 70, 80],  # Infants (originally Children)
    [30, 35, 40, 45, 50, 60, 65],  # Tweens (originally Teenagers)
    [35, 40, 45, 50, 55, 65, 70],  # Millennials (originally Young Adults)
    [25, 30, 35, 40, 35, 45, 50],  # Elders (originally Adults)
    [20, 25, 20, 15, 25, 30, 35]   # Preteens (originally Seniors)
])

x = np.arange(len(days_of_week))

fig, ax = plt.subplots(figsize=(14, 8))

new_colors = ["#FF6347", "#4682B4", "#32CD32", "#DAA520", "#9B59B6"]

bottom_stack = np.zeros(len(days_of_week))

for i, age_group in enumerate(age_groups):
    ax.bar(x, activity_data[i], label=age_group, bottom=bottom_stack, color=new_colors[i])
    bottom_stack += activity_data[i]

ax.set_xlabel('Weekday', fontsize=14)  # Randomly altered X-axis label
ax.set_ylabel('Avg. Activity Per Day (Min)', fontsize=14)  # Randomly altered Y-axis label
ax.set_title('Physical Activity Variety Among Age Categories', fontsize=16, fontweight='bold')  # Randomly altered title
ax.set_xticks(x)
ax.set_xticklabels(days_of_week)
ax.legend(title="Demographics")

plt.tight_layout()
plt.savefig("weekly_activity_levels_stacked_bar.png")
plt.show()