import matplotlib.pyplot as plt
import numpy as np

genres = ['Non-Fiction', 'Fantasy', 'Romance', 'Thriller', 'Science Fiction']
years = [2018, 2019, 2015, 2020, 2016, 2017]

# Manually shuffled sales data within each genre
sales_data = {
    'Science Fiction': [600, 700, 500, 750, 550, 650],
    'Romance': [580, 450, 530, 620, 470, 500],
    'Thriller': [740, 760, 780, 800, 700, 720],
    'Non-Fiction': [340, 360, 380, 300, 320, 400],
    'Fantasy': [750, 680, 780, 700, 650, 720]
}

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
ax = ax.flatten()

for i, year in enumerate(years):
    ax[i].set_title(f"Genre Sales Analysis {year}", fontsize=14, fontstyle='italic')
    bars = ax[i].bar(genres, [sales_data[genre][i] for genre in genres],
                     color='skyblue', edgecolor='blue', linestyle='--')
    ax[i].grid(True, linestyle=':', linewidth=0.5)
    ax[i].set_ylim(0, max(max(sales) for sales in sales_data.values()) + 100)
    ax[i].set_ylabel("Total Sold Units", fontsize=12, fontweight='light')
    ax[i].bar_label(bars, padding=3, fontsize=9)

fig.suptitle("Sales by Book Genre Over Years", fontsize=18, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()