import numpy as np
import matplotlib.pyplot as plt

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Cookies and Cream']

vanilla_sales = np.array([12, 15, 13, 14, 18, 22, 30, 28, 25, 20, 18, 16])
chocolate_sales = np.array([10, 12, 11, 13, 15, 17, 25, 23, 19, 17, 16, 15])
strawberry_sales = np.array([8, 10, 9, 10, 11, 12, 20, 18, 15, 13, 12, 11])
cookies_cream_sales = np.array([5, 6, 5, 6, 8, 9, 14, 13, 12, 10, 9, 8])

sales_data = np.vstack([vanilla_sales, chocolate_sales, strawberry_sales, cookies_cream_sales])
colors = ['#FF80AB', '#D4E157', '#FFDDC1', '#FFC107']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
x_indices = np.arange(len(months))

for i, (sales, color) in enumerate(zip(sales_data, colors)):
    ax.bar(x_indices + i * bar_width, sales, color=color, edgecolor='black', width=bar_width, label=flavors[i])

ax.set_title("Monthly Sales of Ice Cream Flavors in 'Sweet Delight' (2022)", fontsize=18, fontweight='bold')
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Sales (thousand units)", fontsize=14)
ax.set_xticks(x_indices + bar_width * 1.5)
ax.set_xticklabels(months)
ax.legend(title="Flavors")

plt.tight_layout()
plt.show()