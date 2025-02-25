import matplotlib.pyplot as plt
import numpy as np

spring_scores = [8.2, 8.9, 9.1, 7.8, 8.7, 9.3, 7.5, 8.5, 8.8, 9.0, 8.3, 7.9]
summer_scores = [6.5, 6.8, 7.0, 6.4, 6.1, 7.2, 6.6, 6.9, 6.7, 7.1, 6.3, 6.0]
autumn_scores = [8.8, 8.1, 8.5, 8.4, 8.7, 9.0, 8.3, 8.6, 8.9, 9.1, 8.2, 8.0]
winter_scores = [7.0, 7.3, 7.5, 7.8, 6.9, 7.4, 7.1, 7.2, 7.6, 7.9, 7.7, 7.0]
monsoon_scores = [7.5, 7.8, 8.1, 7.0, 7.3, 8.0, 7.4, 7.6, 7.7, 8.2, 8.3, 7.9]
dry_scores = [6.8, 6.5, 6.1, 6.4, 6.6, 7.0, 6.3, 6.2, 6.9, 6.7, 6.0, 6.8]

scores_data = [spring_scores, summer_scores, autumn_scores, winter_scores, monsoon_scores, dry_scores]
median_values = [np.median(season) for season in scores_data]
season_labels = ['Spr', 'Sum', 'Aut', 'Win', 'Mon', 'Dry']

fig, ax = plt.subplots(figsize=(12, 8))

bplot = ax.boxplot(scores_data, vert=True, patch_artist=True, labels=season_labels, notch=True,
                   boxprops=dict(facecolor='lightblue', color='darkgreen', linewidth=1.5),
                   whiskerprops=dict(color='darkgreen', linewidth=1.5),
                   capprops=dict(color='darkgreen', linewidth=2),
                   medianprops=dict(color='orange', linewidth=2),
                   flierprops=dict(marker='s', markerfacecolor='magenta', markersize=8, linestyle='none', markeredgecolor='darkgreen'))

ax.scatter(range(1, 7), median_values, color='black', marker='*', s=150, zorder=3, label='Median')

ax.set_title('Ice Cream Taste Tests', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Season', fontsize=12, labelpad=10)
ax.set_ylabel('Scores', fontsize=12, labelpad=10)

ax.text(1, 9.5, 'High', fontsize=10, color='purple', ha='center')
ax.text(2, 7.5, 'Low', fontsize=10, color='red', ha='center')
ax.text(3, 9.5, 'Excel', fontsize=10, color='olive', ha='center')
ax.text(4, 8.3, 'Avg', fontsize=10, color='teal', ha='center')
ax.text(5, 8.5, 'Smooth', fontsize=10, color='blue', ha='center')
ax.text(6, 7, 'Mild', fontsize=10, color='brown', ha='center')

ax.legend(loc='upper left', fontsize=10)
ax.grid(axis='y', linestyle='-.', linewidth=0.7, alpha=0.3)

plt.tight_layout()
plt.show()