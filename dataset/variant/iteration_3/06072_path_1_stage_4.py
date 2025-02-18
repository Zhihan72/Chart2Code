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
                 meanprops={"marker": "d", "markerfacecolor": "skyblue", "markeredgecolor": "blue", "markersize": 8})

# Modify box colors and outline
colors = ['orange', 'purple', 'green', 'red', 'cyan']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

# Change whisker, cap, median, flier styles
for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='navy', linewidth=1.0, linestyle='-')
    cap.set(color='navy', linewidth=1.0)
    median.set(color='darkgreen', linewidth=2)
    flier.set(marker="x", color="orange", alpha=0.7)

ax.set_title('Employee Performance', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Scores', fontsize=14, fontweight='bold')
ax.set_ylabel('Depts', fontsize=14, fontweight='bold')

# Alter the grid style
ax.grid(linestyle='-', alpha=0.3)

# Update the legend position and style
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, departments, title='Departments', loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()