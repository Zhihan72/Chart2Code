import matplotlib.pyplot as plt
import numpy as np

math_scores = [82, 89, 90, 85, 88, 86, 87, 85, 89, 90, 87, 88, 84, 85, 89]
science_scores = [79, 81, 83, 80, 82, 84, 81, 85, 86, 83, 80, 82, 85, 84, 83]
english_scores = [75, 78, 77, 80, 82, 76, 78, 74, 79, 81, 80, 77, 76, 75, 78]
history_scores = [88, 85, 87, 86, 89, 90, 85, 84, 88, 86, 87, 88, 89, 85, 86]
art_scores = [70, 72, 68, 73, 75, 71, 72, 69, 74, 76, 74, 71, 70, 73, 75]

years = np.array([2018, 2019, 2020, 2021, 2022])
avg_math_scores = np.array([80, 82, 85, 87, 88])
avg_science_scores = np.array([75, 77, 80, 82, 84])
avg_english_scores = np.array([70, 72, 74, 76, 78])
avg_history_scores = np.array([85, 86, 87, 88, 89])
avg_art_scores = np.array([68, 70, 72, 73, 74])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Single color for all line plots
single_color = '#3498DB'

ax1.plot(years, avg_math_scores, color=single_color, marker='o', linestyle='-')
ax1.plot(years, avg_science_scores, color=single_color, marker='s', linestyle='--')
ax1.plot(years, avg_english_scores, color=single_color, marker='^', linestyle='-.')
ax1.plot(years, avg_history_scores, color=single_color, marker='d', linestyle=':')
ax1.plot(years, avg_art_scores, color=single_color, marker='v', linestyle='-')

ax1.set_title('Average Improvement in Scores Over Time\nFor Different Subjects', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Scores', fontsize=12)
ax1.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Single color for all box plots
subjects = ['Math', 'Science', 'English', 'History', 'Art']
test_scores = [math_scores, science_scores, english_scores, history_scores, art_scores]

box = ax2.boxplot(test_scores, vert=False, patch_artist=True,
                  boxprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  capprops=dict(color='black'),
                  flierprops=dict(marker='o', color='black', alpha=0.5),
                  medianprops=dict(color='red'))

for patch in box['boxes']:
    patch.set_facecolor(single_color)

ax2.set_yticklabels(subjects)
ax2.set_title('Distribution of Test Scores Across Subjects\nFor College Entrance Exams', fontsize=14, fontweight='bold')
ax2.set_xlabel('Test Scores', fontsize=12)
ax2.set_ylabel('Subjects', fontsize=12)

plt.tight_layout()
plt.show()