import matplotlib.pyplot as plt
import numpy as np

# Define the data
subjects = ['Mathematics', 'Science', 'English', 'History', 'Physical Education', 'Arts', 'Computer Science']
study_hours = [8, 6, 5, 4, 3, 2, 7]
average_grades = [85, 78, 88, 80, 90, 95, 85]

# Single color for all bars
single_color = '#66B3FF'

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# First subplot: Bar chart for study hours
ax1.bar(subjects, study_hours, color=single_color, edgecolor='black')
ax1.set_title("Average Weekly Study Hours per Subject", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Subjects", fontsize=12)
ax1.set_ylabel("Study Hours", fontsize=12)
ax1.set_ylim(0, max(study_hours) + 2)

# Display study hours values on top of the bars
for idx, value in enumerate(study_hours):
    ax1.text(idx, value + 0.3, f'{value}h', ha='center', fontsize=10, color='black')

# Second subplot: Bar chart for average grades
ax2.bar(subjects, average_grades, color=single_color, edgecolor='black')
ax2.set_title("Average Grades per Subject", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Subjects", fontsize=12)
ax2.set_ylabel("Average Grade", fontsize=12)
ax2.set_ylim(0, 100)

# Display average grade values on top of the bars
for idx, value in enumerate(average_grades):
    ax2.text(idx, value + 1.5, f'{value}', ha='center', fontsize=10, color='black')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()