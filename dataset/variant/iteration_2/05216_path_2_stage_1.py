import matplotlib.pyplot as plt
import numpy as np

# Define the products and months
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Sales data for the 5 products over 12 months (in units sold)
product_sales = np.array([
    [150, 200, 300, 400, 450, 500, 550, 600, 700, 750, 800, 850],  # Product A
    [120, 190, 280, 350, 390, 450, 500, 530, 600, 640, 700, 720],  # Product B
    [100, 140, 160, 200, 220, 260, 270, 320, 340, 360, 380, 400],  # Product C
    [90, 110, 150, 180, 200, 250, 260, 300, 330, 350, 365, 380],   # Product D
    [80, 120, 150, 200, 210, 260, 300, 330, 370, 400, 430, 460]    # Product E
])

# Calculate cumulative sales totals for stacked bar chart
cumulative_sales = np.cumsum(product_sales, axis=0)

# Initialize figure
fig, ax = plt.subplots(figsize=(14, 8))

# Define the bar width
bar_width = 0.7
index = np.arange(len(months))

# Plot each product's sales in a stacked bar format with new colors
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

bars = []
for i, product in enumerate(products):
    if i == 0:
        bars.append(ax.bar(index, product_sales[i], bar_width, color=new_colors[i], label=product))
    else:
        bars.append(ax.bar(index, product_sales[i], bar_width, bottom=cumulative_sales[i-1], color=new_colors[i], label=product))

# Customizing the plot
ax.set_title('Monthly Sales Performance of Top Products\n(Units Sold)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Units Sold', fontsize=14)
ax.set_xticks(index)
ax.set_xticklabels(months)
ax.legend(loc='upper left', fontsize=12, title='Products', frameon=True)

# Adding annotations to bars
for bar_list in bars:
    for bar in bar_list:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{int(height)}',
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                        xytext=(0, 0),
                        textcoords="offset points",
                        ha='center', va='center',
                        fontsize=9, color='black', fontweight='bold')

# Add a horizontal grid to improve readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Show plot
plt.show()