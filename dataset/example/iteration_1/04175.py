import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# An education research study explored the number of hours students from different departments
# spend on self-study per week compared to their average GPAs to analyze the relationship between study time and academic performance.

# Departments and their corresponding self-study hours in a week
departments = ['Computer Science', 'Mechanical Engineering', 'Biochemistry', 'Psychology', 'Business Administration', 'Fine Arts']
study_hours = [25, 20, 22, 18, 15, 10]
average_gpas = [3.8, 3.2, 3.4, 3.6, 3.1, 3.5]

# Define color palette for bars and line plot
bar_colors = ['#4D7EA8', '#C46A6A', '#B8A97D', '#ADA3E2', '#7FB3A7', '#E8AE68']
line_color = '#FF5733'

# Create the plot with a bar chart and a line plot
fig, ax1 = plt.subplots(figsize=(15, 8))

# Bar chart for self-study hours
bars = ax1.bar(departments, study_hours, color=bar_colors, edgecolor='black', width=0.6)

# Annotate each bar with the self-study hours
for bar, hours in zip(bars, study_hours):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, str(hours), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Line plot on secondary y-axis for average GPA
ax2 = ax1.twinx()
ax2.plot(departments, average_gpas, color=line_color, marker='o', linestyle='-', linewidth=2, markersize=7, label='Average GPA')

# Titles and labels
ax1.set_title('Weekly Self-Study Hours vs Average GPA\nAcross Different University Departments', fontsize=16, fontweight='bold')
ax1.set_xlabel('Departments', fontsize=12, labelpad=10)
ax1.set_ylabel('Weekly Self-Study Hours', fontsize=12, labelpad=10)
ax2.set_ylabel('Average GPA', fontsize=12, labelpad=10)

# Customize x-axis labels
ax1.set_xticks(np.arange(len(departments)))
ax1.set_xticklabels(departments, rotation=45, ha='right', fontsize=10, fontweight='bold')

# Set limits and grid
ax1.set_ylim(0, 30)
ax2.set_ylim(0, 4.0)
ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Legend for the line plot
ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.9))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()