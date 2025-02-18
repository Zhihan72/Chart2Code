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

plt.figure(figsize=(12, 7))
bp = plt.boxplot(study_data, vert=False, patch_artist=True, notch=False,
                 boxprops=dict(color='green'),
                 medianprops=dict(color='yellow', linewidth=3),
                 whiskerprops=dict(color='red', linewidth=1),
                 capprops=dict(color='purple', linewidth=2),
                 flierprops=dict(marker='x', color='black', markersize=10, linestyle='none', markeredgecolor='black'))

# New colors for each subject
new_colors = ['steelblue', 'lightpink', 'coral', 'khaki', 'plum']
for patch, color in zip(bp['boxes'], new_colors):
    patch.set_facecolor(color)

plt.grid(axis='x', linestyle='-', alpha=0.5)
average_study_time = np.mean([item for sublist in study_data for item in sublist])
plt.axvline(average_study_time, color='orange', linestyle='-.', linewidth=1)
plt.tight_layout()
plt.show()