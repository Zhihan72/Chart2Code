import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart displays the monthly sales data of a small bookshop named "Book Haven" for the year 2023.
# The bar chart shows the number of books sold per genre each month, and the line plot shows the cumulative sales of each genre over the year.

# Define the genres and months
genres = ['Fiction', 'Non-Fiction', 'Children', 'Science', 'History']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Monthly sales data for each genre (rows: months, columns: genres)
monthly_sales = np.array([
    [50, 30, 20, 25, 30],
    [60, 35, 18, 22, 33],
    [70, 40, 22, 27, 35],
    [80, 45, 25, 30, 40],
    [90, 50, 28, 32, 42],
    [105, 55, 30, 35, 45],
    [120, 60, 32, 37, 48],
    [140, 70, 35, 40, 50],
    [160, 80, 38, 42, 52],
    [180, 90, 40, 45, 55],
    [200, 100, 42, 47, 58],
    [220, 110, 45, 50, 60]
])

# Cumulative sales data for each genre
cumulative_sales = np.cumsum(monthly_sales, axis=0)

# Colors for bar chart
bar_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FFCC99']
line_styles = ['-', '--', '-.', ':', '-']

# Create the subplots, sharing the x-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Create stacked bar chart for monthly sales
bar_width = 0.8
prev_sales = np.zeros(len(months))
bars = []
for i, (genre, color) in enumerate(zip(genres, bar_colors)):
    bars.append(
        ax1.bar(months, monthly_sales[:, i], bottom=prev_sales, color=color, edgecolor='grey', 
                width=bar_width, label=f'Monthly {genre}', alpha=0.7)
    )
    prev_sales += monthly_sales[:, i]

# Create line plot for cumulative sales
ax2 = ax1.twinx()
for i, (genre, color, linestyle) in enumerate(zip(genres, bar_colors, line_styles)):
    ax2.plot(months, cumulative_sales[:, i], color=color, linestyle=linestyle, marker='o',
              label=f'Cumulative {genre}', linewidth=2)

# Add labels and title
ax1.set_title('Book Haven Monthly and Cumulative Sales by Genre (2023)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Monthly Sales (Number of Books)', fontsize=12)
ax2.set_ylabel('Cumulative Sales (Number of Books)', fontsize=12)

# Customize x-ticks and y-ticks
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, fontsize=11)
ax1.set_yticks(np.arange(0, 1300, 100))
ax2.set_yticks(np.arange(0, np.max(cumulative_sales) + 200, 200))

# Add grid lines
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add legends
bar_legend = ax1.legend(loc='upper left', fontsize=10, frameon=False)
line_legend = ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Ensuring no text overlap
plt.tight_layout()

# Show the plot
plt.show()