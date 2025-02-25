import matplotlib.pyplot as plt
import numpy as np

# Departments and their performance scores
departments = ['Engineering', 'HR', 'Marketing', 'Sales', 'Finance']
performance_scores = {
    'Engineering': [88, 92, 85, 90],
    'HR': [75, 80, 78, 77],
    'Marketing': [82, 85, 88, 84],
    'Sales': [77, 79, 81, 78],
    'Finance': [90, 93, 91, 92]
}

# Calculate average performance scores
average_scores = [np.mean(performance_scores[department]) for department in departments]

# Sort departments by average performance scores in descending order
sorted_indices = np.argsort(average_scores)[::-1]
sorted_departments = [departments[i] for i in sorted_indices]
sorted_average_scores = [average_scores[i] for i in sorted_indices]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# New set of colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA8']

# Create a horizontal bar plot with sorted data
bars = ax.barh(sorted_departments, sorted_average_scores, color=colors, alpha=0.75, edgecolor='black')

# Add titles and labels
ax.set_title('Average Quarterly Performance Scores\nfor Company Departments in 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Average Performance Score', fontsize=12)
ax.set_ylabel('Departments', fontsize=12)

# Display the average score above each bar
for bar, avg in zip(bars, sorted_average_scores):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2, f'{avg:.1f}', va='center', fontsize=10, color='black')

# Add grid lines for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()