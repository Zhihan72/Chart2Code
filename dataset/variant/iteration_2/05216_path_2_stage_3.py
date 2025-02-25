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

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.7
index = np.arange(len(months))
base_sales = product_sales.mean(axis=0)

new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, product in enumerate(products):
    ax.bar(index, product_sales[i] - base_sales, bar_width, bottom=base_sales, color=new_colors[i])

ax.set_xticks(index)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()