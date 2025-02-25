import matplotlib.pyplot as plt
import numpy as np

# Data for average daily physical activity levels (in minutes)
age_groups = ["Children", "Teenagers", "Adults", "Seniors"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
activity_data = np.array([
    [40, 50, 45, 55, 60, 70, 80],  # Children
    [30, 35, 40, 45, 50, 60, 65],  # Teenagers
    [25, 30, 35, 40, 35, 45, 50],  # Adults
    [20, 25, 20, 15, 25, 30, 35]   # Seniors
])

# Calculate the baseline position
stacking_order = [activity_data[0], -activity_data[1], activity_data[2], -activity_data[3]]

# Create subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each age group's activity data towards the center baseline
for i, data in enumerate(stacking_order):
    if i % 2 == 0:
        ax.bar(days_of_week, data, label=age_groups[i], bottom=np.sum(stacking_order[:i], axis=0))
    else:
        ax.bar(days_of_week, data, label=age_groups[i], bottom=-np.sum(np.abs(stacking_order[:i]), axis=0))

# Add labels and title
ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Diverging Average Daily Activity (Minutes)', fontsize=14)
ax.set_title('Diverging Physical Activity Levels Across Different Age Groups', fontsize=16, fontweight='bold')
ax.legend(title='Age Groups', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Save and show the plot
plt.savefig("diverging_weekly_activity_levels.png")
plt.show()