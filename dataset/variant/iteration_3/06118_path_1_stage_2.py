import matplotlib.pyplot as plt
import numpy as np

products = ["T-Shirts", "Jeans", "Jackets", "Shoes", "Hats", "Scarves"]

sales_jan = [150, 120, 80, 180, 50, 40]
sales_feb = [160, 130, 85, 190, 55, 45]
sales_mar = [170, 140, 90, 200, 60, 50]
sales_apr = [180, 150, 95, 210, 65, 55]
sales_may = [190, 160, 100, 220, 70, 60]

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.15

r1 = np.arange(len(products))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]
r5 = [x + bar_height for x in r4]

bar1 = ax.barh(r1, sales_jan, color='blue', height=bar_height, edgecolor='grey', label='January')
bar2 = ax.barh(r2, sales_feb, color='orange', height=bar_height, edgecolor='grey', label='February')
bar3 = ax.barh(r3, sales_mar, color='green', height=bar_height, edgecolor='grey', label='March')
bar4 = ax.barh(r4, sales_apr, color='red', height=bar_height, edgecolor='grey', label='April')
bar5 = ax.barh(r5, sales_may, color='purple', height=bar_height, edgecolor='grey', label='May')

ax.grid(linestyle='--', alpha=0.7)

plt.title('Average Monthly Sales of Products at Frontline Outfitters (H1)', fontsize=16, pad=20)
plt.ylabel('Product Categories', fontsize=14)
plt.xlabel('Average Monthly Sales (Units)', fontsize=14)

plt.yticks([r + 2 * bar_height for r in r1], products)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Months', fontsize=10, frameon=False)

plt.tight_layout(rect=[0, 0, 0.9, 1])

plt.show()