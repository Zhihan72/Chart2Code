import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Fictional readership data in millions for each genre with randomized content
fantasy_readership = [2, 2.8, 3, 3.6, 4.5, 5.5, 5.8, 7.2, 7.4, 8.9, 9.5]
mystery_readership = [3, 3.3, 3.8, 4.1, 4, 5.2, 5.4, 6.1, 6.8, 7.6, 8.1]
non_fiction_readership = [5, 5.2, 6.1, 6.3, 7.2, 7, 8.2, 8.1, 9.1, 9.8, 9.9]
romance_readership = [1, 1.7, 1.8, 2.2, 2.9, 3.1, 4.2, 4.3, 5.1, 5.2, 5.6]
sci_fi_readership = [2, 2.3, 2.6, 3.1, 3, 4.2, 4.4, 5.3, 5.2, 6.1, 6.9]

readership_data = np.vstack([fantasy_readership, mystery_readership, non_fiction_readership, romance_readership, sci_fi_readership])

genres = ['Fantasy', 'Mystery', 'Non-Fiction', 'Romance', 'Science Fiction']

fig, ax = plt.subplots(figsize=(14, 8))

# New colors applied here
ax.stackplot(years, readership_data, labels=genres, colors=['#ff6347', '#4682b4', '#7fff00', '#daa520', '#ff69b4'], alpha=0.7)

ax.set_title('The Evolution of Book Genres Over a Decade\nin Digital Libraries', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Readership (in Millions)', fontsize=12)

ax.grid(linestyle='--', alpha=0.6)

ax.legend(loc='upper left', frameon=True, bbox_to_anchor=(1.02, 1), borderaxespad=0.)

ax.annotate('Spike in Fantasy\ndue to Popular Series', xy=(2015, 5.5), xytext=(2013, 7.5),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.7))

plt.tight_layout()

plt.show()