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

sorted_indices = np.argsort(average_scores)[::-1]
sorted_departments = [departments[i] for i in sorted_indices]
sorted_average_scores = [average_scores[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(
    sorted_departments, sorted_average_scores,
    color=['#33FF57', '#3357FF', '#F3FF33', '#FF5733'],  # Shuffled colors
    alpha=0.85, edgecolor='darkred', hatch='/'
)

plt.xticks(fontsize=12, color='darkblue')
plt.yticks(fontsize=12, color='darkblue')
ax.grid(axis='x', linestyle='-.', color='gray', alpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(2)
ax.spines['right'].set_color('red')

plt.tight_layout()
plt.show()