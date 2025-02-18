import matplotlib.pyplot as plt
import numpy as np

departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Support']
tasks = ['Meetings', 'Project Work', 'Emails', 'Training', 'Miscellaneous']

task_data = np.array([
    [10, 20, 5, 2, 3],  # Engineering
    [8, 15, 10, 3, 4],  # Marketing
    [5, 10, 15, 4, 6],  # Sales
    [6, 5, 8, 10, 6],   # HR
    [7, 10, 7, 3, 8]    # Support
])

# Shuffled colors for each data group
colors = ['#3357FF', '#33FFF0', '#FF5733', '#F033FF', '#33FF57']

fig, axes = plt.subplots(1, len(departments), figsize=(20, 10), subplot_kw=dict(aspect="equal"))

for ax, task_distribution in zip(axes, task_data):
    wedges, _, autotexts = ax.pie(task_distribution,
                                  colors=colors,
                                  startangle=140,
                                  wedgeprops=dict(width=0.3, edgecolor='black', linestyle='-.'),
                                  autopct='%1.1f%%',
                                  pctdistance=0.85)

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)

    center_circle = plt.Circle((0, 0), 0.70, fc='lightgrey')
    ax.add_artist(center_circle)
    ax.set_facecolor('#f5f5f5')

fig.legend(wedges, tasks, title="Tasks", loc='center right', fontsize=12, ncol=1, frameon=True, fancybox=True, shadow=True)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()