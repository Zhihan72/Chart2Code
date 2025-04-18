import matplotlib.pyplot as plt
import numpy as np

genres = ['Science Fiction', 'Romance', 'Thriller', 'Non-Fiction', 'Fantasy']
years = [2015, 2016, 2017, 2018, 2019, 2020]

sales_data = {
    'Science Fiction': [500, 550, 600, 650, 700, 750],
    'Romance': [450, 470, 500, 530, 580, 620],
    'Thriller': [700, 720, 740, 760, 780, 800],
    'Non-Fiction': [300, 320, 340, 360, 380, 400],
    'Fantasy': [650, 680, 700, 720, 750, 780]
}

color_map = plt.cm.get_cmap('cool', len(genres))

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
ax = ax.flatten()

for i, year in enumerate(years):
    ax[i].set_title(f"Book Sales in {year}", fontsize=14, fontstyle='italic')
    bars = ax[i].bar(genres, [sales_data[genre][i] for genre in genres],
                     color=[color_map(j) for j in range(len(genres))], edgecolor='blue', linestyle='--')
    ax[i].grid(True, linestyle=':', linewidth=0.5)
    ax[i].set_ylim(0, max(max(sales) for sales in sales_data.values()) + 100)
    ax[i].set_ylabel("Books Sold", fontsize=12, fontweight='light')
    ax[i].bar_label(bars, padding=3, fontsize=9)

fig.suptitle("Yearly Book Sales by Genre (2015-2020)", fontsize=18, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()