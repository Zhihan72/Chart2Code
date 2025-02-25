import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
book_genres = ['Fiction', 'Non-Fic', 'Sci-Fi', 'Myst', 'Kids', 'Fant']

revenue_data = np.array([
    [20, 22, 25, 28, 30, 35, 40, 45, 50, 55],
    [30, 32, 35, 40, 43, 50, 55, 60, 66, 70],
    [-20, -22, -25, -28, -30, -35, -40, -45, -50, -55],
    [-15, -17, -20, -23, -25, -30, -35, -40, -45, -50],
    [25, 27, 30, 33, 35, 40, 45, 50, 55, 60],
    [-10, -12, -15, -18, -20, -23, -27, -30, -33, -37],
])

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.4
positions = np.arange(len(years))

positive_bottoms = np.zeros(len(years))
negative_bottoms = np.zeros(len(years))

# Shuffle colors manually
shuffled_colors = ['#66b3ff', '#ff9999', '#ffb3e6', '#c2c2f0', '#99ff99', '#ffcc99']

for i, genre in enumerate(book_genres):
    data = revenue_data[i]
    color = shuffled_colors[i]
    
    if np.any(data > 0):
        ax.bar(positions, np.where(data > 0, data, 0), width, bottom=positive_bottoms, 
           color=color, edgecolor='black', label=genre if i == 0 else "")
        positive_bottoms += np.where(data > 0, data, 0)
        
    if np.any(data < 0):
        ax.bar(positions, np.where(data < 0, data, 0), width, bottom=negative_bottoms, 
           color=color, edgecolor='black')
        negative_bottoms += np.where(data < 0, data, 0)

ax.axhline(0, color='black', linewidth=1.5)

ax.set_xticks(positions)
ax.set_xticklabels(years)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Revenue (in $K)', fontsize=12)
ax.set_title('Diverging Revenue Chart (2010-2019)', fontsize=16, fontweight='bold')

ax.legend(title='Book Genres', fontsize=10, loc='upper left', frameon=False)
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()