import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2001, 2011)
north_america_books = np.array([5, 5.5, 6, 6.2, 6.5, 7, 7.5, 8, 8.3, 8.7])
europe_books = np.array([4, 4.5, 5, 5.5, 5.8, 6, 6.3, 6.7, 7, 7.3])
asia_books = np.array([2, 2.5, 3, 3.5, 3.8, 4.2, 4.5, 5, 5.3, 5.8])

north_america_growth = np.diff(north_america_books) / north_america_books[:-1] * 100 
europe_growth = np.diff(europe_books) / europe_books[:-1] * 100
asia_growth = np.diff(asia_books) / asia_books[:-1] * 100

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

x = np.arange(len(years))
width = 0.25

ax2.bar(x - width, north_america_books, width, label='North America', color='orchid')
ax2.bar(x, europe_books, width, label='Europe', color='gold')
ax2.bar(x + width, asia_books, width, label='Asia', color='lightsteelblue')

ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Avg Books Read', fontsize=10)
ax2.set_title('Books Read per Year (2001-2010)', fontsize=13, weight='bold', pad=10)
ax2.set_xticks(x)
ax2.set_xticklabels(years, rotation=0)
ax2.legend(loc='lower right', fontsize=8.5, title='Regions', title_fontsize=11)
ax2.grid(True, linestyle=':', alpha=0.5)

ax1.plot(x[1:], north_america_growth, marker='v', linestyle='-', label='North America', color='orchid')
ax1.plot(x[1:], europe_growth, marker='s', linestyle='--', label='Europe', color='gold')
ax1.plot(x[1:], asia_growth, marker='D', linestyle='-.', label='Asia', color='lightsteelblue')

ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Growth Rate (%)', fontsize=10)
ax1.set_title('Growth Rate in Books Read', fontsize=13, weight='bold', pad=10)
ax1.set_xticks(x[1:])
ax1.set_xticklabels(years[1:], rotation=0)
ax1.legend(loc='upper right', fontsize=8.5, title='Regions', title_fontsize=11)
ax1.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()