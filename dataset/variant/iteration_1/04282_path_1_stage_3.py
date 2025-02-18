import matplotlib.pyplot as plt
import numpy as np

# Original data
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Biography']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
books_sold = [
    [120, 150, 180, 170],
    [130, 160, 140, 150],
    [100, 110, 130, 125],
    [140, 135, 145, 160],
    [90, 95, 100, 105]
]

# Convert to numpy array for easier manipulation
books_sold = np.array(books_sold)

# Calculate total books sold per genre
total_books_sold = books_sold.sum(axis=1)

# Sort genres by total books sold in descending order
sorted_indices = np.argsort(total_books_sold)[::-1]
sorted_genres = [genres[i] for i in sorted_indices]
sorted_books_sold = books_sold[sorted_indices]
sorted_colors = ['#2ca02c', '#1f77b4', '#d62728', '#ff7f0e', '#9467bd']  # Sorted colors correspond to new order

fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.15
x_indices = np.arange(len(quarters))

# Plot bars in sorted order
for i, genre in enumerate(sorted_genres):
    ax.bar(x_indices + i * bar_width, sorted_books_sold[i], width=bar_width, label=genre, color=sorted_colors[i])

# Annotate bars with their values
for i, genre_data in enumerate(sorted_books_sold):
    for j, value in enumerate(genre_data):
        ax.text(j + i * bar_width, value + 3, str(value), ha='left', va='bottom', fontsize=8, color='red')

# Set labels and legend
ax.set_xlabel('Quarters of 2022', fontsize=10, labelpad=10)
ax.set_ylabel('Number of Books Sold (thousands)', fontsize=10, labelpad=10)
ax.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1.05), fontsize=8, title_fontsize=10, shadow=True)

# Set grid and x-tick rotation
ax.yaxis.grid(True, linestyle='-.', linewidth=0.6, alpha=0.5)
ax.set_axisbelow(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()