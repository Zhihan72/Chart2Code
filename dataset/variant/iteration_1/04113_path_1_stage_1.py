import matplotlib.pyplot as plt
import numpy as np

# Departments
departments = ["Development", "Marketing", "Sales", "HR", "Support"]

# Monthly satisfaction scores for each department (Jan to Dec)
development_scores = [3, 4, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3]
marketing_scores = [4, 4, 3, 4, 3, 4, 5, 4, 3, 4, 5, 4]
sales_scores = [3, 2, 4, 3, 4, 3, 4, 5, 4, 3, 4, 5]
hr_scores = [5, 4, 4, 3, 5, 4, 5, 5, 4, 3, 4, 5]
support_scores = [4, 3, 4, 4, 3, 4, 3, 4, 5, 4, 3, 4]

satisfaction_data = {
    "Development": development_scores,
    "Marketing": marketing_scores,
    "Sales": sales_scores,
    "HR": hr_scores,
    "Support": support_scores
}

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

fig, axes = plt.subplots(3, 2, figsize=(14, 10))
axes = axes.flatten()
fig.delaxes(axes[-1])

# Set a consistent color for all plots
consistent_color = 'blue'

for ax, (dept, scores) in zip(axes, satisfaction_data.items()):
    ax.plot(months, scores, marker='o', linestyle='-', color=consistent_color, label=f'{dept} Satisfaction')
    ax.set_title(f'{dept} Satisfaction Over the Year', fontsize=14, fontweight='bold')
    ax.set_xlabel('Months', fontsize=12)
    ax.set_ylabel('Satisfaction Score', fontsize=12)
    ax.set_ylim(1, 5.5)
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.legend(loc='upper left')

plt.suptitle("Employee Satisfaction Scores Over the Year in Different Departments", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()