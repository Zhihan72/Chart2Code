import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2001, 2011)

north_america_books = np.array([5.3, 5, 6.1, 6.3, 6.7, 6.8, 7.3, 8.5, 8.1, 8.9])
europe_books = np.array([4, 4.2, 4.7, 5.1, 5.9, 6.5, 6.2, 6.9, 7.1, 7.4])
asia_books = np.array([2.2, 2.8, 2.9, 3.6, 3.7, 4, 4.3, 5.3, 5.5, 5.7])

# Calculate growth rates
north_america_growth = np.diff(north_america_books) / north_america_books[:-1] * 100 
europe_growth = np.diff(europe_books) / europe_books[:-1] * 100
asia_growth = np.diff(asia_books) / asia_books[:-1] * 100

# Sort growth rates and years together
north_america_sorted_indices = np.argsort(north_america_growth)
europe_sorted_indices = np.argsort(europe_growth)
asia_sorted_indices = np.argsort(asia_growth)

north_america_growth = north_america_growth[north_america_sorted_indices]
north_america_years = years[1:][north_america_sorted_indices]

europe_growth = europe_growth[europe_sorted_indices]
europe_years = years[1:][europe_sorted_indices]

asia_growth = asia_growth[asia_sorted_indices]
asia_years = years[1:][asia_sorted_indices]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

width = 0.25

# Plot sorted bar charts
ax1.bar(north_america_years - width, north_america_growth, width, label='North America', color='lightblue')
ax1.bar(europe_years, europe_growth, width, label='Europe', color='salmon')
ax1.bar(asia_years + width, asia_growth, width, label='Asia', color='olive')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Growth Rate (%)', fontsize=12, weight='bold')
ax1.set_title('YoY Growth Rate in Books per Person (Sorted)', fontsize=14, weight='bold', pad=15)
ax1.set_xticks(years[1:])
ax1.set_xticklabels(years[1:], rotation=45, ha='right')
ax1.legend(loc='upper right', fontsize=10, ncol=2, shadow=True)
ax1.grid(True, linestyle='-.', alpha=0.5)

# Plot original line charts
ax2.plot(years, north_america_books, marker='o', linestyle='-', color='lightblue', label='North America')
ax2.plot(years, europe_books, marker='x', linestyle='--', color='salmon', label='Europe')
ax2.plot(years, asia_books, marker='^', linestyle='-.', color='olive', label='Asia')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Avg Books Read per Person', fontsize=12, weight='bold')
ax2.set_title('Avg Books per Person by Region (2001-2010)', fontsize=14, weight='bold', pad=15)
ax2.set_xticks(years)
ax2.legend(loc='lower left', fontsize=10, frameon=False)
ax2.grid(False)

ax2.annotate('Steady Growth', xy=(8, 8.9), xytext=(6, 9.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='navy')
ax2.annotate('Rapid Improvement', xy=(8, 5.7), xytext=(6, 6.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkred')

plt.tight_layout()
plt.show()