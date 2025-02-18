import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

# Randomly alter the data within each category while preserving structure
video_lectures = np.random.permutation([15, 18, 21, 25, 30, 35, 40, 50, 55, 60, 65])
interactive_quizzes = np.random.permutation([5, 8, 12, 15, 18, 20, 25, 28, 30, 32, 35])
discussion_forums = np.random.permutation([3, 5, 10, 12, 14, 18, 20, 25, 27, 30, 32])

usage_stack = np.row_stack((video_lectures, interactive_quizzes, discussion_forums))

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, usage_stack, labels=['Video Lectures', 'Interactive Quizzes', 'Online Discussion Forums'],
             colors=['#FF9999', '#66B3FF', '#99FF99'], alpha=0.8)

ax.set_title('Evolution of Digital Learning Tools Usage\n(2013-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Usage (%)', fontsize=12)

ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.xticks(rotation=45)

plt.show()