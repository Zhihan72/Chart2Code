import matplotlib.pyplot as plt
import numpy as np

# Defined regions
regions = ['North', 'South', 'East', 'West']

# Sales volume data (in thousands of units)
apple_sales = np.array([
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [40, 45, 50, 55],
    [25, 30, 35, 40]
])

orange_sales = np.array([
    [20, 15, 10, 5],
    [25, 30, 35, 40],
    [35, 40, 45, 50],
    [30, 35, 45, 40]
])

banana_sales = np.array([
    [15, 20, 25, 30],
    [20, 25, 30, 35],
    [30, 35, 45, 50],
    [35, 40, 45, 50]
])

# Summing sales across seasons for each fruit type
apple_sum = apple_sales.sum(axis=0)
orange_sum = orange_sales.sum(axis=0)
banana_sum = banana_sales.sum(axis=0)

# Total sales for each region
total_sales = apple_sum + orange_sum + banana_sum

# Sorting in descending order (change order to 'asc' for ascending)
sorted_indices = np.argsort(-total_sales)

# Sorted data
regions_sorted = np.array(regions)[sorted_indices]
apple_sorted = apple_sum[sorted_indices]
orange_sorted = orange_sum[sorted_indices]
banana_sorted = banana_sum[sorted_indices]

# Create plot
fig, ax1 = plt.subplots(figsize=(8, 8))

x = np.arange(len(regions))
bar_width = 0.25

ax1.bar(x - bar_width, apple_sorted, bar_width, label='Apple', color='#ff9999')
ax1.bar(x, orange_sorted, bar_width, label='Orange', color='#66b3ff')
ax1.bar(x + bar_width, banana_sorted, bar_width, label='Banana', color='#99ff99')

ax1.set_title('Total Fruit Sales Sorted by Region', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Region', fontsize=12)
ax1.set_ylabel('Sales Volume (thousands)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(regions_sorted, fontsize=10)
ax1.legend(title='Fruit Type', loc='upper right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

fig.suptitle('Sorted Fruit Sales Analysis', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()