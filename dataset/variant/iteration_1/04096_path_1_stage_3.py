import matplotlib.pyplot as plt
import numpy as np

strategies = [
    'Field Sales', 'Refer-a-Friend', 'Online Marketing', 
    'Telemarketing', 'Email Campaigns', 'Retail Partnerships'
]
sales_percentages = [20, 15, 40, 10, 10, 5]
revenues = [40000, 30000, 80000, 20000, 20000, 10000]

fig, ax1 = plt.subplots(figsize=(12, 8))

bars = ax1.bar(strategies, sales_percentages, color='lightgreen', 
               edgecolor='darkgreen', width=0.5)

ax1.set_ylabel('Percentage of Sales Achieved', fontsize=12, labelpad=10)
ax1.set_xlabel('Approaches to Sales', fontsize=12, labelpad=10)
ax1.set_title('Evaluation of Sales Approaches for H1 2023', fontsize=16, fontweight='bold', pad=20)

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height - 2, f'{height}%', 
             ha='center', va='top', fontsize=12, color='white', fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(strategies, revenues, color='purple', marker='s', linestyle='--', 
         linewidth=2, label='Revenue ($k)')
ax2.set_ylabel('Generated Revenue ($k)', fontsize=12, color='purple', labelpad=10)

for i, rev in enumerate(revenues):
    ax2.text(i, rev + 2000, f'${rev/1000}k', ha='center', va='bottom', fontsize=10, color='purple')

plt.xticks(rotation=45, ha='right')

# Removed grid lines for a cleaner look
ax2.yaxis.grid(False)

plt.tight_layout()

# Moved legend to 'lower left'
ax2.legend(loc='lower left')

plt.show()