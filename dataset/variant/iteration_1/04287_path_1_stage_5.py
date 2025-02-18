import matplotlib.pyplot as plt
import numpy as np

departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Support', 'Finance', 'Operations']
tasks = ['Meetings', 'Project Work', 'Emails', 'Training', 'Miscellaneous']

task_data = np.array([
    [10, 20, 5, 2, 3],   # Engineering
    [8, 15, 10, 3, 4],   # Marketing
    [5, 10, 15, 4, 6],   # Sales
    [6, 5, 8, 10, 6],    # HR
    [7, 10, 7, 3, 8],    # Support
    [9, 12, 8, 7, 5],    # Finance (new)
    [10, 8, 6, 5, 12]    # Operations (new)
])

colors = ['#3357FF', '#33FFF0', '#FF5733', '#F033FF', '#33FF57']

fig, axes = plt.subplots(1, len(departments), figsize=(28, 10))

for ax, task_distribution in zip(axes, task_data):
    wedges, _, autotexts = ax.pie(task_distribution,
                                  colors=colors,
                                  startangle=140,
                                  autopct='%1.1f%%',
                                  pctdistance=0.85)

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)

fig.legend(wedges, tasks, title="Tasks", loc='center right', fontsize=12, ncol=1, frameon=True, fancybox=True, shadow=True)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()