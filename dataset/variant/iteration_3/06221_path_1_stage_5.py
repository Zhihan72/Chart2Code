import matplotlib.pyplot as plt
import numpy as np

genres = ["Fiction", "Non-Fiction", "Science Fiction", "Mystery"]

sales_data = np.array([
    [150, 160, 170, 185, 200, 195, 210, 220, 230, 245, 260],
    [100, 115, 130, 140, 150, 165, 170, 180, 190, 200, 210],
    [75, 80, 90, 95, 110, 120, 130, 140, 150, 160, 170],
    [40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130],
])

total_sales_per_genre = np.sum(sales_data, axis=1)
sorted_indices = np.argsort(total_sales_per_genre)[::-1]
sorted_genres = [genres[i] for i in sorted_indices]
sorted_sales = total_sales_per_genre[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(sorted_genres, sorted_sales, color=['green', 'gold', 'orangered', 'purple'], alpha=0.85)

plt.xlabel('Genres')
plt.ylabel('Total Sales')
plt.title('Total Book Sales by Genre (Sorted)')
plt.show()