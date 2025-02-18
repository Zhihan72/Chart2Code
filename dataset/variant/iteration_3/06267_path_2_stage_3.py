import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Children', 'Science', 'History']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthly_sales = np.array([
    [50, 30, 20, 25, 30],
    [60, 35, 18, 22, 33],
    [70, 40, 22, 27, 35],
    [80, 45, 25, 30, 40],
    [90, 50, 28, 32, 42],
    [105, 55, 30, 35, 45],
    [120, 60, 32, 37, 48],
    [140, 70, 35, 40, 50],
    [160, 80, 38, 42, 52],
    [180, 90, 40, 45, 55],
    [200, 100, 42, 47, 58],
    [220, 110, 45, 50, 60]
])

bar_colors = ['#66B2FF', '#FFD700', '#FFCC99', '#99FF99', '#FF9999']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x = np.arange(len(months))

for i, color in enumerate(bar_colors):
    ax.bar(x + i * bar_width, monthly_sales[:, i], color=color, edgecolor='grey',
           width=bar_width, alpha=0.7)

ax.set_xticks(x + bar_width * (len(genres) - 1) / 2)
ax.set_yticks(np.arange(0, 300, 20))
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()