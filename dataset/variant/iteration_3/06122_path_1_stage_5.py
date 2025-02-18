import matplotlib.pyplot as plt
import numpy as np

categories = ["Elec", "Fash", "Home", "Beauty", "Toys", "Books", "Grocery", "Health"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_data = [
    [120, 110, 105, 100, 95, 110],  # Electronics
    [80, 85, 90, 85, 80, 75],       # Fashion
    [50, 55, 60, 65, 70, 75],       # Home Goods
    [30, 35, 40, 45, 50, 55],       # Beauty
    [20, 30, 25, 35, 30, 40],       # Toys
    [10, 15, 20, 25, 30, 35],       # Books
    [60, 55, 50, 65, 55, 60],       # Grocery
    [45, 50, 55, 50, 60, 65]        # Health
]

sales_data = np.array(sales_data)

fig, ax = plt.subplots(figsize=(12, 10))

y = np.arange(len(months))
bar_height = 0.10

colors = ['#c2c2f0', '#ff9999', '#66b3ff', '#f9d9d1', '#d9f994', '#ffb3e6', '#99ff99', '#ffcc99']

for i in range(len(categories)):
    ax.barh(y + i*bar_height, sales_data[i], height=bar_height, color=colors[i], edgecolor='black', linestyle='-', label=categories[i])

ax.set_title('Sales Overview by Month', fontsize=18, pad=15)
ax.set_xlabel('Sales (Thousand USD)', fontsize=13)
ax.set_yticks(y + bar_height * (len(categories) - 1) / 2)
ax.set_yticklabels(months, fontsize=11)

ax.legend(title="Categories", title_fontsize='12', fontsize='10', loc='upper right')

ax.grid(axis='x', linestyle='-', alpha=0.5)

plt.tight_layout()

plt.show()