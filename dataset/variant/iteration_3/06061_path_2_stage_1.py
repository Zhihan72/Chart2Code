import matplotlib.pyplot as plt
import numpy as np

# Sales specialists
specialists = ['Specialist A', 'Specialist B', 'Specialist C', 'Specialist D']

# Monthly sales data (in thousands)
monthly_sales = np.array([
    [30, 35, 20, 25, 40, 45, 30, 35, 40, 50, 60, 55],  # Specialist A
    [25, 30, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],  # Specialist B
    [40, 45, 50, 55, 60, 65, 55, 50, 45, 40, 35, 30],  # Specialist C
    [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]   # Specialist D
])

# Average customer satisfaction scores (out of 10) for the year
satisfaction_scores = np.array([8.5, 9.0, 7.5, 8.0])

# Create the figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width
bar_width = 0.2

# Positions of the bars on the x-axis
r1 = np.arange(len(monthly_sales[0]))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Plot bars with a single color
common_color = 'c'  # A shade of cyan
ax.bar(r1, monthly_sales[0], color=common_color, width=bar_width, edgecolor='grey', label=specialists[0])
ax.bar(r2, monthly_sales[1], color=common_color, width=bar_width, edgecolor='grey', label=specialists[1])
ax.bar(r3, monthly_sales[2], color=common_color, width=bar_width, edgecolor='grey', label=specialists[2])
ax.bar(r4, monthly_sales[3], color=common_color, width=bar_width, edgecolor='grey', label=specialists[3])

# Adding title and labels
ax.set_title('Monthly Sales Performance and Satisfaction Scores of Sales Specialists', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Sales (in thousands)', fontsize=14)
ax.set_xticks([r + bar_width for r in range(len(monthly_sales[0]))])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.legend()

# Twin axes to show satisfaction scores
ax2 = ax.twinx()
ax2.plot([r + bar_width * 1.5 for r in range(len(specialists))], satisfaction_scores, color='k', marker='o', linestyle='--', linewidth=2, markersize=10)
ax2.set_ylabel('Customer Satisfaction Scores', fontsize=14)

# Display satisfaction scores above the points
for i, score in enumerate(satisfaction_scores):
    ax2.text(i + bar_width * 1.5, score + 0.1, str(score), color='black', ha='center', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', alpha=0.7))

# Enhancing readability
plt.tight_layout()

# Show the plot
plt.show()