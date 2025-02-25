import matplotlib.pyplot as plt
import numpy as np

# Quarters
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Categories and their corresponding sales data (in units)
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports', 'Books', 'Toys']
sales_data = {
    'Electronics': [400, 500, 300, 450],
    'Clothing': [350, 400, 420, 380],
    'Home & Kitchen': [300, 350, 400, 370],
    'Sports': [200, 250, 150, 200],
    'Books': [150, 140, 130, 120],
    'Toys': [100, 150, 160, 170],
}

# Calculate total sales per category
total_sales = {category: sum(sales) for category, sales in sales_data.items()}

# Sort categories by total sales in descending order
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0', '#ffb3e6']
sorted_categories = sorted(total_sales, key=total_sales.get, reverse=True)
sorted_colors = [x for _, x in sorted(zip(categories, colors), key=lambda pair: total_sales[pair[0]], reverse=True)]
sorted_sales_data = [sales_data[category] for category in sorted_categories]

# Create figure and 1x2 subplots
fig, (ax_bar, ax_curve) = plt.subplots(1, 2, figsize=(18, 8))

# Bar chart: Sales data per category sorted by total sales
bar_width = 0.15
x_positions = np.arange(len(quarters))

for i, category_sales in enumerate(sorted_sales_data):
    ax_bar.bar(x_positions + i * bar_width, category_sales, bar_width, color=sorted_colors[i], label=sorted_categories[i])

# Customize the bar chart
ax_bar.set_title("Quarterly Sales Data for 2022\nOnline Store", fontsize=16, fontweight='bold', pad=20)
ax_bar.set_xlabel("Quarters", fontsize=12)
ax_bar.set_ylabel("Sales (units)", fontsize=12)
ax_bar.set_xticks(x_positions + bar_width * (len(categories) - 1) / 2)
ax_bar.set_xticklabels(quarters, fontsize=12)
ax_bar.legend(title="Product Categories", fontsize=10)
ax_bar.yaxis.grid(True, linestyle='--', alpha=0.5)

# Annotate the bars with sales numbers
for i, category_sales in enumerate(sorted_sales_data):
    for j, value in enumerate(category_sales):
        if value > 0:
            ax_bar.text(x_positions[j] + i * bar_width, value + 10, f'{value}', ha='center', va='bottom', fontsize=9, color='black')

# Line plot: Trend comparison of categories across the quarters
for i, category in enumerate(sorted_categories):
    ax_curve.plot(quarters, sales_data[category], marker='o', linestyle='-', color=sorted_colors[i], label=category)

# Customize the line plot
ax_curve.set_title("Sales Trend Comparison\nOnline Store (2022)", fontsize=16, fontweight='bold', pad=20)
ax_curve.set_xlabel("Quarters", fontsize=12)
ax_curve.set_ylabel("Sales (units)", fontsize=12)
ax_curve.legend(title="Product Categories", fontsize=10)
ax_curve.yaxis.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()