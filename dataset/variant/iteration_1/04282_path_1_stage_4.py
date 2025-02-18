import matplotlib.pyplot as plt
import numpy as np

# Original data with some elements manually altered
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Biography']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
books_sold = [
    [170, 150, 120, 180],  # Altered Fiction sales
    [160, 130, 150, 140],  # Altered Non-Fiction sales
    [125, 110, 100, 130],  # Altered Mystery sales
    [135, 140, 145, 160],  # Altered Fantasy sales
    [95, 100, 105, 90]     # Altered Biography sales
]

books_sold = np.array(books_sold)
total_books_sold = books_sold.sum(axis=1)
sorted_indices = np.argsort(total_books_sold)[::-1]
sorted_genres = [genres[i] for i in sorted_indices]
sorted_books_sold = books_sold[sorted_indices]
sorted_colors = ['#2ca02c', '#1f77b4', '#d62728', '#ff7f0e', '#9467bd']

fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.15
x_indices = np.arange(len(quarters))

for i, genre in enumerate(sorted_genres):
    ax.bar(x_indices + i * bar_width, sorted_books_sold[i], width=bar_width, label=genre, color=sorted_colors[i])

for i, genre_data in enumerate(sorted_books_sold):
    for j, value in enumerate(genre_data):
        ax.text(j + i * bar_width, value + 3, str(value), ha='left', va='bottom', fontsize=8, color='red')

ax.set_xlabel('Quarters of 2022', fontsize=10, labelpad=10)
ax.set_ylabel('Number of Books Sold (thousands)', fontsize=10, labelpad=10)
ax.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1.05), fontsize=8, title_fontsize=10, shadow=True)

ax.yaxis.grid(True, linestyle='-.', linewidth=0.6, alpha=0.5)
ax.set_axisbelow(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()