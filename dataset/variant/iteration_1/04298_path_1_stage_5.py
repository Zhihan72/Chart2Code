import matplotlib.pyplot as plt
import numpy as np

years = ["2018", "2019", "2020", "2021", "2022"]
genres = ["Fant", "Myst", "Rom", "Sci-Fi", "Non-Fic"]

data = np.array([
    [140, 100, 150, 130, 160],  
    [120, 90, 140, 140, 150],   
    [130, 110, 170, 120, 190],  
    [150, 130, 140, 130, 180],  
    [160, 120, 160, 140, 170]
])

colors = ['#2ecc71', '#f1c40f', '#9b59b6', '#e74c3c', '#3498db']

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
indices = np.arange(len(years))

for i, genre in enumerate(genres):
    ax.barh(indices + i * bar_height, data[:, i], bar_height, color=colors[i], label=genre)

ax.set_ylabel('Year', fontsize=12, weight='bold')
ax.set_xlabel('Sales (K)', fontsize=12, weight='bold')
ax.set_title('Book Sales (2018-22)', fontsize=16, weight='bold', pad=20)
ax.set_yticks(indices + bar_height * (len(genres) - 1) / 2)
ax.set_yticklabels(years, fontsize=11, weight='bold')

for i, genre_sales in enumerate(data.T):
    for j, sales in enumerate(genre_sales):
        ax.text(sales + 2, indices[j] + i * bar_height, f'{sales}', va='center', ha='left', fontsize=9, weight='bold')

ax.legend()

plt.tight_layout()
plt.show()