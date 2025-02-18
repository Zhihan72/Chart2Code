import matplotlib.pyplot as plt
import numpy as np

# Define the decades and associated data
decades = np.arange(1960, 2021, 10)
fiction_books = [150, 180, 200, 220, 250, 280, 310]
non_fiction_books = [100, 120, 140, 160, 180, 200, 220]

fiction_revenue = [450, 500, 550, 600, 700, 750, 800]
non_fiction_revenue = [300, 350, 400, 450, 500, 550, 600]

# Sort data by number of fiction books (ascending order)
sorted_indices_fiction_books = np.argsort(fiction_books)
sorted_decades_fiction_books = decades[sorted_indices_fiction_books]
sorted_fiction_books = np.array(fiction_books)[sorted_indices_fiction_books]
sorted_fiction_revenue = np.array(fiction_revenue)[sorted_indices_fiction_books]

# Sort data by number of non-fiction books (ascending order)
sorted_indices_non_fiction_books = np.argsort(non_fiction_books)
sorted_decades_non_fiction_books = decades[sorted_indices_non_fiction_books]
sorted_non_fiction_books = np.array(non_fiction_books)[sorted_indices_non_fiction_books]
sorted_non_fiction_revenue = np.array(non_fiction_revenue)[sorted_indices_non_fiction_books]

# Create bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 3
ax1.bar(sorted_decades_fiction_books - bar_width, sorted_fiction_books, width=bar_width, color='#6a5acd', alpha=0.7, label='Fiction Books Published')
ax1.bar(sorted_decades_non_fiction_books, sorted_non_fiction_books, width=bar_width, color='#ff6347', alpha=0.7, label='Non-Fiction Books Published')

# Secondary y-axis for revenue
ax2 = ax1.twinx()
ax2.bar(sorted_decades_fiction_books - bar_width, sorted_fiction_revenue, width=bar_width, color='#6a5acd', alpha=0.3, label='Fiction Revenue')
ax2.bar(sorted_decades_non_fiction_books, sorted_non_fiction_revenue, width=bar_width, color='#ff6347', alpha=0.3, label='Non-Fiction Revenue')

# Set titles and labels
ax1.set_title("Popularity and Revenue of Fiction vs Non-Fiction Books (Sorted)", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Decades", fontsize=12)
ax1.set_ylabel("Number of Books Published", fontsize=12)
ax2.set_ylabel("Revenue in Millions (USD)", fontsize=12)

# Grid and legend
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10, title='Books Published')
ax2.legend(loc='upper right', fontsize=10, title='Revenue')

# Tighten layout
plt.tight_layout()
plt.show()