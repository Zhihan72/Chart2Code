import matplotlib.pyplot as plt
import numpy as np

# Data
activity_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([72, 78, 50, 60, 45, 85, 55, 80, 68, 90])
tv_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tv_happiness_scores = np.array([32, 27, 24, 34, 28, 32, 33, 25, 30, 30])

fig, ax = plt.subplots(figsize=(12, 7))
common_color = 'darkgreen'
ax.scatter(activity_hours, happiness_scores, color=common_color, label='Workouts', s=100, alpha=0.7)
ax.scatter(tv_hours, tv_happiness_scores, color=common_color, label='Binge Watching', s=100, alpha=0.7)

ax.set_title('The Link Between Exercise and TV Viewing\n on Joyfulness Weekly', fontsize=16, fontweight='bold')
ax.set_xlabel('Weekly Hours', fontsize=14)
ax.set_ylabel('Joy Index (max 100)', fontsize=14)
ax.legend(title='Type of Activity', fontsize=12, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()