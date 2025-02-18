import matplotlib.pyplot as plt
import numpy as np

tasks = ['Emails', 'Meetings', 'Coding', 'Lunch', 'Breaks', 'Project Planning', 'Review', 'Training Sessions']
hours_data = [2.5, 2, 4, 1, 1, 1.5, 0.5, 2]

incremental_hours = np.cumsum(hours_data)

day_stages = ['Launch', 'Messages', 'Gatherings', 'Programming', 'Snack Time', 'Pause', 'Blueprint Making', 'Assessment', 'Learning']

time_points = [0] + incremental_hours.tolist()

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(day_stages, time_points, marker='o', linestyle='-', linewidth=2, color='teal', label='Duration Taken')

for i, txt in enumerate(time_points[1:]):
    ax.annotate(f'{txt:.1f} hrs', (day_stages[i + 1], time_points[i + 1]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='teal')

ax.grid(True, linestyle='--', linewidth=0.5)

plt.xticks(rotation=45, ha='right')
plt.yticks(np.arange(0, 14, 1))
plt.xlabel('Remote Work Day Phases')
plt.ylabel('Accumulated Time (Hours)')
plt.title('The Course of a Remote Work Day:\nDuration in Different Tasks')
plt.legend(title='Activities')

plt.tight_layout()

plt.show()