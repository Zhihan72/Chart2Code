import matplotlib.pyplot as plt
import numpy as np

# Randomly altered day labels
days = ['Wenday', 'Thrsday', 'Mnday', 'Satrday', 'Fridy', 'Tuesay', 'Sundy']

# Sales data remains the same
apples_sales = [30, 25, 50, 55, 60, 75, 80]
bananas_sales = [40, 35, 45, 50, 55, 65, 70]
oranges_sales = [20, 25, 30, 35, 40, 50, 55]

fig, ax1 = plt.subplots(figsize=(12, 8))

y_indexes = np.arange(len(days))
height = 0.2
bar_color = 'green'

ax1.barh(y_indexes - height, apples_sales, height=height, color=bar_color)
ax1.barh(y_indexes, bananas_sales, height=height, color=bar_color)
ax1.barh(y_indexes + height, oranges_sales, height=height, color=bar_color)

# Randomly altered title and axis labels
ax1.set_title('Fruit Inventory Through the Days', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Days', fontsize=12)
ax1.set_xlabel('Units', fontsize=12)

ax1.set_yticks(y_indexes)
ax1.set_yticklabels(days)

# Annotated labels for each sale
for i, sales in enumerate(apples_sales):
    ax1.text(apples_sales[i] + 2, i - height, f'{apples_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(bananas_sales):
    ax1.text(bananas_sales[i] + 2, i, f'{bananas_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(oranges_sales):
    ax1.text(oranges_sales[i] + 2, i + height, f'{oranges_sales[i]}', va='center', fontsize=9, color=bar_color)

plt.tight_layout()
plt.show()