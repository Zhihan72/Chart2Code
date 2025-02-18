import matplotlib.pyplot as plt
import numpy as np

# Categories and corresponding sales data over 6 months
categories = ["Elec", "Fash", "Home", "Beauty", "Toys", "Books"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Sales data in thousands USD
sales_data = [
    [120, 110, 105, 100, 95, 110],  # Electronics
    [80, 85, 90, 85, 80, 75],       # Fashion
    [50, 55, 60, 65, 70, 75],       # Home Goods
    [30, 35, 40, 45, 50, 55],       # Beauty
    [20, 30, 25, 35, 30, 40],       # Toys
    [10, 15, 20, 25, 30, 35]        # Books
]

sales_data = np.array(sales_data)

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(len(months))
bar_width = 0.15
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

for i in range(len(categories)):
    ax.bar(x + i*bar_width, sales_data[i], width=bar_width, color=colors[i], edgecolor='grey', label=categories[i])

ax.set_title('Monthly Sales Analysis', fontsize=16, pad=20)
ax.set_ylabel('Sales (k USD)', fontsize=14)
ax.set_xticks(x + bar_width * (len(categories) - 1) / 2)
ax.set_xticklabels(months, rotation=45, ha='right', fontsize=12)

ax.legend(title="Cat", title_fontsize='13', fontsize='11')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()