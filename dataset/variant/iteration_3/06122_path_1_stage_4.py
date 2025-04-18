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

fig, ax = plt.subplots(figsize=(16, 8))

x = np.arange(len(months))
bar_width = 0.10

# Changing the colors and adding border styles
colors = ['#c2c2f0', '#ff9999', '#66b3ff', '#f9d9d1', '#d9f994', '#ffb3e6', '#99ff99', '#ffcc99']

for i in range(len(categories)):
    ax.bar(x + i*bar_width, sales_data[i], width=bar_width, color=colors[i], edgecolor='black', linestyle='-', label=categories[i])

# Changing the title and label font sizes randomly
ax.set_title('Sales Overview by Month', fontsize=18, pad=15)
ax.set_ylabel('Sales (Thousand USD)', fontsize=13)
ax.set_xticks(x + bar_width * (len(categories) - 1) / 2)
ax.set_xticklabels(months, rotation=30, ha='right', fontsize=11)

# Altering legend appearance
ax.legend(title="Categories", title_fontsize='12', fontsize='10', loc='upper left')

# Randomly change grid settings
ax.grid(axis='y', linestyle='-', alpha=0.5)

plt.tight_layout()

plt.show()