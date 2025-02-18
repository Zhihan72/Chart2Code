import matplotlib.pyplot as plt
import numpy as np

activities = ['Social Media', 'Gaming', 'Studying', 'Entertainment', 'Miscellaneous']
hours_spent = [3, 2, 4, 2, 3]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
screen_time_week = [5, 6, 5, 7, 6, 8, 7]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# First subplot: Bar chart for average hours spent on activities
bars1 = ax1.bar(activities, hours_spent, color='darkcyan', alpha=0.8)
ax1.set_ylabel('Average Hours Spent', fontsize=12)
ax1.set_ylim(0, 5)

# Adding annotations on the bars
for bar, hour in zip(bars1, hours_spent):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height - 0.4, f'{hour} hrs', ha='center', color='white', fontsize=10)

# Second subplot: Line plot showing screen time usage distribution over the week
ax2.plot(days, screen_time_week, marker='o', color='darkorange', linewidth=2, markersize=8)
ax2.set_xlabel('Day of the Week', fontsize=12)
ax2.set_ylabel('Hours', fontsize=12)
ax2.set_ylim(4, 9)

# Highlighting the weekend as higher usage days
ax2.axvspan('Saturday', 'Sunday', color='lightgrey', alpha=0.3)
ax2.text(5.5, 8.5, "Higher Usage on Weekends", fontsize=12, fontstyle='italic', ha='center', color='black')

plt.tight_layout()
plt.show()