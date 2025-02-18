import matplotlib.pyplot as plt
import numpy as np

# Define years and genres
years = ["2018", "2019", "2020", "2021", "2022"]
genres = ["Fantasy", "Mystery", "Romance", "Science Fiction", "Non-Fiction"]

# Randomly altered sales data (in thousands) while preserving the dimensional structure
data = np.array([
    [130, 140, 150, 120, 150],
    [140, 120, 140, 150, 130],
    [120, 160, 170, 110, 160],
    [160, 110, 160, 130, 180],
    [150, 130, 180, 140, 170]
])

# Define colors for each genre
colors = ['#9b59b6', '#2ecc71', '#e74c3c', '#3498db', '#f1c40f']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define the height of each bar
bar_height = 0.15

# Position of the genres on the y-axis
indices = np.arange(len(genres))

# Plot each year’s sales for each genre horizontally
for i, year in enumerate(years):
    ax.barh(indices + i * bar_height, data[i], bar_height, color=colors, label=year)

# Set labels and title
ax.set_ylabel('Genres', fontsize=12, weight='bold')
ax.set_xlabel('Sales (Thousands)', fontsize=12, weight='bold')
ax.set_title('Book Sales Growth in Different Genres (2018-2022)', fontsize=16, weight='bold', pad=20)
ax.set_yticks(indices + bar_height * (len(years) - 1) / 2)
ax.set_yticklabels(genres, fontsize=11, weight='bold')
ax.legend(title='Years', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize='11')

# Add grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate the bars with the sales numbers
for i, year_sales in enumerate(data):
    for j, sales in enumerate(year_sales):
        ax.text(sales + 2, indices[j] + i * bar_height, f'{sales}', va='center', fontsize=9, weight='bold')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()