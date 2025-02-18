import matplotlib.pyplot as plt
import numpy as np

# Departments
departments = ["Development", "Marketing", "Sales", "HR", "Support"]

# Monthly satisfaction scores for each department (Jan to Dec)
development_scores = [3, 4, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3]
marketing_scores = [4, 4, 3, 4, 3, 4, 5, 4, 3, 4, 5, 4]
hr_scores = [5, 4, 4, 3, 5, 4, 5, 5, 4, 3, 4, 5]
support_scores = [4, 3, 4, 4, 3, 4, 3, 4, 5, 4, 3, 4]

# Store scores in a dictionary for easier plotting
satisfaction_data = {
    "Development": development_scores,
    "Marketing": marketing_scores,
    "HR": hr_scores,
    "Support": support_scores
}

# Months
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Create the figure and subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for ax, (dept, scores) in zip(axes, satisfaction_data.items()):
    ax.plot(months, scores, marker='o', linestyle='-', label=f'{dept} Satisfaction')
    ax.set_title(f'{dept} Satisfaction Over the Year', fontsize=14, fontweight='bold')
    ax.set_xlabel('Months', fontsize=12)
    ax.set_ylabel('Satisfaction Score', fontsize=12)
    ax.set_ylim(1, 5.5)
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.legend(loc='upper left')

# Set the overall title for the figure
plt.suptitle("Employee Satisfaction Scores Over the Year in Different Departments", fontsize=16, fontweight='bold', y=1.02)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()