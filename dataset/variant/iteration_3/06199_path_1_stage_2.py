import matplotlib.pyplot as plt
import numpy as np

subjects = ['Mathematics', 'Science', 'English', 'History', 'Physical Education', 'Arts', 'Computer Science', 'Music']
study_hours = [8, 6, 5, 4, 3, 2, 7, 4]
average_grades = [85, 78, 88, 80, 90, 95, 85, 82]

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#DA70D6', '#8A2BE2', '#FF69B4']
marker_styles = ['o', '^', 's', 'D', 'v', 'x', '*', 'p']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Randomly altered first subplot: Include gridlines and different marker style
ax1.bar(subjects, study_hours, color=colors, edgecolor='green', linestyle='dotted')
ax1.set_title("Average Weekly Study Hours per Subject", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Subjects", fontsize=12)
ax1.set_ylabel("Study Hours", fontsize=12)
ax1.set_ylim(0, max(study_hours) + 2)
ax1.yaxis.grid(True)

for idx, value in enumerate(study_hours):
    ax1.text(idx, value + 0.3, f'{value}h', ha='center', fontsize=10)

# Randomly altered second subplot: Different edge color and remove gridlines
ax2.bar(subjects, average_grades, color=colors, edgecolor='purple', linestyle='dashdot')
ax2.set_title("Average Grades per Subject", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Subjects", fontsize=12)
ax2.set_ylabel("Average Grade", fontsize=12, labelpad=10)
ax2.set_ylim(0, 100)

for idx, value in enumerate(average_grades):
    ax2.text(idx, value + 1.5, f'{value}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()