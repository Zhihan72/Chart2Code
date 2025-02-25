import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2001, 2011)
north_america_books = np.array([5, 5.5, 6, 6.2, 6.5, 7, 7.5, 8, 8.3, 8.7])
europe_books = np.array([4, 4.5, 5, 5.5, 5.8, 6, 6.3, 6.7, 7, 7.3])

# Calculate growth rates
north_america_growth = np.diff(north_america_books) / north_america_books[:-1] * 100 
europe_growth = np.diff(europe_books) / europe_books[:-1] * 100

# Sort the books data
sorted_na_books = np.sort(north_america_books)
sorted_europe_books = np.sort(europe_books)

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot sorted bar chart
x = np.arange(len(years))
width = 0.35

ax2.bar(x - width / 2, sorted_na_books, width, color='orchid', label='North America')
ax2.bar(x + width / 2, sorted_europe_books, width, color='gold', label='Europe')

ax2.set_xticks(x)
ax2.set_xticklabels(years)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend()

# Plot growth rates
ax1.plot(x[1:], north_america_growth, marker='v', linestyle='-', color='orchid')
ax1.plot(x[1:], europe_growth, marker='s', linestyle='--', color='gold')

ax1.set_xticks(x[1:])
ax1.set_xticklabels(years[1:])
ax1.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()