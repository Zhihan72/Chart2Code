import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2001, 2011)

north_america_books = np.array([5.3, 5, 6.1, 6.3, 6.7, 6.8, 7.3, 8.5, 8.1, 8.9])
europe_books = np.array([4, 4.2, 4.7, 5.1, 5.9, 6.5, 6.2, 6.9, 7.1, 7.4])
asia_books = np.array([2.2, 2.8, 2.9, 3.6, 3.7, 4, 4.3, 5.3, 5.5, 5.7])

north_america_growth = np.diff(north_america_books) / north_america_books[:-1] * 100 
europe_growth = np.diff(europe_books) / europe_books[:-1] * 100
asia_growth = np.diff(asia_books) / asia_books[:-1] * 100

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

x = np.arange(len(years))
width = 0.25

# Changed colors
ax1.bar(x[1:] - width, north_america_growth, width, label='North America', color='purple')
ax1.bar(x[1:], europe_growth, width, label='Europe', color='gold')
ax1.bar(x[1:] + width, asia_growth, width, label='Asia', color='teal')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Growth Rate (%)', fontsize=12)
ax1.set_title('Year-over-Year Growth Rate in Books Read per Person', fontsize=14, weight='bold', pad=15)
ax1.set_xticks(x[1:])
ax1.set_xticklabels(years[1:], rotation=45)
ax1.legend(loc='upper left', fontsize=10, title='Regions', title_fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)

ax2.bar(x - width, north_america_books, width, label='North America', color='purple')
ax2.bar(x, europe_books, width, label='Europe', color='gold')
ax2.bar(x + width, asia_books, width, label='Asia', color='teal')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Average Books Read per Person', fontsize=12)
ax2.set_title('Average Books Read per Person per Year by Region (2001-2010)', fontsize=14, weight='bold', pad=15)
ax2.set_xticks(x)
ax2.set_xticklabels(years, rotation=45)
ax2.legend(loc='upper left', fontsize=10, title='Regions', title_fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

ax2.annotate('Steady Growth', xy=(8, 8.9), xytext=(6, 9.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='navy', weight='bold')
ax2.annotate('Rapid Improvement', xy=(8, 5.7), xytext=(6, 6.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkred', weight='bold')

plt.tight_layout()
plt.show()