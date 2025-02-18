import matplotlib.pyplot as plt
import numpy as np

genres = ['Adventure', 'Romance', 'Action', 'Biography', 'Fantasy']
years = [2015, 2016, 2017, 2018, 2019, 2020]

sales_data = {
    'Adventure': [500, 550, 600, 650, 700, 750],
    'Romance': [450, 470, 500, 530, 580, 620],
    'Action': [700, 720, 740, 760, 780, 800],
    'Biography': [300, 320, 340, 360, 380, 400],
    'Fantasy': [650, 680, 700, 720, 750, 780]
}

color_map = plt.cm.get_cmap('tab10', len(genres))

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
ax = ax.flatten()

custom_titles = ['Yearly Analysis', 'Book Trends', 'Sales Growth', 'Market Performance', 'Genre Popularity', 'Yearly Comparison']

# Rearrange the subplots indices based on the new desired positions
desired_order = [5, 0, 3, 1, 4, 2]

for plot_index, year_index in enumerate(desired_order):
    bars = ax[plot_index].barh(genres, [sales_data[genre][year_index] for genre in genres], color=[color_map(j) for j in range(len(genres))])
    ax[plot_index].set_xlim(0, max(max(sales) for sales in sales_data.values()) + 100)
    ax[plot_index].set_xlabel("Units Sold", fontsize=12)
    ax[plot_index].set_title(custom_titles[year_index], fontsize=14)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()