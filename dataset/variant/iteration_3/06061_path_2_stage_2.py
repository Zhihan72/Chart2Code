import matplotlib.pyplot as plt
import numpy as np

# Monthly sales data (in thousands)
monthly_sales = np.array([
    [30, 35, 20, 25, 40, 45, 30, 35, 40, 50, 60, 55],
    [25, 30, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    [40, 45, 50, 55, 60, 65, 55, 50, 45, 40, 35, 30],
    [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
])

# Satisfaction scores
satisfaction_scores = np.array([8.5, 9.0, 7.5, 8.0])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.2
r1 = np.arange(len(monthly_sales[0]))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

common_color = 'c'
ax.bar(r1, monthly_sales[0], color=common_color, width=bar_width, edgecolor='grey')
ax.bar(r2, monthly_sales[1], color=common_color, width=bar_width, edgecolor='grey')
ax.bar(r3, monthly_sales[2], color=common_color, width=bar_width, edgecolor='grey')
ax.bar(r4, monthly_sales[3], color=common_color, width=bar_width, edgecolor='grey')

# Remove labels, titles, and legend
ax.set_xticks([r + bar_width for r in range(len(monthly_sales[0]))])
ax.set_xticklabels([])

ax2 = ax.twinx()
ax2.plot([r + bar_width * 1.5 for r in range(len(satisfaction_scores))], satisfaction_scores, color='k', marker='o', linestyle='--', linewidth=2, markersize=10)

# Remove the display of satisfaction scores
plt.tight_layout()
plt.show()