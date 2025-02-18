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

fig, ax = plt.subplots(figsize=(14, 10))
width = 0.25
x = np.arange(len(genres))

# Modified color, edgecolor, and linestyle
colors = ['#ff6347', '#4682b4', '#3cb371']  # Different colors for bars
linestyles = ['-', '--', '-.']  # Different line styles
for i, year in enumerate(years):
    sales = sales_data[year]
    ax.bar(x + i*width, sales, width=width, color=colors[i], linestyle=linestyles[i], edgecolor='gray', label=f'{year}')

# Modified text appearance
for i, year in enumerate(years):
    sales = sales_data[year]
    for j, books in enumerate(sales):
        ax.text(j + i*width, books + 30, f'{books}', ha='center', fontsize=10, fontweight='normal', color='darkblue')

# Changed title and label styles
ax.set_title('Books Bazaar Bonanza\nSales Showdown (2021-2023)', fontsize=18, fontweight='light', pad=15)
ax.set_xlabel('Categories', fontsize=14, labelpad=8)
ax.set_ylabel('Units Sold', fontsize=14, labelpad=8)

# Modified tick label appearance
ax.set_xticks(x + width)
ax.set_xticklabels(genres, rotation=30, ha='right', fontsize=12)

# Altered gridlines
ax.yaxis.grid(True, linestyle='-', linewidth=0.5, alpha=0.5)

# Changed legend position and style
ax.legend(title='Sale Year', title_fontsize='13', fontsize='11', loc='lower right')

plt.tight_layout()
plt.show()