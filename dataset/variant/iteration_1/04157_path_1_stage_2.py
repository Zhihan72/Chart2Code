import matplotlib.pyplot as plt
import numpy as np

years = ["2018", "2019", "2020", "2021", "2022"]
genres = ["Fantasy", "Mystery", "Romance", "Science Fiction", "Non-Fiction"]

data = np.array([
    [120, 100, 140, 130, 150],  
    [130, 110, 150, 140, 160],  
    [140, 90, 160, 120, 170],   
    [150, 120, 170, 130, 180],  
    [160, 130, 180, 140, 190]
])

# Shuffled colors
colors = ['#2ecc71', '#f1c40f', '#9b59b6', '#e74c3c', '#3498db']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
indices = np.arange(len(years))

for i in range(len(genres)):
    ax.bar(indices + i * bar_width, data[:, i], bar_width, color=colors[i])

ax.set_xlabel('Years', fontsize=12, weight='bold')
ax.set_ylabel('Sales (Thousands)', fontsize=12, weight='bold')
ax.set_title('Book Sales Growth in Different Genres (2018-2022)', fontsize=16, weight='bold', pad=20)
ax.set_xticks(indices + bar_width * (len(genres) - 1) / 2)
ax.set_xticklabels(years, fontsize=11, weight='bold')

for i, genre_sales in enumerate(data.T):
    for j, sales in enumerate(genre_sales):
        ax.text(indices[j] + i * bar_width, sales + 2, f'{sales}', ha='center', va='bottom', fontsize=9, weight='bold')

plt.tight_layout()
plt.show()