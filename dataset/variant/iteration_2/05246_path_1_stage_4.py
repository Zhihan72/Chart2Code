import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

product_A_sales = np.array([10, 15, 14, 18, 20, 22, 24, 23, 21, 19, 17, 16])
product_B_sales = np.array([12, 14, 16, 19, 21, 23, 25, 26, 24, 22, 20, 18])

y_positions = np.arange(len(months))

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.25

ax.barh(y_positions - bar_height / 2, product_A_sales, height=bar_height, color='blue', edgecolor='black', label='Product A')
ax.barh(y_positions + bar_height / 2, product_B_sales, height=bar_height, color='green', edgecolor='black', label='Product B')

annotations = {
    'Mar': ('Peak Sales', (35, 0)),
    'Aug': ('Launch', (-50, 0)),
    'Dec': ('Discounts', (20, 0))
}

for month, (text, offset) in annotations.items():
    index = np.where(months == month)[0][0]
    target_sales = product_B_sales[index] if month == 'Mar' else (product_A_sales[index] + product_B_sales[index]) / 2.0
    ax.annotate(
        text, 
        (target_sales, y_positions[index]), 
        xytext=offset, 
        textcoords='offset points', 
        va='center', fontsize=10, color='darkred',
        arrowprops=dict(arrowstyle='->', color='grey')
    )

ax.set_title("Sales of A & B (2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Month", fontsize=14)
ax.set_xlabel("Sales (k)", fontsize=14)

ax.set_yticks(y_positions)
ax.set_yticklabels(months, fontsize=11)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.legend()

plt.tight_layout()
plt.show()