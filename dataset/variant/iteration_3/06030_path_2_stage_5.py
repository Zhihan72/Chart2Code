import matplotlib.pyplot as plt
import numpy as np

professions = ['Office Workers', 'Physical Laborers', 'Students']

office_worker_hours = [
    [3, 2, 4, 1, 3, 1, 2],
    [2, 3, 5, 2, 3, 3, 2],
    [2, 1, 3, 2, 2, 2, 1],
    [4, 3, 3, 3, 4, 2, 5]
]

physical_laborer_hours = [
    [8, 7, 8, 9, 8, 7, 7],
    [7, 6, 7, 8, 6, 6, 8],
    [8, 7, 7, 7, 7, 8, 6],
    [7, 8, 9, 8, 8, 7, 8]
]

student_hours = [
    [5, 4, 6, 4, 3, 4, 3],
    [4, 5, 5, 4, 5, 5, 6],
    [4, 4, 3, 4, 3, 3, 4],
    [5, 5, 4, 5, 4, 4, 5]
]

data = [office_worker_hours, physical_laborer_hours, student_hours]

fig, ax = plt.subplots(figsize=(14, 8))

positions = np.arange(len(data[0])) * (len(professions) + 1)
colors = ['#ffcc99', '#99ccff', '#ccffcc']

for i, hours in enumerate(data):
    pos = positions + i
    bp = ax.boxplot(hours, positions=pos, widths=0.6, patch_artist=True, vert=False)

    # Alter styles
    for j, patch in enumerate(bp['boxes']):
        patch.set_facecolor(colors[i])
        patch.set_linewidth(2.5) # thicker border
    
    # Alternate marker styles for whiskers and caps
    for j, whisker in enumerate(bp['whiskers']):
        whisker.set(linewidth=1.2, linestyle='-.')
    for j, cap in enumerate(bp['caps']):
        cap.set(linewidth=1.2, linestyle='-.')
    
    # Change median line to a dotted style
    for j, median in enumerate(bp['medians']):
        median.set(color='red', linewidth=1.5, linestyle=':')  

# Adjust tick positions for clarity
tick_positions = positions + (len(professions) - 1) / 2
ax.set_yticks(tick_positions)
ax.set_yticklabels(['Week 1', 'Week 2', 'Week 3', 'Week 4'])

ax.set_xticks([])
ax.set_xlabel('Hours')
ax.set_ylabel('Weeks')

# Randomly modify the grid style
ax.grid(axis='x', linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()