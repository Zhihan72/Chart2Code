import matplotlib.pyplot as plt
import numpy as np

# Define genres and years
genres = ['Adventure', 'Historical', 'Biography', 'Mystery', 'Fantasy',
          'Horror', 'Thriller', 'Science Fiction', 'Non-Fiction', 'Romance']

# Construct sales data in thousands (fictional data for complexity)
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

boxes = ax.boxplot(sales_data, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='lightcoral', color='darkred'),
                   capprops=dict(color='darkred'),
                   whiskerprops=dict(color='darkred'),
                   flierprops=dict(marker='o', color='darkorange', alpha=0.5),
                   medianprops=dict(color='darkblue'),
                   positions=range(1, len(genres) + 1))

# Set altered labels
ax.set_title('Genre-wise Market Analysis\nStory Units in Thousands', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Book Type', fontsize=12)
ax.set_ylabel('Sales Units (k)', fontsize=12)

# Customizing X-axis
ax.set_xticks(range(1, len(genres) + 1))
ax.set_xticklabels(genres, rotation=45, ha="right")

# Altered annotations
ax.annotate('Romantic Rise', xy=(10, 77), xytext=(9, 85),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

ax.annotate('New Wave: Sci-Fi', xy=(8, 30), xytext=(6, 35),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkgreen')

colors = ['skyblue', 'lightgreen', 'pink', 'lightyellow', 'lightsalmon',
          'plum', 'lightcyan', 'navajowhite', 'lavender', 'lightgrey']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

ax.grid(True, linestyle='--', alpha=0.6)

means = [np.mean(sales) for sales in sales_data]
ax.plot(range(1, len(genres) + 1), means, 'D', color='purple', label='Mean Units')

ax.legend(loc='upper left')

plt.tight_layout()

plt.show()