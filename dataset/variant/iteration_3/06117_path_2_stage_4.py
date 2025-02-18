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

new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Convert values for diverging bar chart
popularity_data = np.array([cookie_popularity, fruit_popularity, nut_popularity, granola_popularity])
neg_popularity_data = np.array([chip_popularity, candy_popularity, popcorn_popularity])

for i, year in enumerate(years):
    positive_base = 0
    negative_base = 0

    # Plotting positive part
    for j, data in enumerate(popularity_data):
        ax.bar(year, data[i], width=bar_width, label=('Cookies', 'Fruits', 'Nuts', 'Granola')[j] if i == 0 else "", 
               bottom=positive_base, color=new_colors[j], edgecolor='grey')
        positive_base += data[i]

    # Plotting negative part
    for j, data in enumerate(neg_popularity_data):
        ax.bar(year, -data[i], width=bar_width, label=('Chips', 'Candy', 'Popcorn')[j] if i == 0 else "", 
               bottom=negative_base, color=new_colors[j + 4], edgecolor='grey')
        negative_base -= data[i]

ax.set_title('Snack Preference Divergence (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity', fontsize=12)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:7], labels[:7], fontsize=10, loc='upper left')

# Set grid
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)

plt.axhline(y=0, color='black', linewidth=0.8)

plt.tight_layout()

plt.show()