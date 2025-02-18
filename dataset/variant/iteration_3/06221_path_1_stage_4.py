import matplotlib.pyplot as plt
import numpy as np

genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery"]

sales_data = np.array([
    [150, 160, 170, 185, 200, 195, 210, 220, 230, 245, 260],
    [100, 115, 130, 140, 150, 165, 170, 180, 190, 200, 210],
    [75, 80, 90, 95, 110, 120, 130, 140, 150, 160, 170],
    [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    [40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130],
])

# Calculate total sales for each genre
total_sales_per_genre = np.sum(sales_data, axis=1)

# Sort the genres by total sales in descending order
sorted_indices = np.argsort(total_sales_per_genre)[::-1]
sorted_genres = [genres[i] for i in sorted_indices]
sorted_sales = total_sales_per_genre[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the sorted bar chart
ax.bar(sorted_genres, sorted_sales, color=['green', 'gold', 'orangered', 'dodgerblue', 'purple'], alpha=0.85)

plt.xlabel('Genres')
plt.ylabel('Total Sales')
plt.title('Total Book Sales by Genre (Sorted)')
plt.show()