import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Art', 'Physical Education', 'Computer Science']
student_A_grades = [85, 89, 92, 88, 76, 79, 91, 84, 90, 89]
student_B_grades = [78, 81, 83, 87, 90, 92, 88, 85, 82, 84]
student_C_grades = [88, 85, 80, 82, 84, 83, 81, 79, 78, 80]
student_D_grades = [90, 88, 86, 84, 85, 89, 87, 81, 83, 86]

fig, ax = plt.subplots(figsize=(14, 8))

# Alter marker shapes, line styles, and colors
ax.plot(subjects, student_A_grades, marker='v', linestyle=':', color='orange', label='Student A')
ax.plot(subjects, student_B_grades, marker='p', linestyle='--', color='darkred', label='Student B')
ax.plot(subjects, student_C_grades, marker='*', linestyle='-', color='cyan', label='Student C')
ax.plot(subjects, student_D_grades, marker='x', linestyle='-.', color='purple', label='Student D')

ax.set_title('Comparative Analysis of Students\' Grades Across Subjects in 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Subjects', fontsize=14)
ax.set_ylabel('Grades', fontsize=14)

# Alter legend properties
ax.legend(title='Student Grades', fontsize=10, title_fontsize=12, loc='upper right')

# Alter grid style
ax.grid(True, linestyle=':', linewidth=1.2, alpha=0.7)

# Add border with altered color and width
for spine in ax.spines.values():
    spine.set_edgecolor('grey')
    spine.set_linewidth(1.1)

ax.annotate('Highest Grade\nStudent A', xy=('Chemistry', 92), xytext=('Chemistry', 95), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)
ax.annotate('Consistent Improvements\nStudent B', xy=('History', 90), xytext=('History', 93), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)
ax.annotate('Declining Trend\nStudent C', xy=('Computer Science', 80), xytext=('Computer Science', 84), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)

plt.tight_layout()
plt.show()