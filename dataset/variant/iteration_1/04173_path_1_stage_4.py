import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Clothing', 'Groceries', 'Household Items', 'Books']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Randomly altered sales data while preserving the original shape
sales_data = np.array([
    [130, 115, 140, 120],  # shuffled Q1 data for 'Electronics'
    [100, 80, 90, 85],     # shuffled Q2 data for 'Clothing'
    [150, 170, 160, 155],  # shuffled Q3 data for 'Groceries'
    [65, 80, 75, 70],      # shuffled Q4 data for 'Household Items'
    [60, 50, 65, 55],      # shuffled Q1 data for 'Books'
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

bar_width = 0.2
bar_positions = np.arange(len(categories))

single_color = 'skyblue'

# Plot bars for each quarter with the shuffled data
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