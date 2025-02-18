import matplotlib.pyplot as plt
import numpy as np

# Departments, self-study hours, and average GPAs
departments = ['Computer Science', 'Mechanical Engineering', 'Biochemistry', 'Psychology', 'Business Administration', 'Fine Arts']
study_hours = [25, 20, 22, 18, 15, 10]
average_gpas = [3.8, 3.2, 3.4, 3.6, 3.1, 3.5]

# Define color palette for bars and line plot
bar_colors = ['#4D7EA8', '#C46A6A', '#B8A97D', '#ADA3E2', '#7FB3A7', '#E8AE68']
line_color = '#FF5733'

# Create the plot with a horizontal bar chart and a line plot
fig, ax1 = plt.subplots(figsize=(15, 8))

# Horizontal bar chart for self-study hours
bars = ax1.barh(departments, study_hours, color=bar_colors, edgecolor='black')

# Annotate each bar with the self-study hours
for bar, hours in zip(bars, study_hours):
    xval = bar.get_width()
    ax1.text(xval + 0.5, bar.get_y() + bar.get_height()/2, str(hours), va='center', ha='left', fontsize=10, fontweight='bold', color='black')

# Line plot on secondary axis for average GPA
ax2 = ax1.twiny()
ax2.plot(average_gpas, departments, color=line_color, marker='o', linestyle='-', linewidth=2, markersize=7, label='Average GPA')

# Titles and labels
ax1.set_title('Weekly Self-Study Hours vs Average GPA\nAcross Different University Departments', fontsize=16, fontweight='bold')
ax1.set_xlabel('Weekly Self-Study Hours', fontsize=12, labelpad=10)
ax2.set_xlabel('Average GPA', fontsize=12, labelpad=10)

# Set limits and grid
ax1.set_xlim(0, 30)
ax2.set_xlim(0, 4.0)
ax1.grid(True, which='both', axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Legend for the line plot
ax2.legend(loc='lower right', bbox_to_anchor=(1, 0.1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()