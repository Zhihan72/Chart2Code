import numpy as np
import matplotlib.pyplot as plt

# Data: Monthly Sales of Various Ice Cream Flavors in "Sweet Delight" (2022)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Cookies and Cream']

# Define sales data in thousand units
vanilla_sales = np.array([12, 15, 13, 14, 18, 22, 30, 28, 25, 20, 18, 16])
chocolate_sales = np.array([10, 12, 11, 13, 15, 17, 25, 23, 19, 17, 16, 15])
strawberry_sales = np.array([8, 10, 9, 10, 11, 12, 20, 18, 15, 13, 12, 11])
cookies_cream_sales = np.array([5, 6, 5, 6, 8, 9, 14, 13, 12, 10, 9, 8])

# Stack sales data together for plotting
sales_data = np.vstack([vanilla_sales, chocolate_sales, strawberry_sales, cookies_cream_sales])

colors = ['#FFDDC1', '#D4E157', '#FF80AB', '#FFC107']

fig, ax = plt.subplots(figsize=(14, 8))

# Stacked bar chart plotting
bottoms = np.zeros(len(months))
for sales, color in zip(sales_data, colors):
    ax.bar(months, sales, color=color, edgecolor='black', bottom=bottoms)
    bottoms += sales

# Add title and labels
ax.set_title("Monthly Sales of Ice Cream Flavors in 'Sweet Delight' (2022)", fontsize=18, fontweight='bold')
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Sales (thousand units)", fontsize=14)

# Annotate bars with sales numbers
for bar in ax.patches:
    ax.annotate(f'{bar.get_height():.0f}', 
                (bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height() / 2), 
                ha='center', va='center', fontsize=10, color='black', 
                fontweight='bold', rotation=0)

# Adjust layout
plt.tight_layout()
plt.show()