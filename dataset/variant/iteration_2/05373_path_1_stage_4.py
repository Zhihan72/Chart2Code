import matplotlib.pyplot as plt
import numpy as np

tasks = ['Lunchtime', 'Email Check', 'Developing', 'Snack Break', 'Prep Meeting', 'Strategy Session']
hours_data = [1.5, 2, 3.5, 0.5, 2, 1.5]

incremental_hours = np.cumsum(hours_data)

day_stages = ['Begin Day', 'Lunchtime', 'Email Check', 'Developing', 'Snack Break', 'Prep Meeting', 'Strategy Session']
time_points = [0] + incremental_hours.tolist()

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(day_stages, time_points, marker='x', linestyle='--', linewidth=2, color='green', label='Effort Distribution')

for i, txt in enumerate(time_points[1:]):
    ax.annotate(f'{txt:.1f} hrs', (day_stages[i + 1], time_points[i + 1]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='green')

ax.grid(True, linestyle='-.', linewidth=0.7)

plt.xticks(rotation=30, ha='right')
plt.yticks(np.arange(0, 13, 1))
plt.xlabel('Remote Work Schedule')
plt.ylabel('Accumulated Time (Hours)')
plt.title('Overview of a Remote Day:\nTime Allocated to Different Activities')
plt.legend(title='Activity Categories', loc='upper left', frameon=False)

plt.tight_layout()
plt.show()