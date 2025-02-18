import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Clothing', 'Groceries', 'Household Items', 'Books']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

sales_data = np.array([
    [130, 115, 140, 120],
    [100, 80, 90, 85],
    [150, 170, 160, 155],
    [65, 80, 75, 70],
    [60, 50, 65, 55],
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

bar_height = 0.2
bar_positions = np.arange(len(categories))

single_color = 'skyblue'

for i, quarter in enumerate(quarters):
    ax1.barh(bar_positions + i * bar_height, sales_data[:, i], height=bar_height, color=single_color)

ax1.set_yticks(bar_positions + bar_height * 1.5)
ax1.set_yticklabels(categories)
ax1.grid(True, which='major', axis='x', linestyle='--', linewidth=0.5, color='gray')

annual_sales = np.sum(sales_data, axis=1)
ax2.barh(categories, annual_sales, color=single_color, linestyle='--', edgecolor='gray')

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()