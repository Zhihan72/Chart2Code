import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])

# Existing snack popularity data
chip_popularity = np.array([25, 26, 28, 27, 26, 25, 24, 23, 22, 20])
cookie_popularity = np.array([20, 19, 18, 20, 21, 22, 23, 24, 25, 25])
fruit_popularity = np.array([15, 16, 17, 18, 19, 20, 21, 22, 23, 25])
nut_popularity = np.array([12, 13, 14, 14, 15, 16, 17, 17, 18, 19])
candy_popularity = np.array([28, 26, 23, 21, 19, 17, 15, 14, 12, 11])

# New made-up snack popularity data
granola_popularity = np.array([10, 11, 12, 13, 14, 15, 15, 16, 17, 18])
chips_2_popularity = np.array([5, 6, 7, 7, 8, 8, 9, 9, 10, 11])

# Recalculate popularity for positive and negative snacks
positive_snacks = chip_popularity + nut_popularity + chips_2_popularity
negative_snacks = candy_popularity + cookie_popularity + fruit_popularity + granola_popularity

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6
positions = np.arange(len(years))

colors = ['#d95f02', '#1b9e77']

ax.barh(positions, positive_snacks, height=bar_width, label='Positive', color=colors[0])
ax.barh(positions, -negative_snacks, height=bar_width, label='Negative', color=colors[1])

ax.set_yticks(positions)
ax.set_yticklabels(years)
ax.set_ylim(-max(negative_snacks) - 10, max(positive_snacks) + 10)
ax.set_xlabel('Popularity', fontsize=12)
ax.set_title('Snack Popularity (2013-2022)', fontsize=16, fontweight='bold', pad=20)

ax.axvline(x=0, color='black', linewidth=0.8)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, fontsize=10, loc='upper left')

ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()