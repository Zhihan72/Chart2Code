import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The plot showcases the sales data of different categories of products in an online store from Q1 to Q4 of the year 2022.

# Quarters
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Categories and their corresponding sales data (in units)
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports', 'Books', 'Toys']
sales_data = {
    'Electronics': [400, 500, 300, 450],  # Sales data for Q1, Q2, Q3, Q4
    'Clothing': [350, 400, 420, 380],
    'Home & Kitchen': [300, 350, 400, 370],
    'Sports': [200, 250, 150, 200],
    'Books': [150, 140, 130, 120],
    'Toys': [100, 150, 160, 170],
}

# Colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create figure and 1x2 subplots: one for the bar chart and one for the comparison curve
fig, (ax_bar, ax_curve) = plt.subplots(1, 2, figsize=(18, 8))

# Bar chart: Sales data per quarter
x = np.arange(len(quarters))
bar_width = 0.15

for i, category in enumerate(categories):
    sales = sales_data[category]
    ax_bar.bar(x + i * bar_width, sales, bar_width, color=colors[i], label=category)

# Customize the bar chart
ax_bar.set_title("Quarterly Sales Data for 2022\nOnline Store", fontsize=16, fontweight='bold', pad=20)
ax_bar.set_xlabel("Quarters", fontsize=12)
ax_bar.set_ylabel("Sales (units)", fontsize=12)
ax_bar.set_xticks(x + bar_width * (len(categories) - 1) / 2)
ax_bar.set_xticklabels(quarters, fontsize=12)
ax_bar.legend(title="Product Categories", fontsize=10)
ax_bar.yaxis.grid(True, linestyle='--', alpha=0.5)

# Annotate the bars with sales numbers
for i, category in enumerate(categories):
    for j, value in enumerate(sales_data[category]):
        if value > 0:
            ax_bar.text(x[j] + i * bar_width, value + 10, f'{value}', ha='center', va='bottom', fontsize=9, color='black')

# Line plot: Trend comparison of categories across the quarters
for category in categories:
    sales = sales_data[category]
    ax_curve.plot(quarters, sales, marker='o', linestyle='-', label=category)

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