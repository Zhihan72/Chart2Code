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
                                      startangle=140,
                                      autopct='%1.1f%%',
                                      pctdistance=0.85)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
    
    ax.set_title(department, fontsize=12, pad=15)

plt.suptitle("Weekly Task Distribution by Department\nInside The Groovy Corp", 
             fontsize=16, fontweight='bold', y=0.95)

fig.legend(wedges, tasks, title="Tasks", loc='lower center', bbox_to_anchor=(0.5, -0.05), fontsize=10, ncol=len(tasks))

plt.tight_layout(rect=[0, 0.05, 1, 0.95])

plt.show()