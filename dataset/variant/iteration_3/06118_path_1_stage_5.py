import matplotlib.pyplot as plt
import numpy as np

products = ["Caps", "Dresses", "Pants", "Boots", "Gloves", "Belts"]  # Shuffled product names

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

bar1 = ax.barh(r1, sales_jan, color='violet', height=bar_height, edgecolor='black', label='Month 1')
bar2 = ax.barh(r2, sales_feb, color='skyblue', height=bar_height, edgecolor='black', label='Month 2')
bar3 = ax.barh(r3, sales_mar, color='gold', height=bar_height, edgecolor='black', label='Month 3')
bar4 = ax.barh(r4, sales_apr, color='lime', height=bar_height, edgecolor='black', label='Month 4')
bar5 = ax.barh(r5, sales_may, color='salmon', height=bar_height, edgecolor='black', label='Month 5')

ax.grid(linestyle='-', linewidth=0.5, alpha=0.8, color='grey')

plt.title('Variable Sales Data of Items at Fashion Hub (Q1)', fontsize=16, pad=20)  # Changed title
plt.ylabel('Item Types', fontsize=14)  # Changed y-axis label
plt.xlabel('Monthly Sales (Units)', fontsize=14)  # Changed x-axis label

plt.yticks([r + 2 * bar_height for r in r1], products)

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Sales Periods', fontsize=12, frameon=True, shadow=True)  # Changed legend title
plt.tight_layout(rect=[0, 0, 0.9, 1])

plt.show()