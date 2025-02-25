import matplotlib.pyplot as plt
import numpy as np

math_scores = [82, 89, 90, 85, 88, 86, 87, 85, 89, 90, 87, 88, 84, 85, 89]
science_scores = [79, 81, 83, 80, 82, 84, 81, 85, 86, 83, 80, 82, 85, 84, 83]
english_scores = [75, 78, 77, 80, 82, 76, 78, 74, 79, 81, 80, 77, 76, 75, 78]
history_scores = [88, 85, 87, 86, 89, 90, 85, 84, 88, 86, 87, 88, 89, 85, 86]
art_scores = [72, 75, 78, 74, 76, 77, 73, 75, 79, 80, 71, 74, 73, 76, 77]
pe_scores = [85, 87, 90, 88, 86, 85, 89, 84, 86, 88, 90, 89, 87, 85, 88]

years = np.array([2018, 2019, 2020, 2021, 2022])

avg_math_scores = np.array([80, 82, 85, 87, 88])
avg_science_scores = np.array([75, 77, 80, 82, 84])
avg_english_scores = np.array([70, 72, 74, 76, 78])
avg_history_scores = np.array([85, 86, 87, 88, 89])
avg_art_scores = np.array([70, 72, 75, 77, 79])
avg_pe_scores = np.array([81, 83, 85, 87, 88])

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 8))

ax2.plot(years, avg_math_scores, label='Math', color='#7DCEA0', marker='d', linestyle=':')
ax2.plot(years, avg_science_scores, label='Science', color='#BB8FCE', marker='x', linestyle='--')
ax2.plot(years, avg_english_scores, label='English', color='#FAD7A0', marker='s', linestyle='-')
ax2.plot(years, avg_history_scores, label='History', color='#D4E6F1', marker='*', linestyle='-.')
ax2.plot(years, avg_art_scores, label='Art', color='#D5DBDB', marker='^', linestyle='-')
ax2.plot(years, avg_pe_scores, label='PE', color='#F9E79F', marker='o', linestyle='--')

ax2.set_title('Improvement Over Time: Average in Scores\nVarious Subjects for', fontsize=14, fontweight='bold')
ax2.set_xlabel('Years', fontsize=12)
ax2.set_ylabel('Scores Average', fontsize=12)
ax2.legend(loc='lower right', fontsize=10)
ax2.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax2.grid(False)

subjects = ['History', 'PE', 'Math', 'Science', 'English', 'Art']
test_scores = [history_scores, pe_scores, math_scores, science_scores, english_scores, art_scores]
box_colors = ['#D4E6F1', '#7DCEA0', '#FAD7A0', '#D5DBDB', '#BB8FCE', '#F9E79F']

box = ax1.boxplot(test_scores, vert=False, patch_artist=True,
                  boxprops=dict(color='grey'),
                  whiskerprops=dict(color='black'),
                  capprops=dict(color='black'),
                  flierprops=dict(marker='x', color='black', alpha=0.5),
                  medianprops=dict(color='green'))

for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)

ax1.set_yticklabels(subjects)
ax1.set_title('Across Subjects: Test Scores of Distribution\nEntrance Exams for College', fontsize=14, fontweight='bold')
ax1.set_xlabel('Scores Test', fontsize=12)
ax1.set_ylabel('Labels Subject', fontsize=12)
ax1.xaxis.grid(True, linestyle=':', which='major', color='blue', alpha=0.7)

plt.tight_layout()
plt.show()