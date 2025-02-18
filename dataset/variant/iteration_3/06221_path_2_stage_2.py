import matplotlib.pyplot as plt
import numpy as np

# Book genres
genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery"]

# Aggregate book sales data (sum over years)
total_sales = np.array([1735, 1670, 1320, 1200, 995])  # Precomputed sum for each genre

# Sorting the genres based on total sales
sorted_indices = np.argsort(total_sales)[::-1]  # Use [::-1] for descending order

sorted_genres = np.array(genres)[sorted_indices]
sorted_sales = total_sales[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(sorted_genres, sorted_sales, color=['dodgerblue', 'orangered', 'green', 'purple', 'gold'], alpha=0.85)

ax.set_xlabel('Genre', fontsize=12)
ax.set_ylabel('Total Book Sales (in thousands)', fontsize=12)
ax.set_title('Total Book Sales by Genre (2010-2020)', fontsize=16, fontweight='bold')

for i, val in enumerate(sorted_sales):
    ax.text(i, val + 5, str(val), ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()