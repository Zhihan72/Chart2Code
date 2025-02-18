import matplotlib.pyplot as plt
import numpy as np

genres = ['Mystery', 'Romance', 'Science Fiction', 'Fantasy', 'Non-fiction']
monthly_sales = np.array([
    [120, 130, 140, 150, 160, 170],
    [200, 190, 220, 210, 230, 240],
    [180, 175, 190, 185, 195, 200],
    [160, 170, 180, 190, 200, 210],
    [220, 210, 230, 220, 240, 250]
])

yearly_sales = monthly_sales.sum(axis=1)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(genres)))
colors = [colors[4], colors[3], colors[1], colors[0], colors[2]]

markers = ['o', 's', '^', 'x', 'D']
linestyles = ['-', '--', ':', '-.', '-']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

width = 0.15
x = np.arange(len(months))

for i in range(len(genres)):
    ax1.plot(x + i * width, monthly_sales[i], marker=markers[i], linestyle=linestyles[i], 
             label=genres[i], color=colors[i])

ax1.set_title('Monthly Book Sales by Genre\n(Jan-Jun)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Books Sold', fontsize=14)
ax1.set_xticks(x + width * (len(genres) - 1) / 2)
ax1.set_xticklabels(months, fontsize=12)
ax1.legend(title='Genres', fontsize=10, loc='upper right')

bars = ax2.barh(genres, yearly_sales, color=colors, edgecolor='black')

ax2.set_title('Total Yearly Sales by Genre', fontsize=16, fontweight='bold')
ax2.set_xlabel('Books Sold', fontsize=14)

for bar in bars:
    width = bar.get_width()
    ax2.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{int(width)}',
             va='center', fontsize=10, color='black', weight='bold')

ax2.yaxis.grid(True, linestyle=':', alpha=0.7)
ax2.set_axisbelow(True)

plt.tight_layout()
plt.show()