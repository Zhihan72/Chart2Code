import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
book_genres = ['Fiction', 'Non-Fic', 'Sci-Fi', 'Myst', 'Kids', 'Fant']

# Revenue data in thousands of dollars
revenue_data = np.array([
    [50, 52, 55, 60, 64, 70, 75, 80, 85, 90],
    [30, 32, 35, 40, 43, 50, 55, 60, 66, 70],
    [20, 22, 25, 28, 30, 35, 40, 45, 50, 55],
    [15, 17, 20, 23, 25, 30, 35, 40, 45, 50],
    [25, 27, 30, 33, 35, 40, 45, 50, 55, 60],
    [10, 12, 15, 18, 20, 23, 27, 30, 33, 37],
])

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.15
positions = np.arange(len(years))

# Changed order and colors to give it a different random appearance
shuffled_colors = ['#ffb3e6', '#99ff99', '#66b3ff', '#ffcc99', '#c2c2f0', '#ff9999']

bottoms = np.zeros(len(years))
for i, genre in enumerate(book_genres):
    # Changed marker type with '|' and line style to dashed
    ax.bar(positions, revenue_data[i], width, bottom=bottoms, 
           color=shuffled_colors[i], edgecolor='black', linestyle=(0, (5, 3)), 
           linewidth=1.5, label=genre)
    bottoms += revenue_data[i]

# Changed appearance of axis borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xticks(positions)
ax.set_xticklabels(years)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Revenue (in $K)', fontsize=12)
ax.set_title('Bookstore Revenue (2010-2019)', fontsize=16, fontweight='bold')

# Changed legend style and location randomly
ax.legend(title='Book Genres', fontsize=10, loc='upper left', frameon=False)

# Added a different grid style
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

for i in range(len(years)):
    total_value = sum(revenue_data[:, i])
    ax.text(i, total_value + 5, f'{total_value}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()