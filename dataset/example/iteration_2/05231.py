import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart represents the average performance score of different departments in a tech company over the last year. Each department's scores are collected quarterly.

# Departments
departments = ['Engineering', 'HR', 'Marketing', 'Sales', 'Finance']

# Quarterly performance scores for the departments
performance_scores = {
    'Engineering': [88, 92, 85, 90],
    'HR': [75, 80, 78, 77],
    'Marketing': [82, 85, 88, 84],
    'Sales': [77, 79, 81, 78],
    'Finance': [90, 93, 91, 92]
}

# Quarterly data as numpy arrays
data = [np.array(performance_scores[department]) for department in departments]

# Calculate average performance scores
average_scores = [np.mean(scores) for scores in data]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create a bar plot
bars = ax.barh(departments, average_scores, color='#4CAF50', alpha=0.75, edgecolor='black')

# Add titles and labels
ax.set_title('Average Quarterly Performance Scores\nfor Company Departments in 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Average Performance Score', fontsize=12)
ax.set_ylabel('Departments', fontsize=12)

# Display the average score above each bar
for bar, avg in zip(bars, average_scores):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2, f'{avg:.1f}', va='center', fontsize=10, color='black')

# Add grid lines for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Additional subplots for quarterly breakdown
fig, axs = plt.subplots(len(departments), 1, figsize=(14, 16), sharex=True)

# Create a bar chart for each department's quarterly scores
for index, (department, scores) in enumerate(performance_scores.items()):
    axs[index].bar(quarters, scores, color='#FF5722', alpha=0.75, edgecolor='black')
    axs[index].set_title(f'{department} Quarterly Performance in 2022', fontsize=13, fontweight='bold')
    axs[index].set_ylabel('Score', fontsize=12)
    for i, score in enumerate(scores):
        axs[index].text(i, score + 1, f'{score}', ha='center', fontsize=10, color='black')
    axs[index].grid(axis='y', linestyle='--', alpha=0.7)

# Overall layout adjustments
plt.tight_layout()

# Display the plots
plt.show()