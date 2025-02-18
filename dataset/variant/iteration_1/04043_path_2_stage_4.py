import matplotlib.pyplot as plt
import numpy as np

# Original categories and sales data
categories = ['Beauty', 'Sports', 'Toys', 'Electronics', 'Home & Kitchen', 'Clothing']
sales_q1 = np.array([150, 200, 130, 120, 170, 90])
sales_q2 = np.array([180, 210, 140, 130, 160, 100])
sales_q3 = np.array([170, 220, 150, 110, 180, 95])

# Calculate total sales per category
total_sales = sales_q1 + sales_q2 + sales_q3

# Sort categories and sales data based on total sales (descending order)
sorted_indices = np.argsort(total_sales)[::-1]
categories_sorted = [categories[i] for i in sorted_indices]
sales_q1_sorted = sales_q1[sorted_indices]
sales_q2_sorted = sales_q2[sorted_indices]
sales_q3_sorted = sales_q3[sorted_indices]

# Plotting the sorted bar chart
fig, ax = plt.subplots(figsize=(14, 8))
width = 0.25
x = np.arange(len(categories_sorted))

bars1 = ax.bar(x - width, sales_q1_sorted, width, color='skyblue', edgecolor='black', label='Q1')
bars2 = ax.bar(x, sales_q2_sorted, width, color='lightcoral', edgecolor='black', label='Q2')
bars3 = ax.bar(x + width, sales_q3_sorted, width, color='lightgreen', edgecolor='black', label='Q3')

for bar in bars1 + bars2 + bars3:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom')

ax.set_xlabel('Product Segments', fontsize=12)
ax.set_ylabel('Units Sold (in thousands)', fontsize=12)
ax.set_title('Sales Overview for 2023\nSorted by Total Sales (Descending)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories_sorted, rotation=45, ha='right')

ax.yaxis.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.legend()

plt.tight_layout()
plt.show()