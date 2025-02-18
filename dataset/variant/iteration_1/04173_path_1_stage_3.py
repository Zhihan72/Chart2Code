import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Clothing', 'Groceries', 'Household Items', 'Books']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

sales_data = np.array([
    [120, 130, 115, 140],
    [80, 90, 85, 100],
    [150, 160, 155, 170],
    [70, 75, 65, 80],
    [50, 55, 60, 65],
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

bar_width = 0.2
bar_positions = np.arange(len(categories))

single_color = 'skyblue'

for i, quarter in enumerate(quarters):
    ax1.bar(bar_positions + i * bar_width, sales_data[:, i], width=bar_width, color=single_color)

ax1.set_xticks(bar_positions + bar_width * 1.5)
ax1.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5, color='gray')

annual_sales = np.sum(sales_data, axis=1)
ax2.bar(categories, annual_sales, color=single_color, linestyle='--', edgecolor='gray')

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()