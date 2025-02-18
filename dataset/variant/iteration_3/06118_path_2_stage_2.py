import matplotlib.pyplot as plt
import numpy as np

products = ["T-Shirts", "Jeans", "Jackets", "Shoes", "Hats", "Scarves"]

sales_jan = [150, 120, 80, 180, 50, 40]
sales_feb = [160, 130, 85, 190, 55, 45]
sales_mar = [170, 140, 90, 200, 60, 50]
sales_apr = [180, 150, 95, 210, 65, 55]
sales_may = [190, 160, 100, 220, 70, 60]
sales_jun = [200, 170, 105, 230, 75, 65]

months = ["January", "February", "March", "April", "May", "June"]

fig, ax = plt.subplots(figsize=(12, 8))
bar_height = 0.13

r1 = np.arange(len(products))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]
r5 = [x + bar_height for x in r4]
r6 = [x + bar_height for x in r5]

ax.barh(r1, sales_jan, color='orange', height=bar_height, edgecolor='grey', label='January')
ax.barh(r2, sales_feb, color='green', height=bar_height, edgecolor='grey', label='February')
ax.barh(r3, sales_mar, color='red', height=bar_height, edgecolor='grey', label='March')
ax.barh(r4, sales_apr, color='purple', height=bar_height, edgecolor='grey', label='April')
ax.barh(r5, sales_may, color='brown', height=bar_height, edgecolor='grey', label='May')
ax.barh(r6, sales_jun, color='blue', height=bar_height, edgecolor='grey', label='June')

ax.grid(linestyle='--', alpha=0.7)

plt.title('Average Monthly Sales of Products at Frontline Outfitters (H1)', fontsize=16, pad=20)
plt.xlabel('Average Monthly Sales (Units)', fontsize=14)
plt.ylabel('Product Categories', fontsize=14)

plt.yticks([r + 2.5 * bar_height for r in r1], products)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Months', fontsize=10, frameon=False)
plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.show()