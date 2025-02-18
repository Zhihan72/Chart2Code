import matplotlib.pyplot as plt
import numpy as np

# Define weekly workout hours data for each profession over four weeks
professions = ['Office Workers', 'Physical Laborers', 'Students']

office_worker_hours = [
    [2, 3, 4, 1, 2, 2, 3],  # Week 1
    [3, 2, 4, 3, 3, 2, 3],  # Week 2
    [1, 2, 2, 2, 1, 3, 2],  # Week 3
    [3, 4, 5, 2, 3, 4, 4]   # Week 4
]

physical_laborer_hours = [
    [7, 8, 7, 8, 9, 8, 7],  # Week 1
    [6, 7, 6, 8, 7, 7, 6],  # Week 2
    [7, 7, 8, 7, 8, 7, 7],  # Week 3
    [7, 8, 8, 9, 7, 8, 8]   # Week 4
]

student_hours = [
    [4, 5, 3, 5, 4, 6, 4],  # Week 1
    [5, 4, 5, 5, 4, 6, 5],  # Week 2
    [3, 4, 4, 3, 4, 4, 3],  # Week 3
    [4, 5, 5, 4, 5, 5, 4]   # Week 4
]

# Aggregate the data
data = [office_worker_hours, physical_laborer_hours, student_hours]

# Plot configuration
fig, ax = plt.subplots(figsize=(14, 8))

# Create a box plot for each profession
positions = np.arange(len(data[0])) * (len(professions) + 1)  # Offset for each week
colors = ['#ff9999', '#66b3ff', '#99ff99']  # Colors for each profession

for i, hours in enumerate(data):
    pos = positions + i  # Offset positions for each profession
    bp = ax.boxplot(hours, positions=pos, widths=0.6, patch_artist=True)

    # Color each box according to its profession
    for patch in bp['boxes']:
        patch.set_facecolor(colors[i])
    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1.5)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1.5)
    for median in bp['medians']:
        median.set(color='black', linewidth=2)

# Set x-ticks to align with the weeks
xticks = positions + 1  # Align ticks to the center of each profession group
ax.set_xticks(xticks)
ax.set_xticklabels([f"Week {i+1}" for i in range(len(data[0]))], fontsize=12)

# Labels and Title
ax.set_title("Weekly Workout Hours Comparison Among Professions:\nInsights into Physical Activity Levels", fontsize=16, fontweight='bold')
ax.set_ylabel("Weekly Workout Hours", fontsize=14)
ax.set_xlabel("Weeks", fontsize=14)

# Grid customization
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Legend indicating profession colors
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, professions, title='Professions', loc='upper right', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()