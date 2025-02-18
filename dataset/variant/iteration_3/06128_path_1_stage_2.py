import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Art', 'Physical Education', 'Computer Science']
student_A_grades = [85, 89, 92, 88, 76, 79, 91, 84, 90, 89]
student_B_grades = [78, 81, 83, 87, 90, 92, 88, 85, 82, 84]
student_C_grades = [88, 85, 80, 82, 84, 83, 81, 79, 78, 80]

fig, ax = plt.subplots(figsize=(14, 8))

# Randomly altered stylistic elements
ax.plot(subjects, student_A_grades, marker='x', linestyle='--', color='purple', label='Scholar Alpha')
ax.plot(subjects, student_B_grades, marker='D', linestyle='-', color='orange', label='Learner Beta')
ax.plot(subjects, student_C_grades, marker='v', linestyle=':', color='magenta', label='Pupil Gamma')

ax.set_title('Random Assessment of Scholar\'s Performances in 2023', fontsize=18, fontweight='bold')
ax.set_xlabel('Study Areas', fontsize=15)
ax.set_ylabel('Scores', fontsize=15)

# Altered legend position and style
ax.legend(title='Participants', fontsize=11, title_fontsize=13, loc='upper center')

# Dotted black grid
ax.grid(True, linestyle=':', color='black', alpha=0.7)

# Annotations slightly moved or altered
ax.annotate('Peak Score\nScholar Alpha', xy=('Chemistry', 92), xytext=('Chemistry', 94), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)
ax.annotate('Progressive Pattern\nLearner Beta', xy=('History', 90), xytext=('History', 94), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)
ax.annotate('Fading Pattern\nPupil Gamma', xy=('Computer Science', 80), xytext=('Computer Science', 82), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)

plt.tight_layout()

plt.show()