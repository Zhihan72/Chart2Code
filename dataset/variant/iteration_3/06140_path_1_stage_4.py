import matplotlib.pyplot as plt
import numpy as np

productivity_data = {
    'Mon': [4, 5, 6, 5, 7, 8, 5, 6, 4, 6],
    'Tue': [6, 7, 5, 6, 8, 9, 7, 6, 8, 9],
    'Wed': [7, 8, 6, 7, 9, 9, 7, 8, 6, 7],
    'Thu': [5, 6, 5, 6, 7, 7, 8, 6, 5, 6],
    'Fri': [4, 5, 4, 5, 6, 6, 5, 4, 5, 6],
    'Sat': [2, 3, 2, 4, 3, 4, 3, 2, 3, 4],
    'Sun': [1, 2, 1, 3, 2, 2, 3, 1, 2, 1],
    'Team A': [3, 5, 7, 6, 8, 5, 7, 6, 5, 7],
    'Team B': [4, 6, 5, 7, 6, 8, 5, 7, 6, 8]
}

box_plot_data = list(productivity_data.values())

fig, ax = plt.subplots(figsize=(14, 10))

ax.boxplot(box_plot_data, labels=productivity_data.keys(), patch_artist=True,
           boxprops=dict(color='blue', facecolor='lightcoral'),
           medianprops=dict(color='orange'),
           whiskerprops=dict(color='purple'),
           capprops=dict(color='black'),
           flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5),
           notch=True)

ax.set_title("Weekly Productivity", fontsize=18, fontweight='bold', loc='center', pad=20)
ax.set_ylabel('Score (1-10)', fontsize=14)
ax.set_xlabel('Day', fontsize=14)

ax.annotate('Peak', xy=(3, 9), xytext=(2.3, 9.5), fontsize=12, color='green',
             arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('Weekend Dip', xy=(7, 2.5), xytext=(6.3, 3.5), fontsize=12, color='orange',
             arrowprops=dict(facecolor='orange', shrink=0.05))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_yticks([])
ax.set_xticks([])

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()