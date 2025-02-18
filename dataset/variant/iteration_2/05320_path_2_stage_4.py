import matplotlib.pyplot as plt
import numpy as np

product_categories = ['Smartphones', 'Laptops', 'Wearables', 'Accessories']
sales_data = np.array([
    [500, 600, 700, 800, 850, 900],
    [450, 475, 500, 520, 570, 600],
    [200, 220, 250, 270, 290, 310],
    [150, 180, 190, 200, 220, 230]
])
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Calculate total sales for each product category
total_sales = sales_data.sum(axis=1)

# Sort indices based on total sales in descending order
sorted_indices = np.argsort(-total_sales)

# Sort categories and data based on sorted indices
sorted_categories = [product_categories[i] for i in sorted_indices]
sorted_sales_data = sales_data[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15
x_positions = np.arange(len(months))
bar_color = 'steelblue'

# Plot the sorted bar chart
for i, category in enumerate(sorted_categories):
    ax.bar(x_positions + i * bar_width, sorted_sales_data[i], bar_width, label=category, color=bar_color)

ax.set_xlabel('Product Categories', fontsize=14, weight='bold')
ax.set_ylabel('Units Sold', fontsize=14, weight='bold')
ax.set_title('Sorted Startup Sales by Product Category for 2023', fontsize=16, weight='bold', pad=20)
ax.set_xticks(x_positions + bar_width * (len(sorted_categories) - 1) / 2)
ax.set_xticklabels(months, fontsize=12)

# Add labels on top of each bar
for i, category_data in enumerate(sorted_sales_data):
    for j, sale in enumerate(category_data):
        ax.text(x_positions[j] + i * bar_width, sale + 5, f'{sale}', ha='center', va='bottom', fontsize=10, rotation=90)

plt.legend()
plt.tight_layout()
plt.show()