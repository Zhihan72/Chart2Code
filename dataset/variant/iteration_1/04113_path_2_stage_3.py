import matplotlib.pyplot as plt
import numpy as np

# Remaining departments
departments = ["Dev", "Mkt", "Supp"]

# Monthly satisfaction scores for each remaining department (Jan to Dec)
dev_scores = [3, 4, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3]
mkt_scores = [4, 4, 3, 4, 3, 4, 5, 4, 3, 4, 5, 4]
supp_scores = [4, 3, 4, 4, 3, 4, 3, 4, 5, 4, 3, 4]

# Updated data dictionary
satisfaction_data = {
    "Dev": dev_scores,
    "Mkt": mkt_scores,
    "Supp": supp_scores
}

# Months
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Create the figure and subplots, with one less subplot
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Remove one subplot by simply not using the last one
for ax, (dept, scores) in zip(axes[:-1], satisfaction_data.items()):
    ax.plot(months, scores, marker='o', linestyle='-', label=f'{dept} Sat.')
    ax.set_title(f'{dept} Sat.', fontsize=14, fontweight='bold')
    ax.set_xlabel('Mths', fontsize=12)
    ax.set_ylabel('Score', fontsize=12)
    ax.set_ylim(1, 5.5)
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.legend(loc='upper left')

# Set the overall title for the figure
plt.suptitle("Sat. Scores by Dept.", fontsize=16, fontweight='bold', y=1.02)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()