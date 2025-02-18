import matplotlib.pyplot as plt
import numpy as np

# Sales strategies being analyzed
strategies = [
    'Online Marketing', 'Field Sales', 
    'Refer-a-Friend', 'Retail Partnerships'
]

# Percentage of total sales achieved by each strategy
sales_percentages = [40, 20, 15, 5]

# Revenue generated per strategy (constructed data)
revenues = [80000, 40000, 30000, 10000]

# Create the figure and bar chart for percentages
fig, ax1 = plt.subplots(figsize=(12, 8))

bars = ax1.bar(strategies, sales_percentages, color='skyblue', edgecolor='black', width=0.6)

# Labels and title
ax1.set_ylabel('Sales Percentage (%)', fontsize=12, labelpad=10)
ax1.set_xlabel('Sales Strategies', fontsize=12, labelpad=10)
ax1.set_title('Performance Analysis of Different Sales Strategies in Q1 2023', fontsize=16, fontweight='bold', pad=20)

# Sales Percentage Data Labels
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height - 2, f'{height}%', 
             ha='center', va='top', fontsize=12, color='white', fontweight='bold')

# Add a line plot for revenue
ax2 = ax1.twinx()
ax2.plot(strategies, revenues, color='orange', marker='o', linewidth=2, label='Revenue ($)')
ax2.set_ylabel('Revenue ($)', fontsize=12, color='orange', labelpad=10)

# Add revenue data labels to the line plot
for i, rev in enumerate(revenues):
    ax2.text(i, rev + 2000, f'${rev/1000}k', ha='center', va='bottom', fontsize=10, color='orange')

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right')

# Grid lines for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)

# Adjust layout automatically
plt.tight_layout()

# Secondary plot legend
ax2.legend(loc='upper right')

# Show the plot
plt.show()