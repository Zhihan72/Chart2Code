import matplotlib.pyplot as plt
import numpy as np

# Ice cream scores by season
spring_scores = [8.2, 8.9, 9.1, 7.8, 8.7, 9.3, 7.5, 8.5, 8.8, 9.0, 8.3, 7.9]
summer_scores = [6.5, 6.8, 7.0, 6.4, 6.1, 7.2, 6.6, 6.9, 6.7, 7.1, 6.3, 6.0]
autumn_scores = [8.8, 8.1, 8.5, 8.4, 8.7, 9.0, 8.3, 8.6, 8.9, 9.1, 8.2, 8.0]
winter_scores = [7.0, 7.3, 7.5, 7.8, 6.9, 7.4, 7.1, 7.2, 7.6, 7.9, 7.7, 7.0]

scores_data = [spring_scores, summer_scores, autumn_scores, winter_scores]
median_values = [np.median(season) for season in scores_data]
season_labels = ['Spr', 'Sum', 'Aut', 'Win']

fig, ax = plt.subplots(figsize=(12, 8))

bplot = ax.boxplot(scores_data, vert=True, patch_artist=True, labels=season_labels, notch=True,
                   boxprops=dict(facecolor='lightpink', color='purple', linewidth=1.5),
                   whiskerprops=dict(color='purple', linewidth=1.5),
                   capprops=dict(color='purple', linewidth=1.5),
                   medianprops=dict(color='darkred', linewidth=2),
                   flierprops=dict(marker='o', markerfacecolor='red', markersize=6, linestyle='none', markeredgecolor='purple'))

ax.scatter(range(1, 5), median_values, color='blue', s=100, zorder=3, label='Median')

ax.set_title('Ice Cream Scores by Season', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Season', fontsize=12, labelpad=10)
ax.set_ylabel('Scores', fontsize=12, labelpad=10)

ax.text(1, 9.5, 'Spr: High', fontsize=10, color='green', ha='center')
ax.text(2, 7.5, 'Sum: Low', fontsize=10, color='darkred', ha='center')
ax.text(3, 9.5, 'Aut: Great', fontsize=10, color='goldenrod', ha='center')
ax.text(4, 8.3, 'Win: Avg', fontsize=10, color='navy', ha='center')

ax.legend(loc='upper right', fontsize=10)
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.6)

plt.tight_layout()
plt.show()