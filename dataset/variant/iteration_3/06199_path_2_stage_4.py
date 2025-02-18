import matplotlib.pyplot as plt
import numpy as np

# Updated data by removing 'Physical Education'
subjects = ['Mathematics', 'Science', 'English', 'History', 'Arts', 'Computer Science']
study_hours = [8, 6, 5, 4, 2, 7]
average_grades = [85, 78, 88, 80, 95, 85]

single_color = '#66B3FF'

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.bar(subjects, study_hours, color=single_color)
ax1.set_ylim(0, max(study_hours) + 2)

for idx, value in enumerate(study_hours):
    ax1.text(idx, value + 0.3, f'{value}h', ha='center', fontsize=10, color='black')

ax2.bar(subjects, average_grades, color=single_color)
ax2.set_ylim(0, 100)

for idx, value in enumerate(average_grades):
    ax2.text(idx, value + 1.5, f'{value}', ha='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()