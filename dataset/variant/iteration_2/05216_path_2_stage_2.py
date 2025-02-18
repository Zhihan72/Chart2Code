import matplotlib.pyplot as plt
import numpy as np

# Define the products and months
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Sales data for the 5 products over 12 months
product_sales = np.array([
    [150, 200, 300, 400, 450, 500, 550, 600, 700, 750, 800, 850],  # Product A
    [120, 190, 280, 350, 390, 450, 500, 530, 600, 640, 700, 720],  # Product B
    [100, 140, 160, 200, 220, 260, 270, 320, 340, 360, 380, 400],  # Product C
    [90, 110, 150, 180, 200, 250, 260, 300, 330, 350, 365, 380],   # Product D
    [80, 120, 150, 200, 210, 260, 300, 330, 370, 400, 430, 460]    # Product E
])

# Initialize figure
fig, ax = plt.subplots(figsize=(14, 8))

# Define the bar width
bar_width = 0.7
index = np.arange(len(months))

# Define base sales data for diverging effect
base_sales = product_sales.mean(axis=0)

# Plot each product's sales in a diverging bar chart format
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, product in enumerate(products):
    ax.bar(index, product_sales[i] - base_sales, bar_width, bottom=base_sales, color=new_colors[i], label=product)

# Customizing the plot
ax.set_title('Diverging Sales Performance of Products', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Variance in Units Sold', fontsize=14)
ax.set_xticks(index)
ax.set_xticklabels(months)
ax.legend(loc='upper left', fontsize=12, title='Products', frameon=True)

# Add a horizontal grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better visualization
plt.tight_layout()

# Show plot
plt.show()