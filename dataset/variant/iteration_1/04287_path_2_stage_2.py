import matplotlib.pyplot as plt
import numpy as np

departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Support']
tasks = ['Meetings', 'Project Work', 'Emails', 'Training', 'Miscellaneous']

task_data = np.array([
    [10, 20, 5, 2, 3],
    [8, 15, 10, 3, 4],
    [5, 10, 15, 4, 6],
    [6, 5, 8, 10, 6],
    [7, 10, 7, 3, 8]
])

colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#C2C2F0']

fig, axes = plt.subplots(1, len(departments), figsize=(20, 10), subplot_kw=dict(aspect="equal"))

for ax, department, task_distribution in zip(axes, departments, task_data):
    wedges, texts, autotexts = ax.pie(task_distribution,
                                      labels=tasks,
                                      colors=colors,
                                      startangle=100,  # Changed start angle
                                      autopct='%1.1f%%',  # Same auto percentage
                                      shadow=True,  # Added shadows to each pie
                                      )
    
    for autotext in autotexts:
        autotext.set_color('black')  # Changed text color to black
        autotext.set_fontsize(10)    # Changed font size
    
    ax.set_title(department, fontsize=14, pad=20)  # Enlarged title size and padding

plt.suptitle("Weekly Task Distribution by Department", 
             fontsize=18, fontweight='bold', y=0.95)

fig.legend(wedges, tasks, title="Tasks Completed", loc='center left', bbox_to_anchor=(0.9, 0.5), fontsize=11, ncol=1)

plt.grid(False)
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

plt.show()