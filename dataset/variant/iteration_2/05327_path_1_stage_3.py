import matplotlib.pyplot as plt
import numpy as np

# Define scores for each major across various exam weeks
scores_data = {
    'Mathematics': [85, 88, 83, 90, 89, 86, 84, 92, 81, 87, 85, 89, 88, 84, 85, 90, 87],
    'Biology': [78, 80, 79, 82, 81, 78, 84, 79, 77, 81, 80, 83, 78, 82, 80, 79, 81],
    'Chemistry': [88, 89, 90, 86, 87, 91, 88, 85, 84, 87, 91, 86, 90, 88, 84, 89, 86],
    'Physics': [80, 83, 78, 81, 82, 80, 79, 81, 77, 80, 83, 79, 81, 82, 78, 80, 83]
}

scores = list(scores_data.values())
majors = list(scores_data.keys())

# Create the figure and the box plot
fig, axs = plt.subplots(1, 2, figsize=(14, 8))

# Horizontal box plot
box = axs[0].boxplot(scores, notch=True, vert=False, patch_artist=True, labels=majors)

# Shuffle colors for each major box plot
colors = ['lightcyan', 'lightcoral', 'lightsalmon', 'lightblue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customizing box plots elements
axs[0].set_title('Student Exam Performance Across Different Majors', fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel('Scores', fontsize=12)
axs[0].set_ylabel('Majors', fontsize=12)
axs[0].grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Set properties for whiskers, caps, and medians
for whisker in box['whiskers']:
    whisker.set(color='grey', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='grey', linewidth=1.5)
for median in box['medians']:
    median.set(color='black', linewidth=2)

# Line plot for median scores over exam weeks for each major
weeks = np.array([1, 2, 3, 4, 5, 6])
math_median = [85, 87, 84, 88, 90, 89]
bio_median = [78, 80, 79, 81, 83, 82]
chem_median = [88, 88, 89, 87, 90, 89]
phys_median = [80, 81, 78, 80, 82, 83]

majors = ['Mathematics', 'Biology', 'Chemistry', 'Physics']
median_scores_over_weeks = [math_median, bio_median, chem_median, phys_median]

for major, median_score, color in zip(majors, median_scores_over_weeks, colors):
    axs[1].plot(weeks, median_score, marker='o', linestyle='-', color=color, label=major)

axs[1].set_title('Median Exam Scores Over Weeks', fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel('Weeks', fontsize=12)
axs[1].set_ylabel('Median Scores', fontsize=12)
axs[1].legend(loc='upper left', fontsize=9)
axs[1].grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()