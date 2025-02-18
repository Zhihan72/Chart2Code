import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the Popularity and Revenue of Fiction vs Non-Fiction Books Over the Decades
# This dataset shows the number of fiction and non-fiction books published each decade and their total revenue.

# Define the decades and number of books published in each genre
decades = np.arange(1960, 2021, 10)
fiction_books = [150, 180, 200, 220, 250, 280, 310]
non_fiction_books = [100, 120, 140, 160, 180, 200, 220]

# Revenue data by genre (in millions)
fiction_revenue = [450, 500, 550, 600, 700, 750, 800]
non_fiction_revenue = [300, 350, 400, 450, 500, 550, 600]

# Create the bar chart with different colors for each genre
fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 3
ax1.bar(decades - bar_width, fiction_books, width=bar_width, color='#6a5acd', alpha=0.7, label='Fiction Books Published')
ax1.bar(decades, non_fiction_books, width=bar_width, color='#ff6347', alpha=0.7, label='Non-Fiction Books Published')

# Create a secondary y-axis for revenue data
ax2 = ax1.twinx()
ax2.bar(decades - bar_width, fiction_revenue, width=bar_width, color='#6a5acd', alpha=0.3, label='Fiction Revenue')
ax2.bar(decades, non_fiction_revenue, width=bar_width, color='#ff6347', alpha=0.3, label='Non-Fiction Revenue')

# Set chart titles and labels
ax1.set_title("Popularity and Revenue of Fiction vs Non-Fiction Books (1960-2020)", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Decades", fontsize=12)
ax1.set_ylabel("Number of Books Published", fontsize=12)
ax2.set_ylabel("Revenue in Millions (USD)", fontsize=12)

# Set grid and legends
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10, title='Books Published')
ax2.legend(loc='upper right', fontsize=10, title='Revenue')

# Annotate key points
ax1.annotate('Fiction Genre Boost', xy=(1990, 220), xytext=(1980, 240),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=10, fontweight='bold', color='blue')
ax1.annotate('Rise of Non-Fiction', xy=(2000, 180), xytext=(2010, 190),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=10, fontweight='bold', color='orange')

# Tighten layout to fit elements neatly
plt.tight_layout()

# Show the plot
plt.show()