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

ax2.bar(x - width, north_america_books, width, color='orchid')
ax2.bar(x, europe_books, width, color='gold')
ax2.bar(x + width, asia_books, width, color='lightsteelblue')

ax2.set_xticks(x)
ax2.grid(True, linestyle=':', alpha=0.5)

ax1.plot(x[1:], north_america_growth, marker='v', linestyle='-', color='orchid')
ax1.plot(x[1:], europe_growth, marker='s', linestyle='--', color='gold')
ax1.plot(x[1:], asia_growth, marker='D', linestyle='-.', color='lightsteelblue')

ax1.set_xticks(x[1:])
ax1.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()