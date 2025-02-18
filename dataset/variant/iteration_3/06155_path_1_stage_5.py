import numpy as np
import matplotlib.pyplot as plt

years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

data = {
    'Aerobics Plus': [90, 70, 120, 130, 50, 65, 100, 110],
    'Meditation': [80, 60, 100, 110, 40, 55, 85, 95],
    'DanceFitness': [110, 80, 130, 135, 60, 75, 95, 105]
}

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['cyan', 'yellow', 'magenta']

# Sort each program data in ascending order
sorted_data = {program: sorted(counts) for program, counts in data.items()}

# Calculate bar positions
x = np.arange(len(years)) * 1.5
width = 0.25

for i, (program, sorted_counts) in enumerate(sorted_data.items()):
    ax.bar(x + i * width, sorted_counts, width, color=colors[i], label=program)

ax.set_xlabel('Chronicles of Time')
ax.set_ylabel('Enthusiasts')
ax.set_title('Transformational Effects of Wellness Projects (Ordered)')
ax.set_xticks(x + width)
ax.set_xticklabels(years)

fig.legend(loc='upper right', ncol=1, bbox_to_anchor=(0.85, 0.95))
ax.grid(True, which='major', linestyle='-')

fig.tight_layout(pad=3)

plt.show()