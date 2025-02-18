import matplotlib.pyplot as plt
import numpy as np

# Data: Hours spent on each subject by students over a month
study_data = [
    [20, 22, 19, 21, 23, 24, 22, 21, 25, 26, 28, 29, 18, 20, 21],  # Math
    [18, 17, 16, 19, 20, 22, 21, 19, 18, 17, 15, 14, 19, 20, 21],  # Science
    [10, 12, 11, 13, 14, 15, 13, 14, 16, 11, 10, 12, 10, 11, 12],  # History
    [8, 9, 7, 10, 12, 15, 14, 11, 13, 13, 11, 9, 8, 10, 13],       # Art
    [5, 6, 7, 6, 8, 9, 7, 6, 5, 4, 5, 6, 6, 7, 8]                  # Physical Education
]

subjects = ['Math', 'Science', 'History', 'Art', 'Physical Education']

# Create the horizontal box plot
plt.figure(figsize=(12, 7))
bp = plt.boxplot(study_data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(color='blue'),
                 medianprops=dict(color='red', linewidth=2),
                 whiskerprops=dict(color='black', linewidth=1.5),
                 capprops=dict(color='darkblue', linewidth=1.5),
                 flierprops=dict(marker='o', color='orange', markersize=8, linestyle='none', markeredgecolor='orange'))

# Colors for each subject
colors = ['lavender', 'lightgreen', 'lightblue', 'pink', 'lightgoldenrodyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
plt.title('Monthly Study Hours Analysis Per Subject\nAmong High School Students', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Subjects', fontsize=12)

# Set y-tick labels
plt.yticks(range(1, len(subjects) + 1), subjects)

# Add gridlines for readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add a reference line for the average study time
average_study_time = np.mean([item for sublist in study_data for item in sublist])
plt.axvline(average_study_time, color='blue', linestyle='--', linewidth=1.5, label=f'Overall Average: {average_study_time:.2f} hrs')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()