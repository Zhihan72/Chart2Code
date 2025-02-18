import matplotlib.pyplot as plt
import numpy as np

years = [2021, 2022, 2023]
genres = [
    'Fiction', 'Non-Fiction', 'Fantasy', 'Science Fiction', 
    'Mystery', 'Historical', 'Biography', 'Romance', 'Horror'
]
sales_data = {
    2021: [1350, 1050, 800, 1100, 980, 600, 350, 820, 450],
    2022: [1450, 1150, 780, 1040, 1120, 610, 410, 920, 490],
    2023: [1550, 1250, 900, 1080, 1170, 620, 550, 920, 550]
}

colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33C4', '#33FFC4', '#FFC300', '#C70039', '#900C3F']

fig, ax = plt.subplots(figsize=(14, 10))
width = 0.25
x = np.arange(len(genres))

for i, year in enumerate(years):
    sales = sales_data[year]
    ax.bar(x + i*width, sales, width=width, color=colors, label=f'{year}', edgecolor='black')

for i, year in enumerate(years):
    sales = sales_data[year]
    for j, books in enumerate(sales):
        ax.text(j + i*width, books + 30, f'{books}', ha='center', fontsize=9, fontweight='bold', color='black')

ax.set_title('Annual Grand Book Festival\nGenre Sales Comparison (2021-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Genres', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Books Sold', fontsize=12, labelpad=10)

ax.set_xticks(x + width)
ax.set_xticklabels(genres, rotation=45, ha='right', fontsize=11)

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

ax.legend(title='Year', title_fontsize='13', fontsize='11', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()