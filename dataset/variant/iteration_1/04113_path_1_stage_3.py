import matplotlib.pyplot as plt
import numpy as np

# Altered department names and labels
departments = ["Innovations", "Outreach", "Transactions", "Well-being", "Tech Support"]
innovation_scores = [3, 4, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3]
outreach_scores = [4, 4, 3, 4, 3, 4, 5, 4, 3, 4, 5, 4]
transactions_scores = [3, 2, 4, 3, 4, 3, 4, 5, 4, 3, 4, 5]
wellbeing_scores = [5, 4, 4, 3, 5, 4, 5, 5, 4, 3, 4, 5]
tech_support_scores = [4, 3, 4, 4, 3, 4, 3, 4, 5, 4, 3, 4]

satisfaction_data = {
    "Innovations": innovation_scores,
    "Outreach": outreach_scores,
    "Transactions": transactions_scores,
    "Well-being": wellbeing_scores,
    "Tech Support": tech_support_scores
}

# Altered months
months = np.array(["January", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "February"])

fig, axes = plt.subplots(3, 2, figsize=(14, 10))
axes = axes.flatten()
fig.delaxes(axes[-1])

marker_types = ['o', '^', 's', 'D', 'x']
line_styles = ['-', '--', '-.', ':']

# New titles and labels reflecting the randomness
for ax, (dept, scores), marker, linestyle in zip(axes, satisfaction_data.items(), marker_types, line_styles):
    ax.plot(months, scores, marker=marker, linestyle=linestyle, color='green', label=f'{dept} Satisfaction')
    ax.set_title(f'Satisfaction Trends in {dept}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year Months', fontsize=12)
    ax.set_ylabel('Happiness Score', fontsize=12)
    ax.set_ylim(1, 5.5)
    ax.grid(False)
    ax.legend(loc='lower right')

plt.suptitle("Team Happiness Index Across 12 Months", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()