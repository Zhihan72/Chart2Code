import matplotlib.pyplot as plt
import numpy as np

# Data: Altered hours spent on each subject by students over a month
study_data = [
    [23, 21, 24, 20, 19, 28, 26, 25, 21, 18, 22, 22, 29, 21, 20],
    [20, 19, 18, 16, 22, 17, 15, 21, 18, 19, 14, 20, 17, 21, 19],
    [12, 10, 11, 10, 16, 14, 12, 14, 11, 13, 10, 15, 11, 12, 13],
    [9, 8, 13, 10, 13, 11, 7, 14, 13, 12, 11, 8, 9, 15, 10],
    [6, 8, 5, 6, 4, 5, 7, 9, 5, 6, 6, 7, 8, 6, 7]
]

plt.figure(figsize=(12, 7))
bp = plt.boxplot(study_data, vert=False, patch_artist=True, notch=False,
                 boxprops=dict(color='green'),
                 medianprops=dict(color='yellow', linewidth=3),
                 whiskerprops=dict(color='red', linewidth=1),
                 capprops=dict(color='purple', linewidth=2),
                 flierprops=dict(marker='x', color='black', markersize=10, linestyle='none', markeredgecolor='black'))

new_colors = ['steelblue', 'lightpink', 'coral', 'khaki', 'plum']
for patch, color in zip(bp['boxes'], new_colors):
    patch.set_facecolor(color)

plt.grid(axis='x', linestyle='-', alpha=0.5)
average_study_time = np.mean([item for sublist in study_data for item in sublist])
plt.axvline(average_study_time, color='orange', linestyle='-.', linewidth=1)
plt.tight_layout()
plt.show()