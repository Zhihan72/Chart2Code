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

single_color = '#1f77b4'  # consistent color for all data groups
labels = ['Fantasy', 'Mystery', 'Science Fiction', 'Romance', 'Non-Fiction']

ax.stackplot(years, genre_data, labels=labels, colors=[single_color]*len(labels), alpha=0.85)

ax.set_title("The Literary Wave: A Decade of Genre Popularity\nOn Novel Isle (2010-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Popularity (Arbitrary Units)', fontsize=14)

ax.legend(loc='upper left', fontsize=12, title='Genre', frameon=False)

ax.grid(linestyle='--', alpha=0.6)

# Since we removed distinct colors, arrow annotation color is also unified.
ax.annotate('Fantasy Surge', xy=(2015, 85), xytext=(2011, 300),
            arrowprops=dict(facecolor='blue', arrowstyle='->', lw=1.5),
            fontsize=12, color='blue')

ax.annotate('Rise of Sci-Fi', xy=(2018, 200), xytext=(2015, 380),
            arrowprops=dict(facecolor='blue', arrowstyle='->', lw=1.5),
            fontsize=12, color='blue')

props = dict(boxstyle='round', facecolor='lavender', alpha=0.3)
textstr = ('Novel Isle saw a dynamic shift in\n'
           'literary tastes with Fantasy and Sci-Fi\n'
           'gaining immense traction.')
ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 401, 50))

for idx, genre in enumerate(labels):
    ax.annotate(f'{genre_data[idx, 0]}', (2010, genre_data[idx, 0]), textcoords="offset points", xytext=(-15,5), ha='center')
    ax.annotate(f'{genre_data[idx, -1]}', (2020, genre_data[idx, -1] + np.sum(genre_data[:idx, -1])), textcoords="offset points", xytext=(-15,-10), ha='center')

plt.tight_layout()

plt.show()