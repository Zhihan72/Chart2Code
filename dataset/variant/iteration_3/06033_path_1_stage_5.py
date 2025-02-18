import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors
flavors = ['Choc', 'Van', 'Straw', 'Mint', 'C.Dough', 'Coffee', 'Caramel']

# Monthly sales data for each flavor
chocolate_sales = [50, 55, 60, 48, 70, 85, 90, 95, 60, 55, 60, 50]
vanilla_sales = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
strawberry_sales = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
mint_sales = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
cookie_dough_sales = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# New flavors sales data
coffee_sales = [25, 30, 35, 40, 45, 50, 55, 60, 40, 35, 30, 25]
caramel_sales = [40, 45, 50, 55, 60, 65, 70, 75, 50, 45, 40, 35]

monthly_sales = np.array([chocolate_sales, vanilla_sales, strawberry_sales, mint_sales, cookie_dough_sales, coffee_sales, caramel_sales])

average_sales = np.mean(monthly_sales, axis=1)

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Apply a single color for all data groups
single_color = '#4682B4'

# Line plot for monthly sales trends
months = np.arange(1, 13)
for sales in monthly_sales:
    axs[0].plot(months, sales, marker='o', color=single_color)

axs[0].set_title('Monthly Trends', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Month', fontsize=12)
axs[0].set_ylabel('Sales (hundreds)', fontsize=12)
axs[0].set_xticks(months)
axs[0].legend(title='Flavors', labels=flavors, fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Horizontal bar plot for average monthly sales
bars = axs[1].barh(flavors, average_sales, color=single_color)
axs[1].set_title('Avg Sales', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Avg Sales (hundreds)', fontsize=12)
axs[1].set_ylabel('Flavors', fontsize=12)
axs[1].grid(axis='x', linestyle='--', alpha=0.7)
axs[1].set_xlim(0, 100)

# Adding data labels
for bar in bars:
    width = bar.get_width()
    axs[1].text(width, bar.get_y() + bar.get_height() / 2.0, f'{int(width)}', va='center', ha='left')

plt.tight_layout()
plt.show()