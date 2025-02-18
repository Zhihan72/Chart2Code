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

bplot = ax.boxplot(scores_data, vert=False, patch_artist=True, labels=season_labels, notch=True,
                   boxprops=dict(facecolor='lightsalmon', color='darkblue', linewidth=1.5),
                   whiskerprops=dict(color='darkblue', linewidth=1.5),
                   capprops=dict(color='darkblue', linewidth=2),
                   medianprops=dict(color='darkgoldenrod', linewidth=2),
                   flierprops=dict(marker='s', markerfacecolor='lavender', markersize=8, linestyle='none', markeredgecolor='darkblue'))

ax.scatter(median_values, range(1, 7), color='firebrick', marker='*', s=150, zorder=3, label='Median')

ax.set_title('Ice Cream Taste Tests', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Scores', fontsize=12, labelpad=10)
ax.set_ylabel('Season', fontsize=12, labelpad=10)

ax.text(9.5, 1, 'High', fontsize=10, color='indigo', va='center')
ax.text(7.5, 2, 'Low', fontsize=10, color='crimson', va='center')
ax.text(9.5, 3, 'Excel', fontsize=10, color='forestgreen', va='center')
ax.text(8.3, 4, 'Avg', fontsize=10, color='teal', va='center')
ax.text(8.5, 5, 'Smooth', fontsize=10, color='royalblue', va='center')
ax.text(7, 6, 'Mild', fontsize=10, color='saddlebrown', va='center')

ax.legend(loc='upper left', fontsize=10)
ax.grid(axis='x', linestyle='-.', linewidth=0.7, alpha=0.3)

plt.tight_layout()
plt.show()