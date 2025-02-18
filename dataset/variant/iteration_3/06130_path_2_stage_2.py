import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Books', 'Clothing', 'Home & Kitchen', 'Sports & Outdoors', 'Toys', 'Beauty Products']
sales_data = {
    'Electronics': [25, 22, 27, 20, 30, 35, 40, 38, 45, 50, 55, 60],
    'Books': [15, 18, 24, 30, 22, 20, 25, 20, 15, 10, 12, 18],
    'Clothing': [20, 25, 30, 28, 35, 40, 38, 42, 50, 55, 60, 65],
    'Home & Kitchen': [18, 22, 27, 23, 25, 30, 35, 33, 37, 40, 43, 45],
    'Sports & Outdoors': [10, 15, 20, 18, 22, 25, 27, 30, 35, 40, 45, 50],
    'Toys': [5, 7, 10, 9, 14, 18, 22, 19, 21, 25, 30, 32],
    'Beauty Products': [8, 9, 15, 12, 16, 20, 25, 28, 29, 31, 35, 38]
}

# Calculate total sales for each category
total_sales = {category: sum(sales) for category, sales in sales_data.items()}

# Sort categories based on total sales
sorted_categories = sorted(total_sales, key=total_sales.get, reverse=True)

# Sort sales data according to sorted categories
sorted_sales_data = {category: sales_data[category] for category in sorted_categories}

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the sorted bar chart
y_pos = np.arange(len(sorted_categories))
sales_totals = [total_sales[category] for category in sorted_categories]
ax.barh(y_pos, sales_totals, align='center', color='skyblue')
ax.set_yticks(y_pos)
ax.set_yticklabels(sorted_categories)

ax.set_xlabel('Total Sales (in thousands of units)', fontsize=12)
ax.set_title('Total Sales for Different Product Categories in 2023', fontsize=14, fontweight='bold')

# Annotate sales values on each bar
for i, v in enumerate(sales_totals):
    ax.text(v + 1, i, str(v), va='center', fontsize=10)

plt.tight_layout()
plt.show()