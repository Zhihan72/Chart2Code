import matplotlib.pyplot as plt
import numpy as np

# Here is our backstory and plan:
# Backstory: "Smartphone Usage Patterns Among University Students"
# We will focus on the average number of hours spent on different activities using a smartphone throughout a typical day.
# We will create data for the following activities: Social Media, Gaming, Studying, Entertainment, Miscellaneous.
# Additionally, we'll provide a subplot showing the distribution of Screen Time usage over the days of the week.

# Defining the categories
activities = ['Social Media', 'Gaming', 'Studying', 'Entertainment', 'Miscellaneous']

# Average hours spent on each activity on a typical day
hours_spent = [3, 2, 4, 2, 3]

# Distribution of screen time usage over the week (in hours)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
screen_time_week = [5, 6, 5, 7, 6, 8, 7]

# Plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# First subplot: Bar chart for average hours spent on activities
bars1 = ax1.bar(activities, hours_spent, color=['#4CAF50', '#FFC107', '#03A9F4', '#E91E63', '#9C27B0'], alpha=0.8)
ax1.set_title('Smartphone Usage Patterns Among University Students', fontsize=16, fontweight='bold')
ax1.set_ylabel('Average Hours Spent', fontsize=12)
ax1.set_ylim(0, 5)
ax1.grid(True, linestyle='--', alpha=0.6)

# Adding annotations on the bars
for bar, hour in zip(bars1, hours_spent):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height - 0.4, f'{hour} hrs', ha='center', color='white', fontsize=10)

# Second subplot: Line plot showing screen time usage distribution over the week
ax2.plot(days, screen_time_week, marker='o', color='darkorange', linewidth=2, markersize=8, label='Screen Time (hours)')
ax2.set_title('Weekly Screen Time Usage Distribution', fontsize=16, fontweight='bold')
ax2.set_xlabel('Day of the Week', fontsize=12)
ax2.set_ylabel('Hours', fontsize=12)
ax2.set_ylim(4, 9)
ax2.grid(True, linestyle='--', alpha=0.6)

# Highlighting the weekend as higher usage days
weekend_start = ax2.axvspan('Saturday', 'Sunday', color='lightgrey', alpha=0.3)
weekend_label = ax2.text(5.5, 8.5, "Higher Usage on Weekends", fontsize=12, fontstyle='italic', ha='center', color='black')

# Combine legends from both axes
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()