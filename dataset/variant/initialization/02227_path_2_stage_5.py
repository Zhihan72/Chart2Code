import matplotlib.pyplot as plt
import numpy as np

years = [2021, 2022, 2023]
genres = [
    'Drama', 'Poetry', 'Adventure', 'Sci-Fi', 
    'Thriller', 'Classical', 'Memoir', 'Passion', 'Ghost'
]
sales_data = {
    2021: [1350, 1050, 800, 1100, 980, 600, 350, 820, 450],
    2022: [1450, 1150, 780, 1040, 1120, 610, 410, 920, 490],
    2023: [1550, 1250, 900, 1080, 1170, 620, 550, 920, 550]
}

# Sorting sales data along with genres
sorted_genres_sales = {year: sorted(zip(sales_data[year], genres), key=lambda x: x[0]) for year in sales_data}
sorted_genres = [genre for sales, genre in sorted_genres_sales[2021]]

fig, ax = plt.subplots(figsize=(14, 10))
width = 0.25
x = np.arange(len(genres))

colors = ['#ff6347', '#4682b4', '#3cb371']
linestyles = ['-', '--', '-.']
for i, year in enumerate(years):
    sorted_sales = [sales for sales, genre in sorted_genres_sales[year]]
    ax.bar(x + i*width, sorted_sales, width=width, color=colors[i], linestyle=linestyles[i], edgecolor='gray', label=f'{year}')

for i, year in enumerate(years):
    sorted_sales = [sales for sales, genre in sorted_genres_sales[year]]
    for j, books in enumerate(sorted_sales):
        ax.text(j + i*width, books + 30, f'{books}', ha='center', fontsize=10, fontweight='normal', color='darkblue')

ax.set_title('Books Bazaar Bonanza\nSales Showdown (2021-2023)', fontsize=18, fontweight='light', pad=15)
ax.set_xlabel('Categories', fontsize=14, labelpad=8)
ax.set_ylabel('Units Sold', fontsize=14, labelpad=8)

ax.set_xticks(x + width)
ax.set_xticklabels(sorted_genres, rotation=30, ha='right', fontsize=12)

ax.yaxis.grid(True, linestyle='-', linewidth=0.5, alpha=0.5)
ax.legend(title='Sale Year', title_fontsize='13', fontsize='11', loc='lower right')

plt.tight_layout()
plt.show()