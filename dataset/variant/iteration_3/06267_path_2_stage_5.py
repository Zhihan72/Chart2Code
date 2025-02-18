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

bar_colors = ['#FF8C00', '#ADFF2F', '#FF69B4']  # Changed bar color

fig, ax = plt.subplots(figsize=(12, 7))  # Changed figure size

bar_width = 0.25  # Changed bar width
x = np.arange(len(months))

for i, color in enumerate(bar_colors):
    ax.bar(x + i * bar_width, monthly_sales[:, i], color=color,
           edgecolor='black', linewidth=1, width=bar_width, alpha=0.8)  # Changed edge color and properties

ax.set_xticks(x + bar_width * (len(genres) - 1) / 2)
ax.set_yticks(np.arange(0, 250, 25))  # Changed y-axis tick spacing
ax.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)  # Changed grid style

ax.spines['top'].set_visible(False)  # Remove top border
ax.spines['right'].set_linewidth(0.5)  # Change right border thickness

# Add legend with different location and altered styling
ax.legend(genres, loc='upper left', frameon=False, title='Book Genres', title_fontsize='13')

plt.tight_layout()
plt.show()