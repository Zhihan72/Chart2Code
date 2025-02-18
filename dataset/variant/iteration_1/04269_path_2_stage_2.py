import matplotlib.pyplot as plt
import numpy as np

# Data: Hours spent on each subject by students over a month
study_data = [
    [20, 22, 19, 21, 23, 24, 22, 21, 25, 26, 28, 29, 18, 20, 21],
    [18, 17, 16, 19, 20, 22, 21, 19, 18, 17, 15, 14, 19, 20, 21],
    [10, 12, 11, 13, 14, 15, 13, 14, 16, 11, 10, 12, 10, 11, 12],
    [8, 9, 7, 10, 12, 15, 14, 11, 13, 13, 11, 9, 8, 10, 13],
    [5, 6, 7, 6, 8, 9, 7, 6, 5, 4, 5, 6, 6, 7, 8]
]

subjects = ['Math', 'Science', 'History', 'Art', 'Physical Education']

# Create the horizontal box plot
plt.figure(figsize=(12, 7))
bp = plt.boxplot(study_data, vert=False, patch_artist=True, notch=False,
                 boxprops=dict(color='green'),
                 medianprops=dict(color='yellow', linewidth=3),
                 whiskerprops=dict(color='red', linewidth=1),
                 capprops=dict(color='purple', linewidth=2),
                 flierprops=dict(marker='x', color='black', markersize=10, linestyle='none', markeredgecolor='black'))

# Colors for each subject
colors = ['seagreen', 'lightcoral', 'deepskyblue', 'orange', 'limegreen']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
plt.title('Monthly Study Hours Analysis Per Subject\nAmong Students', fontsize=14, fontweight='normal')
plt.ylabel('Subjects', fontsize=14)
plt.xlabel('Study Hours', fontsize=10)

# Set y-tick labels
plt.yticks(range(1, len(subjects) + 1), subjects)

# Alter gridlines
plt.grid(axis='x', linestyle='-', alpha=0.5)

# Change reference line style
average_study_time = np.mean([item for sublist in study_data for item in sublist])
plt.axvline(average_study_time, color='orange', linestyle='-.', linewidth=1, label=f'Mean: {average_study_time:.2f} hrs')

# Adjust layout to avoid overlap
plt.tight_layout()

# Remove legend for cleaner look
# Display the plot
plt.show()