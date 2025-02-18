import matplotlib.pyplot as plt
import numpy as np

# Backstory and data
# We are examining the average daily physical activity levels (in minutes) of different age groups over a week.
age_groups = ["Children", "Teenagers", "Adults", "Seniors"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
activity_data = np.array([
    [40, 50, 45, 55, 60, 70, 80],  # Children
    [30, 35, 40, 45, 50, 60, 65],  # Teenagers
    [25, 30, 35, 40, 35, 45, 50],  # Adults
    [20, 25, 20, 15, 25, 30, 35]   # Seniors
])

# Create the primary bar chart
x = np.arange(len(days_of_week))  # the label locations
bar_width = 0.2  # the width of the bars

# Create subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each age group's activity data with different offset
for i, age_group in enumerate(age_groups):
    ax.bar(x + i * bar_width, activity_data[i], bar_width, label=age_group)

# Add some text for labels, title and custom x-axis tick labels
ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Average Daily Activity (Minutes)', fontsize=14)
ax.set_title('Weekly Physical Activity Levels Across Different Age Groups', fontsize=16, fontweight='bold')
ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(days_of_week)
ax.legend(title='Age Groups', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate significant data points
for i, age_group in enumerate(age_groups):
    for j, activity in enumerate(activity_data[i]):
        ax.text(x[j] + i * bar_width, activity + 1, f'{activity}', ha='center', va='bottom', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.savefig("weekly_activity_levels.png")
plt.show()