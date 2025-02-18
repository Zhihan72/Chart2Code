import matplotlib.pyplot as plt
import numpy as np

professions = ['Office Workers', 'Physical Laborers', 'Students']

office_worker_hours = [
    [2, 3, 4, 1, 2, 2, 3],
    [3, 2, 4, 3, 3, 2, 3],
    [1, 2, 2, 2, 1, 3, 2],
    [3, 4, 5, 2, 3, 4, 4]
]

physical_laborer_hours = [
    [7, 8, 7, 8, 9, 8, 7],
    [6, 7, 6, 8, 7, 7, 6],
    [7, 7, 8, 7, 8, 7, 7],
    [7, 8, 8, 9, 7, 8, 8]
]

student_hours = [
    [4, 5, 3, 5, 4, 6, 4],
    [5, 4, 5, 5, 4, 6, 5],
    [3, 4, 4, 3, 4, 4, 3],
    [4, 5, 5, 4, 5, 5, 4]
]

data = [office_worker_hours, physical_laborer_hours, student_hours]

fig, ax = plt.subplots(figsize=(14, 8))

positions = np.arange(len(data[0])) * (len(professions) + 1)

# New set of colors
colors = ['#ffcc99', '#99ccff', '#ccffcc']

for i, hours in enumerate(data):
    pos = positions + i
    bp = ax.boxplot(hours, positions=pos, widths=0.6, patch_artist=True, vert=False)

    for patch in bp['boxes']:
        patch.set_facecolor(colors[i])
    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1.5)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1.5)
    for median in bp['medians']:
        median.set(color='black', linewidth=2)

tick_positions = positions + (len(professions) - 1) / 2
ax.set_yticks(tick_positions)
ax.set_yticklabels(['Week 1', 'Week 2', 'Week 3', 'Week 4'])

ax.set_xticks([])
ax.set_xlabel('Hours')
ax.set_ylabel('Weeks')

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()