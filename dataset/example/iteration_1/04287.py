import matplotlib.pyplot as plt
import numpy as np

# Define the departments and their respective hours spent on different tasks
departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Support']
tasks = ['Meetings', 'Project Work', 'Emails', 'Training', 'Miscellaneous']

# Task distribution for each department (hours per week)
task_data = np.array([
    [10, 20, 5, 2, 3],  # Engineering
    [8, 15, 10, 3, 4],  # Marketing
    [5, 10, 15, 4, 6],  # Sales
    [6, 5, 8, 10, 6],   # HR
    [7, 10, 7, 3, 8]    # Support
])

# Colors for tasks
colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#C2C2F0']

# Create a figure for the donut pies
fig, axes = plt.subplots(1, len(departments), figsize=(20, 10), subplot_kw=dict(aspect="equal"))

# Plot each department's task distribution as a donut pie chart
for ax, department, task_distribution in zip(axes, departments, task_data):
    wedges, texts, autotexts = ax.pie(task_distribution,
                                      labels=tasks,
                                      colors=colors,
                                      startangle=140,
                                      wedgeprops=dict(width=0.3, edgecolor='w'),
                                      autopct='%1.1f%%',
                                      pctdistance=0.85)
    
    # Customize autotexts
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
    
    # Draw a circle in the middle to make it a donut chart
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(center_circle)
    
    # Title for each subplot
    ax.set_title(department, fontsize=12, pad=15)

# Overall plot title
plt.suptitle("Weekly Task Distribution by Department\nInside The Groovy Corp", 
             fontsize=16, fontweight='bold', y=0.95)

# Add a legend at the bottom
fig.legend(wedges, tasks, title="Tasks", loc='lower center', bbox_to_anchor=(0.5, -0.05), fontsize=10, ncol=len(tasks))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Display the plot
plt.show()