import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2021, 10)

# Shuffled data for random alteration while preserving structure
fiction_books = [220, 180, 310, 150, 280, 200, 250]  # Manually shuffled
non_fiction_books = [140, 220, 160, 100, 180, 200, 120]  # Manually shuffled

# Revenue data with altered values
fiction_revenue = [700, 550, 800, 450, 750, 500, 600] # Manually shuffled
non_fiction_revenue = [500, 600, 450, 300, 350, 550, 400] # Manually shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 3
ax1.bar(decades - bar_width, fiction_books, width=bar_width, color='#6a5acd', alpha=0.7, label='Fiction Books Published')
ax1.bar(decades, non_fiction_books, width=bar_width, color='#ff6347', alpha=0.7, label='Non-Fiction Books Published')

ax2 = ax1.twinx()
ax2.bar(decades - bar_width, fiction_revenue, width=bar_width, color='#6a5acd', alpha=0.3, label='Fiction Revenue')
ax2.bar(decades, non_fiction_revenue, width=bar_width, color='#ff6347', alpha=0.3, label='Non-Fiction Revenue')

ax1.set_title("Popularity and Revenue of Fiction vs Non-Fiction Books (1960-2020)", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Decades", fontsize=12)
ax1.set_ylabel("Number of Books Published", fontsize=12)
ax2.set_ylabel("Revenue in Millions (USD)", fontsize=12)

ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10, title='Books Published')
ax2.legend(loc='upper right', fontsize=10, title='Revenue')

plt.tight_layout()
plt.show()