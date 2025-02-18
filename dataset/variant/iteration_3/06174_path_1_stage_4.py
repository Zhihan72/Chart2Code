import matplotlib.pyplot as plt
import numpy as np

categories = ["Apples", "Bananas", "Oranges", "Plums"]
q1_sales = [120, 80, 150, 60]
q2_sales = [130, 85, 160, 70]
q3_sales = [140, 95, 170, 75]
q4_sales = [150, 100, 180, 80]

# Calculate average and sort indices based on it
avg_sales_per_quarter = np.mean([q1_sales, q2_sales, q3_sales, q4_sales], axis=0)
sorted_indices = np.argsort(avg_sales_per_quarter)

# Sort the sales data and categories based on sorted indices
categories_sorted = [categories[i] for i in sorted_indices]
q1_sales_sorted = [q1_sales[i] for i in sorted_indices]
q2_sales_sorted = [q2_sales[i] for i in sorted_indices]
q3_sales_sorted = [q3_sales[i] for i in sorted_indices]
q4_sales_sorted = [q4_sales[i] for i in sorted_indices]
avg_sales_per_quarter_sorted = avg_sales_per_quarter[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))
width = 0.2
x = np.arange(len(categories_sorted))

# Plot the sorted bar chart
ax1.bar(x - 1.5*width, q1_sales_sorted, width, color='dodgerblue', label='Q1')
ax1.bar(x - 0.5*width, q2_sales_sorted, width, color='goldenrod', label='Q2')
ax1.bar(x + 0.5*width, q3_sales_sorted, width, color='seagreen', label='Q3')
ax1.bar(x + 1.5*width, q4_sales_sorted, width, color='tomato', label='Q4')

# Set category labels
ax1.set_xticks(x)
ax1.set_xticklabels(categories_sorted)
ax1.tick_params(axis='y', labelleft=False)
ax1.legend()

# Add line plot for average sales data
ax2 = ax1.twinx()
ax2.plot(x, avg_sales_per_quarter_sorted, color='purple', linestyle='--', marker='o', markersize=8, alpha=0.7)
ax2.tick_params(axis='y', labelright=False)

plt.show()