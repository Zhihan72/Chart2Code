import matplotlib.pyplot as plt
import numpy as np

departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Support']
tasks = ['Meetings', 'Project Work', 'Emails', 'Training', 'Miscellaneous']

# Randomly altered task data while preserving the original dimensional structure
task_data = np.array([
    [3, 5, 20, 10, 2],
    [10, 8, 4, 15, 3],
    [15, 10, 6, 5, 4],
    [8, 6, 5, 6, 10],
    [7, 7, 8, 3, 10]
])

colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#C2C2F0']

fig, axes = plt.subplots(1, len(departments), figsize=(20, 10), subplot_kw=dict(aspect="equal"))

for ax, department, task_distribution in zip(axes, departments, task_data):
    wedges, texts, autotexts = ax.pie(task_distribution,
                                      labels=tasks,
                                      colors=colors,
                                      startangle=100,
                                      autopct='%1.1f%%',
                                      shadow=True,
                                      )
    
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(10)
    
    ax.set_title(department, fontsize=14, pad=20)

plt.suptitle("Weekly Task Distribution by Department", 
             fontsize=18, fontweight='bold', y=0.95)

fig.legend(wedges, tasks, title="Tasks Completed", loc='center left', bbox_to_anchor=(0.9, 0.5), fontsize=11, ncol=1)

plt.grid(False)
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

plt.show()