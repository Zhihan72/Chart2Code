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

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0', '#ffb3e6']

bottoms = np.zeros(len(years))
for i, genre in enumerate(book_genres):
    ax.bar(positions, revenue_data[i], width, bottom=bottoms, color=colors[i], label=genre)
    bottoms += revenue_data[i]

ax.set_xticks(positions)
ax.set_xticklabels(years)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Rev (in K$)', fontsize=12)
ax.set_title('Bookstore Revenue\n(2010-2019)', fontsize=14, fontweight='bold')
ax.legend(title='Genres', fontsize=10)

for i in range(len(years)):
    total_value = sum(revenue_data[:, i])
    ax.text(i, total_value + 5, f'{total_value}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()