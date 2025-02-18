import matplotlib.pyplot as plt
import numpy as np

departments = ['Engineering', 'Marketing', 'Finance']
performance_scores = {
    'Engineering': [88, 92, 85, 90],
    'Marketing': [82, 85, 88, 84],
    'Finance': [90, 93, 91, 92]
}

average_scores = [np.mean(performance_scores[department]) for department in departments]

sorted_indices = np.argsort(average_scores)[::-1]
sorted_departments = [departments[i] for i in sorted_indices]
sorted_average_scores = [average_scores[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF5733', '#33FF57', '#FF33A1']

bars = ax.barh(sorted_departments, sorted_average_scores, color=colors, alpha=0.75, edgecolor='black')

ax.set_title('Dept Performance 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Avg Score', fontsize=12)

for bar, avg in zip(bars, sorted_average_scores):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2, f'{avg:.1f}', va='center', fontsize=10, color='black')

plt.show()