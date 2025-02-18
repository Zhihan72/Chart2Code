import matplotlib.pyplot as plt
import numpy as np

# Subjects and corresponding data
subjects = ['History', 'Mathematics', 'Arts', 'Computer Science', 'Science', 'English']
study_hours = [4, 8, 2, 7, 6, 5]  # Manually shuffled hours to reflect new order
average_grades = [80, 85, 95, 85, 78, 88]  # Manually shuffled grades

single_color = '#66B3FF'

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.bar(subjects, study_hours, color=single_color)
ax1.set_ylim(0, max(study_hours) + 2)

for idx, value in enumerate(study_hours):
    ax1.text(idx, value + 0.3, f'{value} hours', ha='center', fontsize=10, color='black')  # Altered label suffix

ax2.bar(subjects, average_grades, color=single_color)
ax2.set_ylim(0, 100)

for idx, value in enumerate(average_grades):
    ax2.text(idx, value + 1.5, f'Score: {value}', ha='center', fontsize=10, color='black')  # Altered label prefix

# Manually altered titles and labels
ax1.set_title('Weekly Study Hours by Subject')
ax1.set_xlabel('Subjects')
ax1.set_ylabel('Hours Spent')

ax2.set_title('Average Grades by Subject')
ax2.set_xlabel('Subjects')
ax2.set_ylabel('Grades')

plt.tight_layout()
plt.show()