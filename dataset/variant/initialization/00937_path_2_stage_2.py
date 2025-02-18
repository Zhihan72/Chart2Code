import matplotlib.pyplot as plt
import numpy as np

genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Adventure', 
          'Thriller', 'Non-Fiction', 'Historical', 'Biography', 'Horror']

sales_data = [
    [35, 45, 50, 60, 55, 52, 53, 57, 60, 62],
    [25, 30, 35, 32, 40, 38, 41, 43, 44, 46],
    [40, 45, 50, 60, 65, 67, 66, 70, 75, 77],
    [15, 18, 20, 25, 22, 23, 24, 26, 28, 30],
    [30, 35, 40, 38, 42, 44, 46, 45, 48, 50],
    [50, 55, 60, 58, 63, 65, 68, 70, 72, 75],
    [28, 32, 30, 33, 37, 35, 39, 40, 43, 45],
    [20, 22, 25, 27, 29, 30, 32, 35, 37, 40],
    [18, 20, 23, 24, 26, 28, 30, 31, 33, 36],
    [10, 15, 18, 20, 22, 23, 24, 26, 28, 30]
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

ax.annotate('Sci-Fi Resurgence', xy=(30, 4), xytext=(35, 5),
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