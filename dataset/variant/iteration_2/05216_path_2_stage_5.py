import matplotlib.pyplot as plt
import numpy as np

products = ['Product A', 'Product B', 'Product C', 'Product D']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

product_sales = np.array([
    [150, 200, 300, 400, 450, 500, 550, 600, 700, 750, 800, 850],
    [120, 190, 280, 350, 390, 450, 500, 530, 600, 640, 700, 720],
    [100, 140, 160, 200, 220, 260, 270, 320, 340, 360, 380, 400],
    [90, 110, 150, 180, 200, 250, 260, 300, 330, 350, 365, 380]
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.7
index = np.arange(len(months))
base_sales = product_sales.mean(axis=0)

new_colors = ['#d62728', '#2ca02c', '#ff7f0e', '#1f77b4']  # Changed colors

for i, product in enumerate(products):
    ax.bar(index, product_sales[i] - base_sales, bar_width, bottom=base_sales, 
           color=new_colors[i], linestyle='dotted', edgecolor='black')  # Added linestyle and edge color

ax.set_xticks(index)

ax.yaxis.grid(False)  # Removed grid line configuration
ax.legend(products, loc='upper right', frameon=False)  # Added legend with no frame
plt.tight_layout()
plt.show()