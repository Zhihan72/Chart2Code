import matplotlib.pyplot as plt
import numpy as np

activity_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([45, 50, 55, 60, 68, 72, 78, 80, 85, 90])

tv_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tv_happiness_scores = np.array([30, 32, 34, 33, 32, 30, 28, 27, 25, 24])

fig, ax = plt.subplots(figsize=(12, 7))

# Randomly change colors for the two data groups
activity_color = 'blue'
tv_color = 'red'

# Randomly change marker styles
activity_marker = '^'
tv_marker = 'o'

# Randomly set line styles (here using no lines)
# You could add lines in another context using different line styles

ax.scatter(activity_hours, happiness_scores, color=activity_color, label='Physical Activities', s=120, alpha=0.8, marker=activity_marker)
ax.scatter(tv_hours, tv_happiness_scores, color=tv_color, label='Watching TV', s=120, alpha=0.8, marker=tv_marker)

# Randomly shifting legend position
ax.legend(loc='lower right')

# Randomly change the grid style
ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.4)

# Adding tightened layout to avoid clipping of ylabel and title
plt.tight_layout()

plt.show()