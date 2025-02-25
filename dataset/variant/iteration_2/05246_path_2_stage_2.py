import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

product_A_sales = np.array([10, 15, 14, 18, 20, 22, 24, 23, 21, 19, 17, 16])
product_B_sales = np.array([12, 14, 16, 19, 21, 23, 25, 26, 24, 22, 20, 18])
product_C_sales = np.array([8, 9, 11, 13, 15, 17, 19, 20, 21, 23, 22, 21])

x_positions = np.arange(len(months))

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.25

ax.bar(x_positions - bar_width, product_A_sales, width=bar_width, color='blue', edgecolor='black')
ax.bar(x_positions, product_B_sales, width=bar_width, color='green', edgecolor='black')
ax.bar(x_positions + bar_width, product_C_sales, width=bar_width, color='red', edgecolor='black')

annotations = {
    'Mar': ('Peak Sales', (0, 30)),
    'Aug': ('Launch', (0, -50)),
    'Dec': ('Discounts', (0, 20))
}

for month, (text, offset) in annotations.items():
    index = np.where(months == month)[0][0]
    target_sales = product_B_sales[index] if month == 'Mar' else sum([
        product_A_sales[index], product_B_sales[index], product_C_sales[index]
    ]) / 3.0
    ax.annotate(
        text, 
        (x_positions[index], target_sales), 
        xytext=offset, 
        textcoords='offset points', 
        arrowprops=dict(arrowstyle='->', color='grey'),
        ha='center', fontsize=10, color='darkred'
    )

ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Sales (k)", fontsize=14)
ax.set_xticks(x_positions)
ax.set_xticklabels(months, fontsize=11, rotation=30, ha='right')

average_sales = (product_A_sales + product_B_sales + product_C_sales) / 3
ax.plot(x_positions, average_sales, color='purple', linestyle='-.', marker='o', linewidth=1.5)

plt.tight_layout()
plt.show()