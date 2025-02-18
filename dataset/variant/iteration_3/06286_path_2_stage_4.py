import matplotlib.pyplot as plt
import numpy as np

activity_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([45, 50, 55, 60, 68, 72, 78, 80, 85, 90])

fig, ax = plt.subplots(figsize=(12, 7))

activity_color = 'blue'
activity_marker = '^'

ax.scatter(activity_hours, happiness_scores, color=activity_color, label='Physical Activities', s=120, alpha=0.8, marker=activity_marker)

ax.legend(loc='lower right')
ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.4)

plt.tight_layout()
plt.show()