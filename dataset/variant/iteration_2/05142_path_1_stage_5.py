import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia']
q1_sales = [120, 98, 140]
q2_sales = [150, 110, 160]
q3_sales = [130, 120, 165]
q4_sales = [140, 130, 180]

# Sort the data
sorted_indices_q1 = np.argsort(q1_sales)
sorted_indices_q2 = np.argsort(q2_sales)
sorted_indices_q3 = np.argsort(q3_sales)
sorted_indices_q4 = np.argsort(q4_sales)

# Sort sales and corresponding regions
regions_sorted_q1 = [regions[i] for i in sorted_indices_q1]
regions_sorted_q2 = [regions[i] for i in sorted_indices_q2]
regions_sorted_q3 = [regions[i] for i in sorted_indices_q3]
regions_sorted_q4 = [regions[i] for i in sorted_indices_q4]

q1_sales_sorted = [q1_sales[i] for i in sorted_indices_q1]
q2_sales_sorted = [q2_sales[i] for i in sorted_indices_q2]
q3_sales_sorted = [q3_sales[i] for i in sorted_indices_q3]
q4_sales_sorted = [q4_sales[i] for i in sorted_indices_q4]

fig, ax1 = plt.subplots(1, 1, figsize=(12, 7))
bar_width = 0.2
bar_positions = np.arange(len(regions))

ax1.bar(bar_positions - 1.5 * bar_width, q1_sales_sorted, width=bar_width, color='#8B0000', edgecolor='black', label='Q1')
ax1.bar(bar_positions - 0.5 * bar_width, q2_sales_sorted, width=bar_width, color='#FF8C00', edgecolor='black', label='Q2')
ax1.bar(bar_positions + 0.5 * bar_width, q3_sales_sorted, width=bar_width, color='#32CD32', edgecolor='black', label='Q3')
ax1.bar(bar_positions + 1.5 * bar_width, q4_sales_sorted, width=bar_width, color='#1E90FF', edgecolor='black', label='Q4')

# Assuming sorting by Q1 sales as the primary order for x-ticks
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(regions_sorted_q1)
ax1.legend(loc='upper right', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()