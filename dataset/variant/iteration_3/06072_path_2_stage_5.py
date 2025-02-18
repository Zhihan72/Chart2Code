import matplotlib.pyplot as plt
import numpy as np

departments = ['Admin', 'BizDev', 'Engineering', 'Comm', 'Support']

HR_scores = [85, 88, 70, 75, 60, 90, 82, 74, 77, 80]
Sales_scores = [91, 90, 85, 83, 89, 88, 85, 80, 87, 92]
Development_scores = [84, 91, 78, 85, 87, 79, 90, 82, 83, 86]
Marketing_scores = [81, 84, 78, 85, 79, 82, 77, 88, 75, 80]
Support_scores = [71, 60, 72, 70, 68, 73, 69, 65, 74, 70]

performance_data = [HR_scores, Sales_scores, Development_scores, Marketing_scores, Support_scores]

fig, ax = plt.subplots(figsize=(14, 8))

box = ax.boxplot(performance_data, vert=False, patch_artist=True, notch=False, showmeans=False, 
                 medianprops={"color": "darkred", "linewidth": 3})

# Applying a single color consistently across all data groups
single_color = 'skyblue'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

ax.set_title('Division Analysis: Team Scores', fontsize=18, fontweight='bold')
ax.set_ylabel('Groups', fontsize=15, color='blue')
ax.set_xlabel('Rating Values', fontsize=15, color='green')

for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='purple', linewidth=1.2, linestyle=':')
    cap.set(color='purple', linewidth=1.2)

ax.grid(False)

# Update the legend to reflect a single color
handle = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=single_color, markersize=10)
ax.legend([handle], ['All Teams'], title='Team Legend', loc='upper right')

plt.tight_layout()
plt.show()