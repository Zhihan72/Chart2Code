import matplotlib.pyplot as plt
import numpy as np

activities = ['Social', 'Gaming', 'Study', 'Entertain', 'Misc']
hours_spent = [3, 2, 4, 2, 3]

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
screen_time_week = [5, 6, 5, 7, 6, 8, 7]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Updated color scheme for the bar chart
ax1.bar(activities, hours_spent, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFCC33'], alpha=0.8)
ax1.set_title('Usage Patterns', fontsize=16, fontweight='bold')
ax1.set_ylabel('Avg Hours', fontsize=12)
ax1.set_ylim(0, 5)

for bar, hour in zip(ax1.patches, hours_spent):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height - 0.4, f'{hour}h', ha='center', color='white', fontsize=10)

# Updated color for the line plot
ax2.plot(days, screen_time_week, marker='o', color='#FF5733', linewidth=2, markersize=8)
ax2.set_title('Weekly Screen Time', fontsize=16, fontweight='bold')
ax2.set_xlabel('Weekday', fontsize=12)
ax2.set_ylabel('Hours', fontsize=12)
ax2.set_ylim(4, 9)

ax2.axvspan('Sat', 'Sun', color='lightgrey', alpha=0.3)
ax2.text(5.5, 8.5, "High Usage", fontsize=12, fontstyle='italic', ha='center', color='black')

plt.tight_layout()
plt.show()