import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Biography']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

books_sold = [
    [120, 150, 180, 170],
    [130, 160, 140, 150],
    [100, 110, 130, 125],
    [140, 135, 145, 160],
    [90, 95, 100, 105]
]

books_sold = np.array(books_sold)

fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.15
x_indices = np.arange(len(quarters))

# Randomly altered colors
colors = ['#d62728', '#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

for i, genre in enumerate(genres):
    ax.bar(x_indices + i * bar_width, books_sold[i], width=bar_width, label=genre, color=colors[i])

# Changed text properties
for i, genre_data in enumerate(books_sold):
    for j, value in enumerate(genre_data):
        ax.text(j + i * bar_width, value + 3, str(value), ha='left', va='bottom', fontsize=8, color='red')

# Modified label fonts and removed title
ax.set_xlabel('Quarters of 2022', fontsize=10, labelpad=10)
ax.set_ylabel('Number of Books Sold (thousands)', fontsize=10, labelpad=10)

# Adjusted legend properties
ax.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1.05), fontsize=8, title_fontsize=10, shadow=True)

# Modified grid style
ax.yaxis.grid(True, linestyle='-.', linewidth=0.6, alpha=0.5)
ax.set_axisbelow(True)

# Altered tick rotation
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()