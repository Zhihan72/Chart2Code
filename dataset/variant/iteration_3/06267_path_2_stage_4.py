import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Children']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthly_sales = np.array([
    [50, 30, 20],
    [60, 35, 18],
    [70, 40, 22],
    [80, 45, 25],
    [90, 50, 28],
    [105, 55, 30],
    [120, 60, 32],
    [140, 70, 35],
    [160, 80, 38],
    [180, 90, 40],
    [200, 100, 42],
    [220, 110, 45]
])

bar_colors = ['#66B2FF', '#FFD700', '#FFCC99']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
x = np.arange(len(months))

for i, color in enumerate(bar_colors):
    ax.bar(x + i * bar_width, monthly_sales[:, i], color=color, edgecolor='grey',
           width=bar_width, alpha=0.7)

ax.set_xticks(x + bar_width * (len(genres) - 1) / 2)
ax.set_yticks(np.arange(0, 300, 20))
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()