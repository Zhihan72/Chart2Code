import matplotlib.pyplot as plt
import numpy as np

departments = ['HR', 'Sales', 'Dev', 'Mktg', 'Support']

HR_scores = [80, 77, 82, 90, 70, 74, 60, 85, 88, 75]
Sales_scores = [91, 88, 83, 85, 87, 85, 80, 89, 92, 90]
Development_scores = [83, 79, 87, 82, 90, 78, 84, 86, 91, 85]
Marketing_scores = [84, 78, 77, 81, 79, 75, 88, 82, 80, 85]
Support_scores = [68, 69, 71, 70, 65, 72, 70, 60, 73, 74]

performance_data = [HR_scores, Sales_scores, Development_scores, Marketing_scores, Support_scores]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(performance_data, vert=False, patch_artist=True, notch=True, showmeans=True,
                 meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black", "markersize": 8})

colors = ['lightcoral', 'lightgreen', 'lightblue', 'lightyellow', 'lightpink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Employee Performance', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Scores', fontsize=14, fontweight='bold')
ax.set_ylabel('Depts', fontsize=14, fontweight='bold')

for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='grey', linewidth=1.5, linestyle='--')
    cap.set(color='grey', linewidth=1.5)
    median.set(color='darkred', linewidth=2)
    flier.set(marker='o', color='gold', alpha=0.5)

ax.grid(linestyle='--', alpha=0.6)

handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, departments, title='Depts', loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()