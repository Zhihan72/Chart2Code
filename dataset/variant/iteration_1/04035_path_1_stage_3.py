import matplotlib.pyplot as plt
import numpy as np

activities = ['Social Media', 'Gaming', 'Studying', 'Entertainment', 'Miscellaneous']
hours_spent = [3, 2, 4, 2, 3]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
screen_time_week = [5, 6, 5, 7, 6, 8, 7]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# First subplot: Bar chart for average hours spent on activities (without annotations)
bars1 = ax1.bar(activities, hours_spent, color='darkcyan', alpha=0.8)
ax1.set_ylim(0, 5)

# Second subplot: Line plot showing screen time usage distribution over the week (no textual elements)
ax2.plot(days, screen_time_week, marker='o', color='darkorange', linewidth=2, markersize=8)
ax2.set_ylim(4, 9)
ax2.axvspan('Saturday', 'Sunday', color='lightgrey', alpha=0.3)

plt.tight_layout()
plt.show()