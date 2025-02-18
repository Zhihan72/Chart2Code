import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors
flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Cookie Dough']

# Monthly sales data for each flavor (in hundreds of units)
chocolate_sales = [50, 55, 60, 48, 70, 85, 90, 95, 60, 55, 60, 50]
vanilla_sales = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
strawberry_sales = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
cookie_dough_sales = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Aggregate the data into a NumPy array without mint sales
monthly_sales = np.array([chocolate_sales, vanilla_sales, strawberry_sales, cookie_dough_sales])

# Calculate the average monthly sales for each flavor
average_sales = np.mean(monthly_sales, axis=1)

# Change the subplot arrangement to 2 rows and 1 column
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Bar plot for average monthly sales with new colors
bars = axs[0].bar(flavors, average_sales, color=['#FF5733', '#33FF57', '#3357FF', '#A133FF'])
axs[0].set_title('Average Monthly Sales of Ice Cream Flavors', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Ice Cream Flavors', fontsize=12)
axs[0].set_ylabel('Average Monthly Sales (hundreds of units)', fontsize=12)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)
axs[0].set_ylim(0, 100)

# Adding data labels
for bar in bars:
    height = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom')

# Line plot for monthly sales trends with new colors
months = np.arange(1, 13)
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#A133FF']
for i, sales in enumerate(monthly_sales):
    axs[1].plot(months, sales, marker='o', color=new_colors[i], label=flavors[i])

axs[1].set_title('Monthly Sales Trends of Ice Cream Flavors', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('Sales (hundreds of units)', fontsize=12)
axs[1].set_xticks(months)
axs[1].legend(title='Ice Cream Flavors', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()