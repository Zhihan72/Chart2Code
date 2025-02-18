import matplotlib.pyplot as plt
import numpy as np

math_hours = [20, 22, 19, 21, 23, 24, 22, 21, 25, 26, 28, 29, 18, 20, 21]
science_hours = [18, 17, 16, 19, 20, 22, 21, 19, 18, 17, 15, 14, 19, 20, 21]
history_hours = [10, 12, 11, 13, 14, 15, 13, 14, 16, 11, 10, 12, 10, 11, 12]
pe_hours = [5, 6, 7, 6, 8, 9, 7, 6, 5, 4, 5, 6, 6, 7, 8]

study_data = [math_hours, science_hours, history_hours, pe_hours]

subjects = ['Calculation', 'Natural Phenomena', 'Past Events', 'Fitness']

plt.figure(figsize=(12, 7))
bp = plt.boxplot(study_data, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(color='darkgray'),
                 medianprops=dict(color='black', linewidth=2),
                 whiskerprops=dict(color='black', linewidth=1.5),
                 capprops=dict(color='gray', linewidth=1.5),
                 flierprops=dict(marker='o', color='darkorange', markersize=8, linestyle='none', markeredgecolor='darkorange'))

# New color palette for box faces
colors = ['khaki', 'thistle', 'lightcoral', 'lightcyan']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Analysis of Scholarly Engagement Time per Theme\nIn the Adolescent Learning Environment', fontsize=16, fontweight='bold')
plt.ylabel('Engagement Duration (Hours)', fontsize=12)
plt.xlabel('Themes', fontsize=12)

plt.xticks(range(1, len(subjects) + 1), subjects)

means = [np.mean(data_set) for data_set in study_data]
for idx, mean in enumerate(means, start=1):
    plt.scatter(idx, mean, color='purple', zorder=3)
    plt.annotate(f'Mean: {mean:.2f}', xy=(idx, mean), xytext=(idx + 0.1, mean + 0.5),
                 fontsize=9, color='purple', arrowprops=dict(facecolor='purple', arrowstyle='->', lw=1.5))

average_study_time = np.mean([item for sublist in study_data for item in sublist])
plt.axhline(average_study_time, color='darkcyan', linestyle='--', linewidth=1.5)

plt.tight_layout()

plt.show()