import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

product_A_sales = np.array([10, 15, 14, 18, 20, 22, 24, 23, 21, 19, 17, 16])
product_B_sales = np.array([12, 14, 16, 19, 21, 23, 25, 26, 24, 22, 20, 18])

x_positions = np.arange(len(months))

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.25

ax.bar(x_positions - bar_width / 2, product_A_sales, width=bar_width, color='blue', edgecolor='black')
ax.bar(x_positions + bar_width / 2, product_B_sales, width=bar_width, color='green', edgecolor='black')

annotations = {
    'Mar': ('Peak Sales', (0, 30)),
    'Aug': ('Launch', (0, -50)),
    'Dec': ('Discounts', (0, 20))
}

for month, (text, offset) in annotations.items():
    index = np.where(months == month)[0][0]
    target_sales = product_B_sales[index] if month == 'Mar' else (product_A_sales[index] + product_B_sales[index]) / 2.0
    ax.annotate(
        text, 
        (x_positions[index], target_sales), 
        xytext=offset, 
        textcoords='offset points', 
        ha='center', fontsize=10, color='darkred',
        arrowprops=dict(arrowstyle='->', color='grey')
    )

ax.set_title("Sales of A & B (2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Sales (k)", fontsize=14)

ax.set_xticks(x_positions)
ax.set_xticklabels(months, fontsize=11, rotation=30, ha='right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()