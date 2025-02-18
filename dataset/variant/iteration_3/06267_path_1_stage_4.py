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

for i, (genre, color) in enumerate(zip(genres, bar_colors)):
    ax.bar(x_indices + i * bar_width, monthly_sales[:, i], color=color, edgecolor='black',
           width=bar_width, label=genre)

ax.set_title('Book Haven Monthly Sales by Genre (2023)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Months', fontsize=12, color='darkred')
ax.set_ylabel('Sales (Number of Books)', fontsize=12, color='darkred')

ax.set_xticks(x_indices + bar_width * (len(genres) - 1) / 2)
ax.set_xticklabels(months, fontsize=11, rotation=45)
ax.set_yticks(np.arange(0, 250, 25))

ax.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)

ax.legend(loc='upper left', fontsize=9, frameon=True, shadow=True, ncol=1)

plt.tight_layout()
plt.show()