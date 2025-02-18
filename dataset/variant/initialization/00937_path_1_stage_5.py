import matplotlib.pyplot as plt
import numpy as np

genres = ['Adventure', 'Historical', 'Biography', 'Mystery', 'Fantasy',
          'Horror', 'Thriller', 'Science Fiction', 'Non-Fiction', 'Romance',
          'Self-Help', 'Graphic Novels']

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
    [10, 15, 18, 20, 22, 23, 24, 26, 28, 30],
    [20, 25, 28, 30, 35, 33, 30, 40, 42, 44],
    [15, 17, 19, 21, 23, 25, 27, 30, 32, 35]
]

fig, ax = plt.subplots(figsize=(14, 8))

boxes = ax.boxplot(sales_data, patch_artist=True, notch=False, vert=False,
                   boxprops=dict(facecolor='skyblue', color='navy'),
                   capprops=dict(color='navy'),
                   whiskerprops=dict(color='navy'),
                   flierprops=dict(marker='x', color='lime', alpha=0.5),
                   medianprops=dict(color='orange'),
                   positions=range(1, len(genres) + 1))

ax.set_title('Genre-wise Market Analysis', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Sales Units (k)', fontsize=10)
ax.set_ylabel('Book Type', fontsize=10)

ax.set_yticks(range(1, len(genres) + 1))
ax.set_yticklabels(genres)

ax.annotate('Romantic Rise', xy=(77, 10), xytext=(85, 9),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=9, color='navy')

ax.annotate('New Wave: Sci-Fi', xy=(30, 8), xytext=(35, 6),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=9, color='forestgreen')

for patch in boxes['boxes']:
    patch.set_facecolor('skyblue')

ax.grid(True, linestyle='-', alpha=0.5)

means = [np.mean(sales) for sales in sales_data]
ax.plot(means, range(1, len(genres) + 1), 's', color='red', label='Mean Units')

ax.legend(loc='upper right')

plt.tight_layout()
plt.show()