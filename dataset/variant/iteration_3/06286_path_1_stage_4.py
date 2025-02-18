import matplotlib.pyplot as plt
import numpy as np

# Data
activity_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([72, 78, 50, 60, 45, 85, 55, 80, 68, 90])
tv_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tv_happiness_scores = np.array([32, 27, 24, 34, 28, 32, 33, 25, 30, 30])

fig, ax = plt.subplots(figsize=(10, 6))  # Changed size for variety
ax.scatter(activity_hours, happiness_scores, color='blue', label='Exercise', s=120, alpha=0.8, marker='x')
ax.scatter(tv_hours, tv_happiness_scores, color='orange', label='TV', s=120, alpha=0.8, marker='o')

ax.set_title('Impact of Habits on Happiness', fontsize=15, fontweight='light', color='navy')
ax.set_xlabel('Hours Per Week', fontsize=13, color='darkred')
ax.set_ylabel('Happiness Index (0-100)', fontsize=13, color='darkred')
ax.legend(title='Activities', fontsize=11, loc='lower right', edgecolor='lavender')
ax.grid(True, linestyle=':', alpha=0.4)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()