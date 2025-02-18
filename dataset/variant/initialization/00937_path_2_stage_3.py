import matplotlib.pyplot as plt
import numpy as np

genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Adventure', 
          'Thriller', 'Non-Fiction', 'Historical', 'Biography', 'Horror']

# Modified sales data with altered data values while preserving the original structure
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

boxes = ax.boxplot(sales_data, patch_artist=True, notch=True, vert=False,
                   boxprops=dict(facecolor='cyan', color='dodgerblue'),
                   capprops=dict(color='dodgerblue'),
                   whiskerprops=dict(color='dodgerblue'),
                   flierprops=dict(marker='o', color='forestgreen', alpha=0.5),
                   medianprops=dict(color='gold'),
                   positions=range(1, len(genres) + 1))

ax.set_title('Annual Book Sales Distribution\nby Genre in the Wonderland Publishing Market', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Book Sales (thousands of units)', fontsize=12)
ax.set_ylabel('Genre', fontsize=12)

ax.set_yticks(range(1, len(genres) + 1))
ax.set_yticklabels(genres)

ax.annotate('Romantic Boom', xy=(77, 3), xytext=(85, 2),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

ax.annotate('Sci-Fi Resurgence', xy=(25, 4), xytext=(35, 5),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkgreen')

colors = ['lightcoral', 'peachpuff', 'palegreen', 'lightcyan', 'lemonchiffon', 
          'lightblue', 'lavenderblush', 'mistyrose', 'moccasin', 'honeydew']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

ax.grid(True, linestyle='--', alpha=0.6)

means = [np.mean(sales) for sales in sales_data]
ax.plot(means, range(1, len(genres) + 1), 'D', color='purple', label='Mean Sales')

ax.legend(loc='upper right')

plt.tight_layout()
plt.show()