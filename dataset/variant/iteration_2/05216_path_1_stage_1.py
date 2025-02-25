import matplotlib.pyplot as plt
import numpy as np

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

product_sales = np.array([
    [150, 200, 300, 400, 450, 500, 550, 600, 700, 750, 800, 850],
    [120, 190, 280, 350, 390, 450, 500, 530, 600, 640, 700, 720],
    [100, 140, 160, 200, 220, 260, 270, 320, 340, 360, 380, 400],
    [90, 110, 150, 180, 200, 250, 260, 300, 330, 350, 365, 380],
    [80, 120, 150, 200, 210, 260, 300, 330, 370, 400, 430, 460]
])

cumulative_sales = np.cumsum(product_sales, axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

index = np.arange(len(months))
colors = ['#FF6347', '#FFD700', '#4B0082', '#98FB98', '#9370DB']

for i, product in enumerate(products):
    if i == 0:
        ax.bar(index, product_sales[i], 0.7, color=colors[i])
    else:
        ax.bar(index, product_sales[i], 0.7, bottom=cumulative_sales[i-1], color=colors[i])
        
ax.set_title('Monthly Sales Performance of Top Products\n(Units Sold)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Units Sold', fontsize=14)
ax.set_xticks(index)
ax.set_xticklabels(months)

for i, product in enumerate(products):
    for j in range(len(months)):
        height = product_sales[i][j]
        bottom = cumulative_sales[i-1][j] if i > 0 else 0
        if height > 0:
            ax.annotate(f'{int(height)}',
                        xy=(j, bottom + height / 2),
                        xytext=(0, 0),
                        textcoords="offset points",
                        ha='center', va='center',
                        fontsize=9, color='black', fontweight='bold')

plt.show()