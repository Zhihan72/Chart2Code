import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors
flavors = ['Choc', 'Van', 'Straw', 'Mint', 'C.Dough']

# Monthly sales data for each flavor
chocolate_sales = [50, 55, 60, 48, 70, 85, 90, 95, 60, 55, 60, 50]
vanilla_sales = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
strawberry_sales = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
mint_sales = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
cookie_dough_sales = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

monthly_sales = np.array([chocolate_sales, vanilla_sales, strawberry_sales, mint_sales, cookie_dough_sales])

average_sales = np.mean(monthly_sales, axis=1)

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Horizontal bar plot for average monthly sales
bars = axs[0].barh(flavors, average_sales, color=['#8B4513', '#DEB887', '#FF69B4', '#98FB98', '#D2B48C'])
axs[0].set_title('Avg Sales', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Avg Sales (hundreds)', fontsize=12)
axs[0].set_ylabel('Flavors', fontsize=12)
axs[0].grid(axis='x', linestyle='--', alpha=0.7)
axs[0].set_xlim(0, 100)

# Adding data labels
for bar in bars:
    width = bar.get_width()
    axs[0].text(width, bar.get_y() + bar.get_height() / 2.0, f'{int(width)}', va='center', ha='left')

# Line plot for monthly sales trends
months = np.arange(1, 13)
colors = ['#8B4513', '#DEB887', '#FF69B4', '#98FB98', '#D2B48C']
for i, sales in enumerate(monthly_sales):
    axs[1].plot(months, sales, marker='o', color=colors[i], label=flavors[i])

axs[1].set_title('Monthly Trends', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('Sales (hundreds)', fontsize=12)
axs[1].set_xticks(months)
axs[1].legend(title='Flavors', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()