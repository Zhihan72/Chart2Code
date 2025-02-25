import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']

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

apple_sum = apple_sales.sum(axis=0)
orange_sum = orange_sales.sum(axis=0)
banana_sum = banana_sales.sum(axis=0)

total_sales = apple_sum + orange_sum + banana_sum
sorted_indices = np.argsort(-total_sales)

regions_sorted = np.array(regions)[sorted_indices]
apple_sorted = apple_sum[sorted_indices]
orange_sorted = orange_sum[sorted_indices]
banana_sorted = banana_sum[sorted_indices]

fig, ax1 = plt.subplots(figsize=(8, 8))

x = np.arange(len(regions))
bar_width = 0.25

# Applying a single color to all data groups
consistent_color = '#4682b4'  # Steel blue color for all bars

ax1.bar(x - bar_width, apple_sorted, bar_width, color=consistent_color)
ax1.bar(x, orange_sorted, bar_width, color=consistent_color)
ax1.bar(x + bar_width, banana_sorted, bar_width, color=consistent_color)

ax1.set_title('Total Fruit Sales Sorted by Region')
ax1.set_xlabel('Region')
ax1.set_ylabel('Sales Volume (thousands)')
ax1.set_xticks(x)
ax1.set_xticklabels(regions_sorted)

plt.tight_layout()
plt.show()