import matplotlib.pyplot as plt
import numpy as np

# Define the genres and months
genres = ['Fiction', 'Non-Fiction', 'Children', 'Science', 'History']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Monthly sales data for each genre
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

# Colors for the bar chart
bar_colors = ['#66B2FF', '#FFD700', '#FFCC99', '#99FF99', '#FF9999']

fig, ax = plt.subplots(figsize=(14, 8))

# Create grouped bar chart for monthly sales
bar_width = 0.15
x = np.arange(len(months))

# Plot each genre's monthly sales side by side
for i, (genre, color) in enumerate(zip(genres, bar_colors)):
    ax.bar(x + i * bar_width, monthly_sales[:, i], color=color, edgecolor='grey',
           width=bar_width, label=genre, alpha=0.7)

# Add labels and title
ax.set_title('Book Haven Monthly Sales by Genre (2023)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Monthly Sales (Number of Books)', fontsize=12)

# Customize x-ticks and y-ticks
ax.set_xticks(x + bar_width * (len(genres) - 1) / 2)
ax.set_xticklabels(months, fontsize=11)
ax.set_yticks(np.arange(0, 300, 20))

# Add grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()