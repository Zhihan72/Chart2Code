import matplotlib.pyplot as plt
import numpy as np

tasks = ['Breaks', 'Coding', 'Emails', 'Lunch', 'Project Planning', 'Meetings']
hours_data = [1, 4, 2.5, 1, 1.5, 2]

incremental_hours = np.cumsum(hours_data)

day_stages = ['Start', 'Breaks', 'Coding', 'Emails', 'Lunch', 'Project Planning', 'Meetings']
time_points = [0] + incremental_hours.tolist()

fig, ax = plt.subplots(figsize=(14, 8))

# Assigned a new color to the line and the annotations
ax.plot(day_stages, time_points, marker='o', linestyle='-', linewidth=2, color='purple', label='Time Spent')

for i, txt in enumerate(time_points[1:]):
    ax.annotate(f'{txt:.1f} hrs', (day_stages[i + 1], time_points[i + 1]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='purple')

ax.grid(True, linestyle='--', linewidth=0.5)

plt.xticks(rotation=45, ha='right')
plt.yticks(np.arange(0, 13, 1))
plt.xlabel('Work-from-Home Day Stages')
plt.ylabel('Cumulative Time Spent (Hours)')
plt.title('The Flow of a Work-from-Home Day:\nTime Spent on Various Tasks')
plt.legend(title='Tasks')

plt.tight_layout()
plt.show()