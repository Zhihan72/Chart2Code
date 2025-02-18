import matplotlib.pyplot as plt
import numpy as np

years = ["2018", "2019", "2020", "2021", "2022"]
genres = ["Fant", "Myst", "Rom", "Sci-Fi", "Non-Fic"]

data = np.array([
    [130, 140, 150, 120, 150],
    [140, 120, 140, 150, 130],
    [120, 160, 170, 110, 160],
    [160, 110, 160, 130, 180],
    [150, 130, 180, 140, 170]
])

colors = ['#9b59b6', '#2ecc71', '#e74c3c', '#3498db', '#f1c40f']

fig, ax = plt.subplots(figsize=(14, 8))
bar_height = 0.15
indices = np.arange(len(genres))

for i, year in enumerate(years):
    ax.barh(indices + i * bar_height, data[i], bar_height, color=colors, label=year)

ax.set_ylabel('Genres', fontsize=12, weight='bold')
ax.set_xlabel('Sales (k)', fontsize=12, weight='bold')
ax.set_title('Sales by Genre (2018-22)', fontsize=16, weight='bold', pad=20)
ax.set_yticks(indices + bar_height * (len(years) - 1) / 2)
ax.set_yticklabels(genres, fontsize=11, weight='bold')
ax.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize='11')

ax.grid(axis='x', linestyle='--', alpha=0.7)

for i, year_sales in enumerate(data):
    for j, sales in enumerate(year_sales):
        ax.text(sales + 2, indices[j] + i * bar_height, f'{sales}', va='center', fontsize=9, weight='bold')

plt.tight_layout()
plt.show()