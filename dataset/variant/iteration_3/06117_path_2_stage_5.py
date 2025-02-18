import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])

chip_popularity = np.array([25, 26, 28, 27, 26, 25, 24, 23, 22, 20])
cookie_popularity = np.array([20, 19, 18, 20, 21, 22, 23, 24, 25, 25])
fruit_popularity = np.array([15, 16, 17, 18, 19, 20, 21, 22, 23, 25])
nut_popularity = np.array([12, 13, 14, 14, 15, 16, 17, 17, 18, 19])
candy_popularity = np.array([28, 26, 23, 21, 19, 17, 15, 14, 12, 11])
popcorn_popularity = np.array([10, 11, 12, 13, 14, 15, 16, 16, 17, 17])
granola_popularity = np.array([5, 6, 6, 7, 7, 8, 9, 10, 11, 12])

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

new_colors = ['#ff7f0e', '#1f77b4', '#d62728', '#2ca02c', '#e377c2', '#9467bd', '#8c564b']

popularity_data = np.array([fruit_popularity, cookie_popularity, granola_popularity, nut_popularity])
neg_popularity_data = np.array([candy_popularity, chip_popularity, popcorn_popularity])

for i, year in enumerate(years):
    positive_base = 0
    negative_base = 0

    for j, data in enumerate(popularity_data):
        ax.bar(year, data[i], width=bar_width, label=('Fruits', 'Cookies', 'Granola', 'Nuts')[j] if i == 0 else "", 
               bottom=positive_base, color=new_colors[j], edgecolor='black', linestyle='--')
        positive_base += data[i]

    for j, data in enumerate(neg_popularity_data):
        ax.bar(year, -data[i], width=bar_width, label=('Candy', 'Chips', 'Popcorn')[j] if i == 0 else "", 
               bottom=negative_base, color=new_colors[j + 4], edgecolor='black', linestyle='-')
        negative_base -= data[i]

ax.set_title('Snack Preference Divergence (2013-2022)', fontsize=16, fontweight='light', pad=25)
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Popularity', fontsize=11)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:7], labels[:7], fontsize=9, loc='lower right')

ax.yaxis.grid(True, linestyle=':', linewidth=0.6, alpha=0.5)
ax.set_axisbelow(True)

plt.axhline(y=0, color='black', linewidth=0.9, linestyle='-.')

plt.tight_layout()

plt.show()