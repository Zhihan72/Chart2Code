import matplotlib.pyplot as plt
import numpy as np

products = ["Jeans", "Hats", "T-Shirts", "Scarves", "Shoes", "Jackets"]

# Manually altering sales data within each array while maintaining the original structure
sales_jan = [150, 180, 80, 120, 50, 40]  # shuffled values
sales_feb = [130, 160, 55, 190, 45, 85]  # shuffled values
sales_mar = [140, 170, 60, 200, 50, 90]  # shuffled values
sales_apr = [150, 180, 65, 210, 95, 55]  # shuffled values
sales_may = [160, 190, 70, 220, 100, 60] # shuffled values
sales_jun = [170, 200, 75, 230, 65, 105] # shuffled values

months = ["January", "February", "March", "April", "May", "June"]

fig, ax = plt.subplots(figsize=(12, 8))
bar_height = 0.13

r1 = np.arange(len(products))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]
r5 = [x + bar_height for x in r4]
r6 = [x + bar_height for x in r5]

ax.barh(r1, sales_jan, color='orchid', height=bar_height, edgecolor='darkblue', label='January')
ax.barh(r2, sales_feb, color='slateblue', height=bar_height, edgecolor='darkgreen', label='February')
ax.barh(r3, sales_mar, color='coral', height=bar_height, edgecolor='darkred', label='March')
ax.barh(r4, sales_apr, color='lime', height=bar_height, edgecolor='darkviolet', label='April')
ax.barh(r5, sales_may, color='teal', height=bar_height, edgecolor='maroon', label='May')
ax.barh(r6, sales_jun, color='gold', height=bar_height, edgecolor='darkgoldenrod', label='June')

ax.grid(linewidth=0.5, linestyle=':', color='grey')

plt.title('Frontline Outfitters: Sales Product Monthly Average (H1)', fontsize=16, pad=15, color='darkred')
plt.xlabel('Monthly Average Product Sales (Units)', fontsize=14, color='navy')
plt.ylabel('Category of Product', fontsize=14, color='darkgreen')

plt.yticks([r + 2.5 * bar_height for r in r1], products)

plt.legend(loc='lower right', title='Months', fontsize=10, frameon=True, facecolor='lightgrey')
plt.tight_layout(rect=[0, 0, 0.95, 1])
plt.show()