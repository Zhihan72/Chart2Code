import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents the number of books sold in different genres over four quarters of 2022.
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Biography']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Data (number of books sold in thousands)
books_sold = [
    [120, 150, 180, 170],  # Fiction
    [130, 160, 140, 150],  # Non-Fiction
    [100, 110, 130, 125],  # Mystery
    [140, 135, 145, 160],  # Fantasy
    [90, 95, 100, 105]     # Biography
]

# Convert data into a numpy array for manipulation
books_sold = np.array(books_sold)

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Bar width
bar_width = 0.15

# Create an array for the x-axis indices
x_indices = np.arange(len(quarters))

# Plot bars for each genre
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, genre in enumerate(genres):
    ax.bar(x_indices + i * bar_width, books_sold[i], width=bar_width, label=genre, color=colors[i])

# Add data annotations
for i, genre_data in enumerate(books_sold):
    for j, value in enumerate(genre_data):
        ax.text(j + i * bar_width, value + 3, str(value), ha='center', va='bottom', fontsize=9, color='black')

# Set the labels and ticks
ax.set_xlabel('Quarters of 2022', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Books Sold (thousands)', fontsize=12, labelpad=10)
ax.set_title('Book Sales Across Different Genres in 2022', fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(x_indices + bar_width * 2)
ax.set_xticklabels(quarters)

# Rotate x-axis labels for better readability
plt.xticks(rotation=20)

# Add a legend to the plot
ax.legend(title='Book Genres', loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()