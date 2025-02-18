import matplotlib.pyplot as plt
import numpy as np

genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Adventure', 
          'Thriller', 'Non-Fiction', 'Historical', 'Biography', 'Horror']

sales_data = [
    [60, 50, 55, 45, 35, 57, 53, 62, 52, 60],
    [46, 30, 35, 25, 32, 44, 38, 41, 43, 40],
    [77, 45, 50, 70, 40, 67, 60, 66, 75, 65],
    [25, 20, 15, 22, 18, 26, 24, 28, 23, 30],
    [48, 35, 30, 50, 38, 45, 40, 42, 46, 44],
    [75, 50, 55, 65, 58, 72, 60, 63, 68, 70],
    [32, 45, 28, 30, 33, 40, 37, 35, 39, 43],
    [37, 22, 25, 27, 20, 35, 29, 30, 32, 40],
    [31, 20, 18, 24, 23, 36, 26, 28, 30, 33],
    [26, 15, 10, 22, 18, 28, 20, 23, 24, 30]
]

fig, ax = plt.subplots(figsize=(14, 8))

boxes = ax.boxplot(sales_data, patch_artist=True, notch=False, vert=True,
                   boxprops=dict(facecolor='lightgreen', color='seagreen', linestyle=':'),
                   capprops=dict(color='seagreen'),
                   whiskerprops=dict(color='seagreen'),
                   flierprops=dict(marker='x', color='red', alpha=0.8),
                   medianprops=dict(color='darkgoldenrod'),
                   positions=range(1, len(genres) + 1))

ax.set_title('Annual Book Sales Distribution in Wonderland Market', 
             fontsize=14, fontweight='normal', pad=15)
ax.set_xlabel('Genre', fontsize=10)
ax.set_ylabel('Book Sales (thousands of units)', fontsize=10)

ax.set_xticks(range(1, len(genres) + 1))
ax.set_xticklabels(genres, rotation=45, ha='right')

colors = ['lemonchiffon', 'honeydew', 'mistyrose', 'peachpuff', 'lightcyan', 
          'lavenderblush', 'moccasin', 'lightblue', 'lightcoral', 'palegreen']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

ax.grid(False)

means = [np.mean(sales) for sales in sales_data]
ax.plot(range(1, len(genres) + 1), means, 's', color='magenta', label='Mean Sales')

ax.legend(loc='lower left')

plt.tight_layout()
plt.show()