import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

video_lectures = [60, 65, 35, 50, 55, 21, 40, 15, 18, 25, 30]
interactive_quizzes = [20, 28, 30, 12, 25, 5, 32, 8, 35, 18, 15]
discussion_forums = [14, 18, 12, 10, 5, 32, 25, 30, 27, 3, 20]

usage_stack = np.row_stack((video_lectures, interactive_quizzes, discussion_forums))

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, usage_stack, colors=['#FF5733', '#C70039', '#900C3F'], alpha=0.8)

ax.set_title('Digital Tool Usage (2013-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Usage (%)', fontsize=12)

plt.xticks(rotation=45)
plt.show()