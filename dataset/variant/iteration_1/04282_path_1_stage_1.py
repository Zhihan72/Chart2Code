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

# Shuffled colors for each genre
colors = ['#9467bd', '#ff7f0e', '#1f77b4', '#d62728', '#2ca02c']  # Manually shuffled

for i, genre in enumerate(genres):
    ax.bar(x_indices + i * bar_width, books_sold[i], width=bar_width, label=genre, color=colors[i])

for i, genre_data in enumerate(books_sold):
    for j, value in enumerate(genre_data):
        ax.text(j + i * bar_width, value + 3, str(value), ha='center', va='bottom', fontsize=9, color='black')

ax.set_xlabel('Quarters of 2022', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Books Sold (thousands)', fontsize=12, labelpad=10)
ax.set_title('Book Sales Across Different Genres in 2022', fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(x_indices + bar_width * 2)
ax.set_xticklabels(quarters)

plt.xticks(rotation=20)
ax.legend(title='Book Genres', loc='upper left', bbox_to_anchor=(1, 1))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()