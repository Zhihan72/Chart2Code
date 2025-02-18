import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Reviewing Book Sales Growth in Different Genres Over the Last Five Years.
# This fictional dataset shows how book sales have fluctuated across five genres over the past five years.

# Define years and genres
years = ["2018", "2019", "2020", "2021", "2022"]
genres = ["Fantasy", "Mystery", "Romance", "Science Fiction", "Non-Fiction"]

# Sales data (in thousands)
# Each row corresponds to the sales of books in [Fantasy, Mystery, Romance, Science Fiction, Non-Fiction] for a particular year.
data = np.array([
    [120, 100, 140, 130, 150],  # 2018
    [130, 110, 150, 140, 160],  # 2019
    [140, 90, 160, 120, 170],   # 2020
    [150, 120, 170, 130, 180],  # 2021
    [160, 130, 180, 140, 190]   # 2022
])

# Define colors for each genre
colors = ['#9b59b6', '#2ecc71', '#e74c3c', '#3498db', '#f1c40f']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define the width of each bar
bar_width = 0.15

# Position of the years on the x-axis
indices = np.arange(len(years))

# Plot each genre's sales for each year
for i, genre in enumerate(genres):
    ax.bar(indices + i * bar_width, data[:, i], bar_width, color=colors[i], label=genre)

# Set labels and title
ax.set_xlabel('Years', fontsize=12, weight='bold')
ax.set_ylabel('Sales (Thousands)', fontsize=12, weight='bold')
ax.set_title('Book Sales Growth in Different Genres (2018-2022)', fontsize=16, weight='bold', pad=20)
ax.set_xticks(indices + bar_width * (len(genres) - 1) / 2)
ax.set_xticklabels(years, fontsize=11, weight='bold')
ax.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize='11')

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate the bars with the sales numbers
for i, genre_sales in enumerate(data.T):
    for j, sales in enumerate(genre_sales):
        ax.text(indices[j] + i * bar_width, sales + 2, f'{sales}', ha='center', va='bottom', fontsize=9, weight='bold')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()