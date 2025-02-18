import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Children', 'History']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthly_sales = np.array([
    [50, 30, 20, 30],
    [60, 35, 18, 33],
    [70, 40, 22, 35],
    [80, 45, 25, 40],
    [90, 50, 28, 42],
    [105, 55, 30, 45],
    [120, 60, 32, 48],
    [140, 70, 35, 50],
    [160, 80, 38, 52],
    [180, 90, 40, 55],
    [200, 100, 42, 58],
    [220, 110, 45, 60]
])

bar_colors = ['#FF9999', '#FFD700', '#99FF99', '#66B2FF']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
x_indices = np.arange(len(months))

for i, color in enumerate(bar_colors):
    ax.bar(x_indices + i * bar_width, monthly_sales[:, i], color=color, edgecolor='black', width=bar_width)

ax.set_xticks(x_indices + bar_width * (len(genres) - 1) / 2)
ax.set_yticks(np.arange(0, 250, 25))

ax.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.show()