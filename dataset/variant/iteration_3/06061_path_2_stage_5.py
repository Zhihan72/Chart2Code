import matplotlib.pyplot as plt
import numpy as np

monthly_sales = np.array([
    [35, 40, 20, 25, 45, 30, 55, 35, 40, 30, 50, 60],
    [85, 60, 45, 30, 90, 55, 65, 50, 75, 25, 70, 80],
    [45, 65, 30, 55, 50, 40, 55, 35, 60, 50, 40, 45],
    [60, 70, 25, 35, 40, 20, 30, 45, 75, 55, 65, 50]
])

# Calculate total sales for each group and sort by these totals
total_sales = monthly_sales.sum(axis=1)
sorted_indices = np.argsort(total_sales)[::-1]  # Sort in descending order

# Sort data based on total sales
sorted_sales = monthly_sales[sorted_indices]

# Plotting the sorted bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.6  # Use a wider bar for a single series

r = np.arange(len(sorted_sales))

ax.bar(r, sorted_sales[:, 0], color='c', width=bar_width)

ax.set_xticks(r)
ax.set_xticklabels([f'Group {i+1}' for i in sorted_indices])

plt.tight_layout()
plt.show()