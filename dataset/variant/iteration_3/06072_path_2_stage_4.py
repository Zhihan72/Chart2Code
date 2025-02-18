import matplotlib.pyplot as plt
import numpy as np

# Changed departments labels
departments = ['Admin', 'BizDev', 'Engineering', 'Comm', 'Support']

# Data - manually altered within groups
HR_scores = [85, 88, 70, 75, 60, 90, 82, 74, 77, 80]  # Randomly shuffled
Sales_scores = [91, 90, 85, 83, 89, 88, 85, 80, 87, 92]  # Randomly shuffled
Development_scores = [84, 91, 78, 85, 87, 79, 90, 82, 83, 86]  # Randomly shuffled
Marketing_scores = [81, 84, 78, 85, 79, 82, 77, 88, 75, 80]  # Randomly shuffled
Support_scores = [71, 60, 72, 70, 68, 73, 69, 65, 74, 70]  # Randomly shuffled

# Grouped data
performance_data = [HR_scores, Sales_scores, Development_scores, Marketing_scores, Support_scores]

fig, ax = plt.subplots(figsize=(14, 8))

# Horizontal box plot
box = ax.boxplot(performance_data, vert=False, patch_artist=True, notch=False, showmeans=False,
                 medianprops={"color": "darkred", "linewidth": 3})

colors = ['skyblue', 'lightgreen', 'peachpuff', 'powderblue', 'lavender']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Changed textual elements
ax.set_title('Division Analysis: Team Scores', fontsize=18, fontweight='bold')
ax.set_ylabel('Groups', fontsize=15, color='blue')
ax.set_xlabel('Rating Values', fontsize=15, color='green')

# Customize whiskers, caps
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='purple', linewidth=1.2, linestyle=':')
    cap.set(color='purple', linewidth=1.2)

# Remove grid lines
ax.grid(False)

# Legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
ax.legend(handles, departments, title='Team Legend', loc='upper right')

plt.tight_layout()
plt.show()