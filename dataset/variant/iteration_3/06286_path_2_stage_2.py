import matplotlib.pyplot as plt
import numpy as np

activity_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([45, 50, 55, 60, 68, 72, 78, 80, 85, 90])

tv_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tv_happiness_scores = np.array([30, 32, 34, 33, 32, 30, 28, 27, 25, 24])

fig, ax = plt.subplots(figsize=(12, 7))

# Apply the same color to all data groups
consistent_color = 'darkgreen'

ax.scatter(activity_hours, happiness_scores, color=consistent_color, label='Physical Activities', s=100, alpha=0.7)

ax.scatter(tv_hours, tv_happiness_scores, color=consistent_color, label='Watching TV', s=100, alpha=0.7)

ax.legend(loc='upper left')

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()