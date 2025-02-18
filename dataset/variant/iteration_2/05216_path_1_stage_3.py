import matplotlib.pyplot as plt
import numpy as np

product_sales = np.array([
    [150, 200, 300, 400, 450, 500, 550, 600, 700, 750, 800, 850],
    [120, 190, 280, 350, 390, 450, 500, 530, 600, 640, 700, 720],
    [100, 140, 160, 200, 220, 260, 270, 320, 340, 360, 380, 400],
    [90, 110, 150, 180, 200, 250, 260, 300, 330, 350, 365, 380],
    [80, 120, 150, 200, 210, 260, 300, 330, 370, 400, 430, 460]
])

cumulative_sales = np.cumsum(product_sales, axis=0)
colors = ['#4B0082', '#98FB98', '#FF6347', '#9370DB', '#FFD700']

fig, ax = plt.subplots(figsize=(14, 8))
index = np.arange(12)

for i in range(len(product_sales)):
    if i == 0:
        ax.bar(index, product_sales[i], 0.7, color=colors[i])
    else:
        ax.bar(index, product_sales[i], 0.7, bottom=cumulative_sales[i-1], color=colors[i])

plt.show()