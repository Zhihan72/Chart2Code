import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Title: "Employee Performance Evaluation: A Measure Across Departments"
# The company, "Tech Solutions Inc.", annually evaluates the performance of its employees across different departments. 
# To analyze the variation in performance within and across departments, we have collected performance scores of employees 
# from five key departments.

# Departments
departments = ['HR', 'Sales', 'Development', 'Marketing', 'Customer Support']

# Performance scores for each department
# Explicitly created data based on a fictional performance scoring system
HR_scores = [70, 75, 80, 85, 60, 90, 88, 74, 82, 77]
Sales_scores = [85, 87, 90, 83, 80, 88, 92, 85, 91, 89]
Development_scores = [78, 82, 85, 91, 87, 84, 79, 86, 90, 83]
Marketing_scores = [75, 80, 78, 82, 85, 88, 77, 84, 79, 81]
Support_scores = [65, 70, 72, 60, 68, 74, 70, 69, 71, 73]

# Combine data into a list
performance_data = [HR_scores, Sales_scores, Development_scores, Marketing_scores, Support_scores]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create the box plot
box = ax.boxplot(performance_data, vert=True, patch_artist=True, notch=True, showmeans=True,
                 meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black", "markersize": 8})

# Define colors for each department
colors = ['lightcoral', 'lightgreen', 'lightblue', 'lightyellow', 'lightpink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add titles and labels
ax.set_title('Employee Performance Evaluation:\nA Measure Across Departments', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Departments', fontsize=14, fontweight='bold')
ax.set_ylabel('Performance Scores', fontsize=14, fontweight='bold')

# Customize whiskers, medians, caps, and outliers
for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='grey', linewidth=1.5, linestyle='--')
    cap.set(color='grey', linewidth=1.5)
    median.set(color='darkred', linewidth=2)
    flier.set(marker='o', color='gold', alpha=0.5)

# Add grid for better readability
ax.grid(linestyle='--', alpha=0.6)

# Legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, departments, title='Departments', loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()