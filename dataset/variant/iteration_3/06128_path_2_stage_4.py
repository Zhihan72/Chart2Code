import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Phy', 'Chem', 'Bio', 'Hist', 'Geo', 'Eng', 'Art', 'PE', 'CS']
student_A_grades = [85, 89, 92, 88, 76, 79, 91, 84, 90, 89]
student_B_grades = [78, 81, 83, 87, 90, 92, 88, 85, 82, 84]
student_C_grades = [88, 85, 80, 82, 84, 83, 81, 79, 78, 80]
student_D_grades = [90, 88, 86, 84, 85, 89, 87, 81, 83, 86]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(subjects, student_A_grades, marker='v', linestyle=':', color='orange', label='A')
ax.plot(subjects, student_B_grades, marker='p', linestyle='--', color='darkred', label='B')
ax.plot(subjects, student_C_grades, marker='*', linestyle='-', color='cyan', label='C')
ax.plot(subjects, student_D_grades, marker='x', linestyle='-.', color='purple', label='D')

ax.set_title('Grades Analysis 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Subj', fontsize=14)
ax.set_ylabel('Score', fontsize=14)

ax.legend(title='Stu', fontsize=10, title_fontsize=12, loc='upper right')

ax.grid(True, linestyle=':', linewidth=1.2, alpha=0.7)

for spine in ax.spines.values():
    spine.set_edgecolor('grey')
    spine.set_linewidth(1.1)

ax.annotate('Top A', xy=('Chem', 92), xytext=('Chem', 95), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)
ax.annotate('Improved B', xy=('Hist', 90), xytext=('Hist', 93), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)
ax.annotate('Down C', xy=('CS', 80), xytext=('CS', 84), arrowprops=dict(facecolor='grey', shrink=0.05), fontsize=12)

plt.tight_layout()
plt.show()