import matplotlib.pyplot as plt
import numpy as np

genres = ['Mystery', 'Romance', 'Science Fiction', 'Fantasy', 'Non-fiction']
monthly_sales = np.array([
    [120, 130, 140, 150, 160, 170],  # Mystery
    [200, 190, 220, 210, 230, 240],  # Romance
    [180, 175, 190, 185, 195, 200],  # Science Fiction
    [160, 170, 180, 190, 200, 210],  # Fantasy
    [220, 210, 230, 220, 240, 250]   # Non-fiction
])

yearly_sales = monthly_sales.sum(axis=1)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(genres)))

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 8))  # Switched positions

# Plot yearly sales (now on ax1, originally ax2)
bars = ax1.barh(genres, yearly_sales, color=colors, edgecolor='black')
ax1.set_title('Total Yearly Sales by Genre', fontsize=16, fontweight='bold')
ax1.set_xlabel('Number of Books Sold', fontsize=14)
ax1.set_ylabel('Genre', fontsize=14)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{int(width)}', 
             va='center', fontsize=10, color='black', weight='bold')

ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_axisbelow(True)

# Plot monthly sales (now on ax2, originally ax1)
width = 0.15
x = np.arange(len(months))

for i in range(len(genres)):
    ax2.bar(x + i * width, monthly_sales[i], width, label=genres[i], color=colors[i], edgecolor='black')

ax2.set_title('Monthly Book Sales by Genre\n(Jan-Jun)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Month', fontsize=14)
ax2.set_ylabel('Number of Books Sold', fontsize=14)
ax2.set_xticks(x + width * (len(genres) - 1) / 2)
ax2.set_xticklabels(months, fontsize=12)
ax2.legend(title='Genres', fontsize=10)

plt.tight_layout()
plt.show()