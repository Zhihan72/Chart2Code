import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

product_A_sales = np.array([10, 15, 14, 18, 20, 22, 24, 23, 21, 19, 17, 16])
product_B_sales = np.array([12, 14, 16, 19, 21, 23, 25, 26, 24, 22, 20, 18])
product_C_sales = np.array([8, 9, 11, 13, 15, 17, 19, 20, 21, 23, 22, 21])

y_positions = np.arange(len(months))
bar_height = 0.25

fig, ax = plt.subplots(figsize=(10, 8))

# Consistent color 'blue' is applied to all data groups
ax.barh(y_positions - bar_height, product_A_sales, height=bar_height, color='blue', edgecolor='black')
ax.barh(y_positions, product_B_sales, height=bar_height, color='blue', edgecolor='black')
ax.barh(y_positions + bar_height, product_C_sales, height=bar_height, color='blue', edgecolor='black')

annotations = {
    'Mar': ('Peak Sales', (50, 0)),
    'Aug': ('Launch', (-60, 0)),
    'Dec': ('Discounts', (20, 0))
}

for month, (text, offset) in annotations.items():
    index = np.where(months == month)[0][0]
    target_sales = product_B_sales[index] if month == 'Mar' else sum([
        product_A_sales[index], product_B_sales[index], product_C_sales[index]
    ]) / 3.0
    ax.annotate(
        text, 
        (target_sales, y_positions[index]), 
        xytext=offset, 
        textcoords='offset points', 
        arrowprops=dict(arrowstyle='->', color='grey'),
        va='center', fontsize=10, color='darkred'
    )

ax.set_ylabel("Months", fontsize=14)
ax.set_xlabel("Sales (k)", fontsize=14)
ax.set_yticks(y_positions)
ax.set_yticklabels(months, fontsize=11)

average_sales = (product_A_sales + product_B_sales + product_C_sales) / 3
ax.plot(average_sales, y_positions, color='purple', linestyle='-.', marker='o', linewidth=1.5)

plt.tight_layout()
plt.show()