import matplotlib.pyplot as plt
import numpy as np

professions = ['Office Workers', 'Physical Laborers', 'Students']

office_worker_hours = [
    [3, 4, 2, 3, 2, 3, 1],
    [4, 3, 2, 2, 3, 3, 3],
    [2, 1, 3, 2, 2, 2, 1],
    [4, 3, 3, 4, 5, 2, 4]
]

physical_laborer_hours = [
    [8, 7, 9, 8, 8, 7, 7],
    [7, 6, 7, 8, 6, 7, 7],
    [8, 7, 8, 7, 7, 7, 7],
    [8, 9, 8, 7, 8, 8, 7]
]

student_hours = [
    [3, 4, 6, 5, 4, 5, 4],
    [5, 4, 4, 6, 5, 5, 4],
    [4, 3, 4, 4, 4, 4, 3],
    [5, 5, 4, 5, 4, 4, 5]
]

data = [office_worker_hours, physical_laborer_hours, student_hours]

fig, ax = plt.subplots(figsize=(14, 8))
single_color = '#8c66ff'
positions = np.arange(len(data[0])) * (len(professions) + 1) 

for i, hours in enumerate(data):
    pos = positions + i
    bp = ax.boxplot(hours, positions=pos, widths=0.6, patch_artist=True, vert=False)

    for patch in bp['boxes']:
        patch.set_facecolor(single_color)
    for whisker in bp['whiskers']:
        whisker.set(color='lightgray', linewidth=1)
    for cap in bp['caps']:
        cap.set(color='lightgray', linewidth=1)
    for median in bp['medians']:
        median.set(color='blue', linestyle='--', linewidth=2)

yticks = positions + 1
ax.set_yticks(yticks)
ax.set_yticklabels([f"Week {i+1}" for i in range(len(data[0]))], fontsize=12)

ax.set_title("Weekly Workout Hours", fontsize=16, fontweight='bold')
ax.set_xlabel("Hours", fontsize=14)
ax.set_ylabel("Weeks", fontsize=14)

ax.grid(axis='x', linestyle='-.', alpha=0.5)
ax.xaxis.set_tick_params(width=1.5)

plt.tight_layout()
plt.show()