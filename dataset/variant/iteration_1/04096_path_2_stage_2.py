import matplotlib.pyplot as plt
import numpy as np

strategies = ['Online Marketing', 'Field Sales', 'Refer-a-Friend', 'Retail Partnerships']
sales_percentages = [40, 20, 15, 5]
revenues = [80000, 40000, 30000, 10000]

fig, ax1 = plt.subplots(figsize=(12, 8))

bars = ax1.bar(strategies, sales_percentages, color='blue', edgecolor='black', width=0.6)

ax1.set_ylabel('Sales Percentage (%)', fontsize=12, labelpad=10)
ax1.set_xlabel('Sales Strategies', fontsize=12, labelpad=10)
ax1.set_title('Performance Analysis of Different Sales Strategies in Q1 2023', fontsize=16, fontweight='bold', pad=20)

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height - 2, f'{height}%', 
             ha='center', va='top', fontsize=12, color='white', fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(strategies, revenues, color='blue', marker='o', linewidth=2, label='Revenue ($)')
ax2.set_ylabel('Revenue ($)', fontsize=12, color='blue', labelpad=10)

for i, rev in enumerate(revenues):
    ax2.text(i, rev + 2000, f'${rev/1000}k', ha='center', va='bottom', fontsize=10, color='blue')

plt.xticks(rotation=45, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
ax2.legend(loc='upper right')
plt.show()