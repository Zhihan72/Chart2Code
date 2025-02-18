import matplotlib.pyplot as plt
import numpy as np

subjects = ['Mathematics', 'Science', 'English', 'History', 'Physical Education', 'Arts', 'Computer Science', 'Music']
study_hours = [8, 6, 5, 4, 3, 2, 7, 4]
average_grades = [85, 78, 88, 80, 90, 95, 85, 82]

# Using a single consistent color for all data groups
single_color = '#66B3FF'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.barh(subjects, study_hours, color=single_color, edgecolor='green', linestyle='dotted')
ax1.set_xlim(0, max(study_hours) + 2)
ax1.xaxis.grid(True)

for idx, value in enumerate(study_hours):
    ax1.text(value + 0.3, idx, f'{value}h', va='center', fontsize=10)

ax2.barh(subjects, average_grades, color=single_color, edgecolor='purple', linestyle='dashdot')
ax2.set_xlim(0, 100)

for idx, value in enumerate(average_grades):
    ax2.text(value + 1.5, idx, f'{value}', va='center', fontsize=10)

plt.tight_layout()
plt.show()