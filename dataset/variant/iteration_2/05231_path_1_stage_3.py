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

# Remove textual elements
plt.xticks([])
plt.yticks([])
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()