import matplotlib.pyplot as plt
import numpy as np

scores_data = {
    'Mathematics': [85, 88, 83, 90, 89, 86, 84, 92, 81, 87, 85, 89, 88, 84, 85, 90, 87],
    'Biology': [78, 80, 79, 82, 81, 78, 84, 79, 77, 81, 80, 83, 78, 82, 80, 79, 81],
    'Chemistry': [88, 89, 90, 86, 87, 91, 88, 85, 84, 87, 91, 86, 90, 88, 84, 89, 86],
    'Physics': [80, 83, 78, 81, 82, 80, 79, 81, 77, 80, 83, 79, 81, 82, 78, 80, 83]
}

scores = list(scores_data.values())
majors = list(scores_data.keys())

fig, axs = plt.subplots(2, 1, figsize=(10, 12))

box = axs[0].boxplot(scores, notch=False, vert=True, patch_artist=True, labels=majors)
colors = ['lightblue', 'lightpink', 'lightgreen', 'lightyellow']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_title('Exam Performance by Major', fontsize=14, fontweight='light', style='italic', pad=15)
axs[0].set_xlabel('Majors', fontsize=10)
axs[0].set_ylabel('Scores', fontsize=10)
axs[0].grid(axis='y', linestyle='-.', linewidth=0.5, alpha=0.5)

for whisker in box['whiskers']:
    whisker.set(color='navy', linewidth=1.2)
for cap in box['caps']:
    cap.set(color='navy', linewidth=1.2)
for median in box['medians']:
    median.set(color='crimson', linewidth=1.5)

weeks = np.array([1, 2, 3, 4, 5, 6])

median_scores_over_weeks = [
    [85, 87, 84, 88, 90, 89], 
    [78, 80, 79, 81, 83, 82],
    [88, 88, 89, 87, 90, 89], 
    [80, 81, 78, 80, 82, 83]
]

marker_styles = ['^', 's', 'D', '*']
line_styles = [':', '-.', '--', '-']

for major, median_score, color, marker, linestyle in zip(majors, median_scores_over_weeks, colors, marker_styles, line_styles):
    axs[1].plot(weeks, median_score, marker=marker, linestyle=linestyle, color=color, label=major)

axs[1].set_title('Median Scores by Week', fontsize=14, fontweight='light', style='italic', pad=15)
axs[1].set_xlabel('Weeks', fontsize=10)
axs[1].set_ylabel('Median Scores', fontsize=10)
axs[1].legend(loc='lower right', fontsize=8)
axs[1].grid(axis='x', linestyle='-.', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.show()