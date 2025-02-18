import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart presents a comparative analysis of three fictional students' grades over the academic year in a university. Each student has a different performance trend, showcasing the ups and downs across multiple subjects through the year.

# Data (constructed without random):
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Art', 'Physical Education', 'Computer Science']
student_A_grades = [85, 89, 92, 88, 76, 79, 91, 84, 90, 89]
student_B_grades = [78, 81, 83, 87, 90, 92, 88, 85, 82, 84]
student_C_grades = [88, 85, 80, 82, 84, 83, 81, 79, 78, 80]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each student
ax.plot(subjects, student_A_grades, marker='o', linestyle='-', color='blue', label='Student A')
ax.plot(subjects, student_B_grades, marker='s', linestyle='--', color='green', label='Student B')
ax.plot(subjects, student_C_grades, marker='^', linestyle='-.', color='red', label='Student C')

# Add titles and labels
ax.set_title('Comparative Analysis of Students\' Grades Across Subjects in 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Subjects', fontsize=14)
ax.set_ylabel('Grades', fontsize=14)

# Add legend
ax.legend(title='Students', fontsize=12, title_fontsize=14, loc='lower left')

# Customize grid
ax.grid(True, linestyle='--', alpha=0.5)

# Annotations to highlight key points
ax.annotate('Highest Grade\nStudent A', xy=('Chemistry', 92), xytext=('Chemistry', 95), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
ax.annotate('Consistent Improvements\nStudent B', xy=('History', 90), xytext=('History', 93), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
ax.annotate('Declining Trend\nStudent C', xy=('Computer Science', 80), xytext=('Computer Science', 84), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()