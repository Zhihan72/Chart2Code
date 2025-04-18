import matplotlib.pyplot as plt
import numpy as np

# Define weekly workout hours data for each profession over four weeks
professions = ['Office Workers', 'Physical Laborers', 'Students']

office_worker_hours = [
    [3, 4, 2, 3, 2, 3, 1],  # Week 1: Randomly altered order
    [4, 3, 2, 2, 3, 3, 3],  # Week 2: Randomly altered order
    [2, 1, 3, 2, 2, 2, 1],  # Week 3: Randomly altered order
    [4, 3, 3, 4, 5, 2, 4]   # Week 4: Randomly altered order
]

physical_laborer_hours = [
    [8, 7, 9, 8, 8, 7, 7],  # Week 1: Randomly altered order
    [7, 6, 7, 8, 6, 7, 7],  # Week 2: Randomly altered order
    [8, 7, 8, 7, 7, 7, 7],  # Week 3: Randomly altered order
    [8, 9, 8, 7, 8, 8, 7]   # Week 4: Randomly altered order
]

student_hours = [
    [3, 4, 6, 5, 4, 5, 4],  # Week 1: Randomly altered order
    [5, 4, 4, 6, 5, 5, 4],  # Week 2: Randomly altered order
    [4, 3, 4, 4, 4, 4, 3],  # Week 3: Randomly altered order
    [5, 5, 4, 5, 4, 4, 5]   # Week 4: Randomly altered order
]

# Aggregate the data
data = [office_worker_hours, physical_laborer_hours, student_hours]

fig, ax = plt.subplots(figsize=(14, 8))
single_color = '#66b3ff'
positions = np.arange(len(data[0])) * (len(professions) + 1)

for i, hours in enumerate(data):
    pos = positions + i
    bp = ax.boxplot(hours, positions=pos, widths=0.6, patch_artist=True)

    for patch in bp['boxes']:
        patch.set_facecolor(single_color)
    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1.5)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1.5)
    for median in bp['medians']:
        median.set(color='black', linewidth=2)

xticks = positions + 1
ax.set_xticks(xticks)
ax.set_xticklabels([f"Week {i+1}" for i in range(len(data[0]))], fontsize=12)

ax.set_title("Weekly Workout Hours Comparison Among Professions:\nInsights into Physical Activity Levels", fontsize=16, fontweight='bold')
ax.set_ylabel("Weekly Workout Hours", fontsize=14)
ax.set_xlabel("Weeks", fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)

ax.legend([plt.Line2D([0], [0], color=single_color, lw=4)], ['Professions'], title='Color Key', loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()