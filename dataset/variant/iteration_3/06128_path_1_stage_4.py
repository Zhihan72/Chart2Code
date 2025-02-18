import matplotlib.pyplot as plt

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Art', 'Physical Education', 'Computer Science']
student_A_grades = [89, 85, 92, 79, 76, 90, 88, 84, 91, 89]  # Randomly altered
student_B_grades = [83, 81, 92, 82, 90, 84, 87, 88, 85, 78]  # Randomly altered
student_C_grades = [81, 80, 85, 79, 84, 78, 82, 88, 80, 83]  # Randomly altered

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(subjects, student_A_grades, marker='x', linestyle='--', color='red', label='Scholar Alpha')
ax.plot(subjects, student_B_grades, marker='D', linestyle='-', color='green', label='Learner Beta')
ax.plot(subjects, student_C_grades, marker='v', linestyle=':', color='blue', label='Pupil Gamma')

ax.set_title('Random Assessment of Scholar\'s Performances in 2023', fontsize=18, fontweight='bold')
ax.set_xlabel('Study Areas', fontsize=15)
ax.set_ylabel('Scores', fontsize=15)

ax.legend(title='Participants', fontsize=11, title_fontsize=13, loc='upper center')

ax.grid(True, linestyle=':', color='black', alpha=0.7)

ax.annotate('Peak Score\nScholar Alpha', xy=('Chemistry', 92), xytext=('Chemistry', 94), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)
ax.annotate('Progressive Pattern\nLearner Beta', xy=('Geography', 92), xytext=('Geography', 96), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)  # Adjusted annotation
ax.annotate('Fading Pattern\nPupil Gamma', xy=('Art', 88), xytext=('Art', 90), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)  # Adjusted annotation

plt.tight_layout()

plt.show()