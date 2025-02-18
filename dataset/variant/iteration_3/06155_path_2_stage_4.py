import numpy as np
import matplotlib.pyplot as plt

years = ['Year One', 'Year Two', 'Year Three', 'Year Four', 'Year Five', 'Year Six', 'Year Seven', 'Year Eight']

data = {
    'Dance': [50, 60, 65, 70, 90, 100, 110, 120],
    'Meditation': [40, 50, 55, 60, 70, 85, 95, 100],
    'Jogging': [60, 70, 75, 80, 85, 95, 105, 115]
}

# Sort the data for each activity in descending order for demonstration
sorted_data = {program: sorted(counts, reverse=True) for program, counts in data.items()}

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years))
width = 0.25
colors = ['cyan', 'magenta', 'gold']

# Plot each program's data as a sorted bar chart
for i, (program, counts) in enumerate(sorted_data.items()):
    ax.bar(x + i * width, counts, width, label=program, color=colors[i], linestyle='-.', edgecolor='black')

ax.set_xlabel('Annual Cycle')
ax.set_ylabel('Enrollees')
ax.set_title('Participation Trends in Health Activities (Sorted)')

ax.set_xticks(x + width)
ax.set_xticklabels(years, rotation=45)

# Updating legend placement
ax.legend(loc='lower right', fontsize='small')

# Adding grid
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)

fig.tight_layout(pad=2)

plt.show()