import matplotlib.pyplot as plt
import numpy as np

# Define activities and corresponding average hours
activities = ['Social', 'Gaming', 'Study', 'Entertain', 'Misc']
hours_spent = [3, 2, 4, 2, 3]

# Screen time distribution over the week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
screen_time_week = [5, 6, 5, 7, 6, 8, 7]

# Plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Bar chart for average hours spent on activities
bars1 = ax1.bar(activities, hours_spent, color=['#4CAF50', '#FFC107', '#03A9F4', '#E91E63', '#9C27B0'], alpha=0.8)
ax1.set_title('Usage Patterns', fontsize=16, fontweight='bold')
ax1.set_ylabel('Avg Hours', fontsize=12)
ax1.set_ylim(0, 5)
ax1.grid(True, linestyle='--', alpha=0.6)

# Adding annotations on the bars
for bar, hour in zip(bars1, hours_spent):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height - 0.4, f'{hour}h', ha='center', color='white', fontsize=10)

# Line plot for screen time over the week
ax2.plot(days, screen_time_week, marker='o', color='darkorange', linewidth=2, markersize=8, label='Screen Time')
ax2.set_title('Weekly Screen Time', fontsize=16, fontweight='bold')
ax2.set_xlabel('Weekday', fontsize=12)
ax2.set_ylabel('Hours', fontsize=12)
ax2.set_ylim(4, 9)
ax2.grid(True, linestyle='--', alpha=0.6)

# Highlight weekend
ax2.axvspan('Sat', 'Sun', color='lightgrey', alpha=0.3)
ax2.text(5.5, 8.5, "High Usage", fontsize=12, fontstyle='italic', ha='center', color='black')

# Combine legends
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()