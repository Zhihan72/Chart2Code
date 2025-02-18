import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
fantasy_readership = [2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]
mystery_readership = [3, 3.2, 3.5, 4, 4.2, 5, 5.5, 6, 7, 7.5, 8]
romance_readership = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
sci_fi_readership = [2, 2.2, 2.5, 3, 3.2, 4, 4.5, 5, 5.5, 6, 7]
readership_data = np.vstack([fantasy_readership, mystery_readership, romance_readership, sci_fi_readership])
genres = ['Fnt', 'Mys', 'Rom', 'Sci-Fi']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, readership_data, labels=genres, colors=['#8A2BE2', '#5F9EA0', '#FF7F50', '#9ACD32'], alpha=0.85)

ax.set_title('Readers By Genre\nOver 10 Years', fontsize=14, fontweight='medium', pad=15)
ax.set_xlabel('Yr', fontsize=11)
ax.set_ylabel('Readers (M)', fontsize=11)

ax.grid(linestyle=':', alpha=0.9)

ax.legend(loc='upper right', frameon=False, fontsize=10)

ax.annotate('Fantasy Up', xy=(2015, 5), xytext=(2016, 8.5),
            arrowprops=dict(facecolor='gray', arrowstyle='fancy'), fontsize=9, ha='left', bbox=dict(facecolor='lightgray', alpha=0.5))

plt.tight_layout()
plt.show()