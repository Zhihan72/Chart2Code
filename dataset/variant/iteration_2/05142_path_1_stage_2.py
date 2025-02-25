import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia']
q1_sales = [120, 98, 140]
q2_sales = [150, 110, 160]
q3_sales = [130, 120, 165]
q4_sales = [140, 130, 180]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
bar_width = 0.2
bar_positions = np.arange(len(regions))

# Changed colors
ax1.bar(bar_positions - 1.5 * bar_width, q1_sales, width=bar_width, color='#8B0000', edgecolor='black', label='Q1')
ax1.bar(bar_positions - 0.5 * bar_width, q2_sales, width=bar_width, color='#FF8C00', edgecolor='black', label='Q2')
ax1.bar(bar_positions + 0.5 * bar_width, q3_sales, width=bar_width, color='#32CD32', edgecolor='black', label='Q3')
ax1.bar(bar_positions + 1.5 * bar_width, q4_sales, width=bar_width, color='#1E90FF', edgecolor='black', label='Q4')

ax1.set_title('Monthly Sales Performance of Beverage Company Across Regions (2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Regions', fontsize=14)
ax1.set_ylabel('Sales Units (in thousands)', fontsize=14)
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(regions, rotation=15, ha='right', fontsize=12)
ax1.legend(loc='upper right', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

overall_sales = np.array(q1_sales) + np.array(q2_sales) + np.array(q3_sales) + np.array(q4_sales)
ax2.barh(regions, overall_sales, color='#8A2BE2', edgecolor='black', alpha=0.8)

ax2.set_title('Overall Annual Sales Performance by Region (2022)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Sales Units (in thousands)', fontsize=14)
ax2.set_ylabel('Regions', fontsize=14)

for i in range(len(overall_sales)):
    ax2.text(overall_sales[i] + 5, i, f'{overall_sales[i]}K', va='center', ha='left', fontsize=12, color='white', fontweight='bold')

plt.tight_layout()
plt.show()