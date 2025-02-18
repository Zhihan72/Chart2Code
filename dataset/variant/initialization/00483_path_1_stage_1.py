import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Shuffle the content within each genre array, maintaining original dimensionality
fantasy = np.array([22, 17, 15, 21, 20, 19, 18, 18, 19, 20, 19])
sci_fi = np.array([12, 22, 13, 14, 15, 16, 11, 20, 21, 18, 23])
mystery = np.array([23, 25, 24, 21, 20, 19, 18, 18, 17, 16, 15])
romance = np.array([23, 21, 24, 23, 25, 22, 20, 26, 25, 24, 21])
non_fiction = np.array([23, 28, 27, 21, 22, 22, 21, 18, 18, 18, 17])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, fantasy, sci_fi, mystery, romance, non_fiction,
             labels=['Fantasy', 'Sci-Fi', 'Mystery', 'Romance', 'Non-Fiction'],
             colors=['#c9d1d3', '#aad6a1', '#f6b393', '#f7e1a0', '#b0a8d0'], alpha=0.85)

ax.set_title('Literature Evolution: Reading Preferences Over Time\n(2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage of Total Readership', fontsize=14)

ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)
ax.legend(loc='upper left', title='Genres', fontsize=12, frameon=False)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

ax.annotate('Rise in Sci-Fi', xy=(2018, 60), xytext=(2016, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
ax.annotate('Steady Interest in Romance', xy=(2020, 82), xytext=(2015, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

plt.tight_layout()
plt.show()