import matplotlib.pyplot as plt
import numpy as np

departments = ['Engineering', 'Marketing', 'Sales', 'Finance']

performance_scores = {
    'Engineering': [88, 92, 85, 90],
    'Marketing': [82, 85, 88, 84],
    'Sales': [77, 79, 81, 78],
    'Finance': [90, 93, 91, 92]
}

data = [np.array(performance_scores[department]) for department in departments]
average_scores = [np.mean(scores) for scores in data]

# Sort departments based on average performance scores in descending order
sorted_indices = np.argsort(average_scores)[::-1]
sorted_departments = [departments[i] for i in sorted_indices]
sorted_average_scores = [average_scores[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(sorted_departments, sorted_average_scores, color='#4CAF50', alpha=0.75, edgecolor='black')

ax.set_title('Average Quarterly Performance Scores\nfor Company Departments in 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Average Performance Score', fontsize=12)
ax.set_ylabel('Departments', fontsize=12)

for bar, avg in zip(bars, sorted_average_scores):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2, f'{avg:.1f}', va='center', fontsize=10, color='black')

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()