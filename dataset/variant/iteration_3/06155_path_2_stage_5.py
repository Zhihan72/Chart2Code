import numpy as np
import matplotlib.pyplot as plt

years = ['Year One', 'Year Two', 'Year Three', 'Year Four', 'Year Five', 'Year Six', 'Year Seven', 'Year Eight']

data = {
    'Dance': [50, 60, 65, 70, 90, 100, 110, 120],
    'Meditation': [40, 50, 55, 60, 70, 85, 95, 100],
    'Jogging': [60, 70, 75, 80, 85, 95, 105, 115],
    'Yoga': [30, 45, 50, 55, 60, 70, 80, 90],
    'Swimming': [20, 30, 40, 50, 60, 70, 80, 90]
}

sorted_data = {program: sorted(counts, reverse=True) for program, counts in data.items()}

fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(years))
width = 0.15
colors = ['cyan', 'magenta', 'gold', 'lightgreen', 'orange']

for i, (program, counts) in enumerate(sorted_data.items()):
    ax.bar(x + i * width, counts, width, label=program, color=colors[i], linestyle='-.', edgecolor='black')

ax.set_xlabel('Annual Cycle')
ax.set_ylabel('Enrollees')
ax.set_title('Participation Trends in Health Activities (Sorted)')

ax.set_xticks(x + width * 2)
ax.set_xticklabels(years, rotation=45)

ax.legend(loc='lower right', fontsize='small')
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
fig.tight_layout(pad=2)

plt.show()