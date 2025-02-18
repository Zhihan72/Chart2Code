import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents average monthly sales data of various ice cream flavors in a local shop over a year. 
# The ice cream flavors are Chocolate, Vanilla, Strawberry, Mint, and Cookie Dough.

# Ice cream flavors
flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Mint', 'Cookie Dough']

# Monthly sales data for each flavor (in hundreds of units)
chocolate_sales = [50, 55, 60, 48, 70, 85, 90, 95, 60, 55, 60, 50]
vanilla_sales = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
strawberry_sales = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
mint_sales = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
cookie_dough_sales = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Aggregate data into a NumPy array
monthly_sales = np.array([chocolate_sales, vanilla_sales, strawberry_sales, mint_sales, cookie_dough_sales])

# Calculate the average monthly sales for each flavor
average_sales = np.mean(monthly_sales, axis=1)

# Initialize the plot figure and multiple subplots for bar and line charts
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Bar plot for average monthly sales
bars = axs[0].bar(flavors, average_sales, color=['#8B4513', '#DEB887', '#FF69B4', '#98FB98', '#D2B48C'])
axs[0].set_title('Average Monthly Sales of Ice Cream Flavors', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Ice Cream Flavors', fontsize=12)
axs[0].set_ylabel('Average Monthly Sales (hundreds of units)', fontsize=12)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)
axs[0].set_ylim(0, 100)

# Adding data labels
for bar in bars:
    height = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom')

# Line plot for monthly sales trends
months = np.arange(1, 13)
colors = ['#8B4513', '#DEB887', '#FF69B4', '#98FB98', '#D2B48C']
for i, sales in enumerate(monthly_sales):
    axs[1].plot(months, sales, marker='o', color=colors[i], label=flavors[i])

axs[1].set_title('Monthly Sales Trends of Ice Cream Flavors', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('Sales (hundreds of units)', fontsize=12)
axs[1].set_xticks(months)
axs[1].legend(title='Ice Cream Flavors', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()