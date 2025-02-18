import matplotlib.pyplot as plt
import numpy as np

departments = ['Computer Science', 'Mechanical Engineering', 'Biochemistry', 'Psychology', 'Business Administration', 'Fine Arts']
study_hours = [15, 22, 10, 20, 25, 18]
average_gpas = [3.5, 3.4, 3.6, 3.1, 3.8, 3.2]

# Set a single consistent color for all bars
single_bar_color = '#4D7EA8'
line_color = '#FF5733'

fig, ax1 = plt.subplots(figsize=(15, 8))

bars = ax1.barh(departments, study_hours, color=single_bar_color, edgecolor='black')

for bar, hours in zip(bars, study_hours):
    xval = bar.get_width()
    ax1.text(xval + 0.5, bar.get_y() + bar.get_height()/2, str(hours), va='center', ha='left', fontsize=10, fontweight='bold', color='black')

ax2 = ax1.twiny()
ax2.plot(average_gpas, departments, color=line_color, marker='o', linestyle='-', linewidth=2, markersize=7)

ax1.set_title('Weekly Self-Study Hours vs Average GPA\nAcross Different University Departments', fontsize=16, fontweight='bold')
ax1.set_xlabel('Weekly Self-Study Hours', fontsize=12, labelpad=10)
ax2.set_xlabel('Average GPA', fontsize=12, labelpad=10)

ax1.set_xlim(0, 30)
ax2.set_xlim(0, 4.0)

plt.tight_layout()
plt.show()