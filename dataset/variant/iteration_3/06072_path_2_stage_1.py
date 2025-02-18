import matplotlib.pyplot as plt
import numpy as np

# Departments
departments = ['HR', 'Sales', 'Development', 'Marketing', 'Customer Support']

# Performance scores for each department
HR_scores = [70, 75, 80, 85, 60, 90, 88, 74, 82, 77]
Sales_scores = [85, 87, 90, 83, 80, 88, 92, 85, 91, 89]
Development_scores = [78, 82, 85, 91, 87, 84, 79, 86, 90, 83]
Marketing_scores = [75, 80, 78, 82, 85, 88, 77, 84, 79, 81]
Support_scores = [65, 70, 72, 60, 68, 74, 70, 69, 71, 73]
performance_data = [HR_scores, Sales_scores, Development_scores, Marketing_scores, Support_scores]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create the box plot
box = ax.boxplot(performance_data, vert=True, patch_artist=True, notch=False, showmeans=False,
                 medianprops={"color": "darkred", "linewidth": 3})

colors = ['skyblue', 'lightgreen', 'peachpuff', 'powderblue', 'lavender']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Titles and labels
ax.set_title('Employee Performance Evaluation: Departments', fontsize=18, fontweight='bold')
ax.set_xlabel('Departments', fontsize=15, color='blue')
ax.set_ylabel('Scores', fontsize=15, color='green')

# Customize whiskers, caps
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='purple', linewidth=1.2, linestyle=':')
    cap.set(color='purple', linewidth=1.2)

# Remove grid lines
ax.grid(False)

# Legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
ax.legend(handles, departments, title='Department Legend', loc='lower right')

# Layout adjustment
plt.tight_layout()

plt.show()