import matplotlib.pyplot as plt
import numpy as np

# Ice cream scores by season
spring_scores = [8.2, 8.9, 9.1, 7.8, 8.7, 9.3, 7.5, 8.5, 8.8, 9.0, 8.3, 7.9]
summer_scores = [6.5, 6.8, 7.0, 6.4, 6.1, 7.2, 6.6, 6.9, 6.7, 7.1, 6.3, 6.0]
autumn_scores = [8.8, 8.1, 8.5, 8.4, 8.7, 9.0, 8.3, 8.6, 8.9, 9.1, 8.2, 8.0]

scores_data = [spring_scores, summer_scores, autumn_scores]
median_values = [np.median(season) for season in scores_data]
season_labels = ['Spr', 'Sum', 'Aut']

fig, ax = plt.subplots(figsize=(12, 8))

# New color order for boxplots
color_order = ['lightgreen', 'lightyellow', 'lightblue']
edge_color_order = ['green', 'goldenrod', 'blue']
median_color_order = ['darkgreen', 'darkgoldenrod', 'darkblue']

# Adjust boxplot properties for horizontal orientation
bplot = ax.boxplot(scores_data, vert=False, patch_artist=True, labels=season_labels, notch=True,
                   boxprops=dict(facecolor=color_order[0], color=edge_color_order[0], linewidth=1.5),
                   whiskerprops=dict(color=edge_color_order[0], linewidth=1.5),
                   capprops=dict(color=edge_color_order[0], linewidth=1.5),
                   medianprops=dict(color=median_color_order[0], linewidth=2),
                   flierprops=dict(marker='o', markerfacecolor='red', markersize=6, linestyle='none', markeredgecolor='purple'))

ax.scatter(median_values, range(1, len(scores_data) + 1), color='orange', s=100, zorder=3, label='Median')

ax.set_title('Ice Cream Scores by Season', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Scores', fontsize=12, labelpad=10)
ax.set_ylabel('Season', fontsize=12, labelpad=10)

# Adjusted annotation positions
ax.text(9.5, 1, 'Spr: High', fontsize=10, color='green', va='center')
ax.text(7.5, 2, 'Sum: Low', fontsize=10, color='goldenrod', va='center')
ax.text(9.5, 3, 'Aut: Great', fontsize=10, color='blue', va='center')

ax.legend(loc='upper right', fontsize=10)
ax.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.6)

plt.tight_layout()
plt.show()