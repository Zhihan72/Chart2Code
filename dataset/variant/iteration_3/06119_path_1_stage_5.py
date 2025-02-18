import matplotlib.pyplot as plt
import numpy as np

genres = ['Fantasy', 'Science Fiction', 'Romance', 'Non-fiction', 'Mystery']
monthly_sales = np.array([
    [160, 170, 180, 190, 200, 210],
    [180, 175, 190, 185, 195, 200],
    [200, 190, 220, 210, 230, 240],
    [220, 210, 230, 220, 240, 250],
    [120, 130, 140, 150, 160, 170]
])

months = ['Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan']
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(genres)))
shuffled_colors = [colors[2], colors[0], colors[3], colors[4], colors[1]]

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 8))

# Yearly sales bar plot
yearly_sales = monthly_sales.sum(axis=1)
bars = ax1.barh(genres, yearly_sales, color=shuffled_colors, edgecolor='black')
ax1.set_title('Books Sold Annually by Category', fontsize=16, fontweight='bold')
ax1.set_xlabel('Books Count', fontsize=14)
ax1.set_ylabel('Category', fontsize=14)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_axisbelow(True)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{int(width)}',
             va='center', fontsize=10, color='black', weight='bold')

# Diverging bar plot for monthly sales
x = np.arange(len(months))
width = 0.3

half_idx = len(genres) // 2
for i in range(half_idx):
    ax2.bar(x - (half_idx - i) * width/2, monthly_sales[i], width, label=genres[i],
            color=shuffled_colors[i], edgecolor='black')

for i in range(half_idx, len(genres)):
    ax2.bar(x + (i - half_idx + 1) * width/2, monthly_sales[i], width, label=genres[i],
            color=shuffled_colors[i], edgecolor='black')

ax2.set_title('Diverging Sales by Month (First Half)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Sales Month', fontsize=14)
ax2.set_ylabel('Book Quantity', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(months, fontsize=12)
ax2.legend(title='Category Types', fontsize=10, loc='upper center')

plt.tight_layout()
plt.show()