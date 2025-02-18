import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

apples_sales = [30, 25, 50, 55, 60, 75, 80]
bananas_sales = [40, 35, 45, 50, 55, 65, 70]
oranges_sales = [20, 25, 30, 35, 40, 50, 55]
grapes_sales = [10, 15, 20, 25, 30, 40, 45]

fig, ax1 = plt.subplots(figsize=(12, 8))

y_indexes = np.arange(len(days))
height = 0.2
bar_color = 'green'

ax1.barh(y_indexes - 1.5 * height, apples_sales, height=height, color=bar_color)
ax1.barh(y_indexes - 0.5 * height, bananas_sales, height=height, color=bar_color)
ax1.barh(y_indexes + 0.5 * height, oranges_sales, height=height, color=bar_color)
ax1.barh(y_indexes + 1.5 * height, grapes_sales, height=height, color=bar_color)

ax2 = ax1.twiny()  # Maintained the secondary axis (though not used)

ax1.set_title('Fruit Sales and Prices in a Local Market Over a Week', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Day of the Week', fontsize=12)
ax1.set_xlabel('Number of Units Sold', fontsize=12)

ax1.set_yticks(y_indexes)
ax1.set_yticklabels(days)

for i, sales in enumerate(apples_sales):
    ax1.text(apples_sales[i] + 2, i - 1.5 * height, f'{apples_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(bananas_sales):
    ax1.text(bananas_sales[i] + 2, i - 0.5 * height, f'{bananas_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(oranges_sales):
    ax1.text(oranges_sales[i] + 2, i + 0.5 * height, f'{oranges_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(grapes_sales):
    ax1.text(grapes_sales[i] + 2, i + 1.5 * height, f'{grapes_sales[i]}', va='center', fontsize=9, color=bar_color)

plt.tight_layout()
plt.show()