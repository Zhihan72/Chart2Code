import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

fantasy = np.array([20, 25, 30, 45, 65, 80, 95, 110, 130, 145, 160])
mystery = np.array([30, 35, 40, 45, 50, 55, 65, 70, 75, 85, 90])
science_fiction = np.array([15, 20, 28, 35, 45, 55, 70, 85, 100, 115, 130])
romance = np.array([25, 30, 35, 40, 45, 50, 60, 70, 80, 85, 95])
non_fiction = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])

genre_data = np.vstack([fantasy, mystery, science_fiction, romance, non_fiction])

fig, ax = plt.subplots(figsize=(14, 9))

# Changed color palette
colors = ['#d73027', '#4575b4', '#f46d43', '#74add1', '#fdae61']
# Randomly shuffled labels
labels = ['Science Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Romance']

ax.stackplot(years, genre_data, labels=labels, colors=colors, alpha=0.85)

ax.set_title("The Literary Wave: A Decade of Genre Popularity\nOn Novel Isle (2010-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Popularity (Arbitrary Units)', fontsize=14)

# Random placement and style of legend
ax.legend(loc='lower right', fontsize=13, title='Popular Genres', frameon=True, shadow=True, facecolor='lightgray')

# Random grid style
ax.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.3)

props = dict(boxstyle='round', facecolor='seashell', alpha=0.5)
textstr = ('Novel Isle saw a dynamic shift in\n'
           'literary tastes with Fantasy and Sci-Fi\n'
           'gaining immense traction.')
ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

plt.xticks(years, rotation=90)
plt.yticks(np.arange(0, 401, 50))

# Randomly chosen annotation styles
for idx, genre in enumerate(labels):
    ax.annotate(f'{genre_data[idx, 0]}', (2010, genre_data[idx, 0]), textcoords="offset points", xytext=(-10,10), ha='right')
    ax.annotate(f'{genre_data[idx, -1]}', (2020, genre_data[idx, -1] + np.sum(genre_data[:idx, -1])), textcoords="offset points", xytext=(-20,-5), ha='left')

plt.tight_layout()
plt.show()