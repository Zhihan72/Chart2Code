import matplotlib.pyplot as plt
import numpy as np

# Sales strategies
strategies = [
    'Field Sales', 'Refer-a-Friend', 'Online Marketing', 
    'Telemarketing', 'Email Campaigns', 'Retail Partnerships'
]

# Sales percentages data
sales_percentages = [20, 15, 40, 10, 10, 5]

# Revenues data
revenues = [40000, 30000, 80000, 20000, 20000, 10000]

# Create the figure and bar chart for percentages
fig, ax1 = plt.subplots(figsize=(12, 8))

# Apply a single color to all bars
bars = ax1.bar(strategies, sales_percentages, color='skyblue', edgecolor='black', width=0.6)

# Labels and title
ax1.set_ylabel('Percentage of Sales Achieved', fontsize=12, labelpad=10)
ax1.set_xlabel('Approaches to Sales', fontsize=12, labelpad=10)
ax1.set_title('Evaluation of Sales Approaches for H1 2023', fontsize=16, fontweight='bold', pad=20)

# Sales Percentage Data Labels
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height - 2, f'{height}%', 
             ha='center', va='top', fontsize=12, color='white', fontweight='bold')

# Revenue line plot for comparison
ax2 = ax1.twinx()
ax2.plot(strategies, revenues, color='orange', marker='o', linewidth=2, label='Revenue ($k)')
ax2.set_ylabel('Generated Revenue ($k)', fontsize=12, color='orange', labelpad=10)

# Revenue Data Labels
for i, rev in enumerate(revenues):
    ax2.text(i, rev + 2000, f'${rev/1000}k', ha='center', va='bottom', fontsize=10, color='orange')

# X-axis labels rotation
plt.xticks(rotation=45, ha='right')

# Grid lines for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)

# Adjust the layout automatically
plt.tight_layout()

# Secondary legend
ax2.legend(loc='upper right')

# Show plot
plt.show()