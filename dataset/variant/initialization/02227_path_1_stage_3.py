import matplotlib.pyplot as plt
import numpy as np

years = [2021, 2022, 2023]
genres = [
    'Fiction', 'Non-Fiction', 'Fantasy', 'Science Fiction', 
    'Mystery', 'Historical', 'Biography', 'Romance', 'Horror'
]
sales_data = {
    2021: [1400, 1100, 750, 950, 1050, 550, 300, 800, 400],
    2022: [1500, 1200, 800, 1000, 1100, 600, 400, 900, 500],
    2023: [1600, 1300, 850, 1050, 1150, 650, 500, 950, 600]
}

# Altered colors and marker styles for variety
colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#DAF7A6', '#33FFBD', '#00FF57', '#33A1FF', '#F333FF']
line_styles = ['-', '--', '-.', ':']

fig, ax = plt.subplots(figsize=(14, 10))
width = 0.25
x = np.arange(len(genres))

for i, (year, line_style) in enumerate(zip(years, line_styles)):
    sales = sales_data[year]
    ax.bar(x + i*width, sales, width=width, color=colors, edgecolor='black', linestyle=line_style)

ax.set_xticks(x + width)
ax.set_xticklabels(genres, rotation=45, ha='right')

ax.yaxis.grid(True, linestyle='-.', linewidth=1.0, alpha=0.5)
ax.legend([f'Sales {year}' for year in years], title="Year", loc='upper left', frameon=False)
plt.tight_layout()
plt.show()