import matplotlib.pyplot as plt
import numpy as np

# Backstory
# The chart represents the yearly revenue generated from different types of books in a fictional small-town bookstore for the past decade.
years = np.arange(2010, 2020)
book_genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Mystery', 'Children']

# Revenue data in thousands of dollars
revenue_data = np.array([
    [50, 52, 55, 60, 64, 70, 75, 80, 85, 90],  # Fiction
    [30, 32, 35, 40, 43, 50, 55, 60, 66, 70],  # Non-Fiction
    [20, 22, 25, 28, 30, 35, 40, 45, 50, 55],  # Science Fiction
    [15, 17, 20, 23, 25, 30, 35, 40, 45, 50],  # Mystery
    [25, 27, 30, 33, 35, 40, 45, 50, 55, 60],  # Children
])

# Initialize the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar widths and positions
width = 0.15
positions = np.arange(len(years))

# Colors for each genre
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']

# Create stacked bar chart
bottoms = np.zeros(len(years))
for i, genre in enumerate(book_genres):
    ax.bar(positions, revenue_data[i], width, bottom=bottoms, color=colors[i], label=genre)
    bottoms += revenue_data[i]

# Add grid, labels, title, and legend
ax.set_xticks(positions)
ax.set_xticklabels(years)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Revenue (in Thousands of Dollars)', fontsize=12)
ax.set_title('Annual Revenue Generated from Different Book Genres\nThe Story of a Small-town Bookstore (2010-2019)', fontsize=14, fontweight='bold')
ax.legend(title='Book Genres', fontsize=10)

# Annotate revenue for each year
for i in range(len(years)):
    total_value = sum(revenue_data[:, i])
    ax.text(i, total_value + 5, f'{total_value}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()