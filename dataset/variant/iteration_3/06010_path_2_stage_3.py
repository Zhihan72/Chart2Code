import matplotlib.pyplot as plt
import numpy as np

# Define data: Monthly sales data for a fictional bookstore (in thousands)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
fiction_sales = np.array([20, 25, 23, 28, 30, 35, 33, 30, 27, 32, 35, 40])
non_fiction_sales = np.array([15, 18, 20, 22, 25, 28, 27, 25, 24, 28, 30, 33])
children_sales = np.array([10, 12, 15, 18, 20, 22, 21, 20, 18, 21, 23, 25])
educational_sales = np.array([5, 7, 8, 10, 12, 15, 14, 13, 12, 14, 16, 18])
sci_fi_sales = np.array([8, 10, 12, 14, 16, 18, 17, 15, 14, 16, 18, 20])
biography_sales = np.array([6, 7, 9, 11, 13, 15, 14, 13, 12, 13, 15, 17])

# Total monthly sales data
total_sales = (fiction_sales + non_fiction_sales + children_sales +
               educational_sales + sci_fi_sales + biography_sales)

fig, axs = plt.subplots(1, 2, figsize=(18, 7))

# First subplot: Sorted Bar Chart for Monthly Sales by Genre (using total of individual genres for sorting)
genre_sales = {
    'Fiction': fiction_sales.sum(),
    'Non-Fiction': non_fiction_sales.sum(),
    'Children': children_sales.sum(),
    'Educational': educational_sales.sum(),
    'Sci-Fi': sci_fi_sales.sum(),
    'Biography': biography_sales.sum()
}

sorted_genres = sorted(genre_sales.items(), key=lambda x: x[1])  # Ascending order
genres, values = zip(*sorted_genres)

axs[0].bar(genres, values, color=['#FFC300', '#99FF99', '#C70039', '#FF9999', '#FFCC99', '#66B2FF'], alpha=0.8)
axs[0].set_title("Total Annual Sales by Genre\nFictional Bookstore (2022)", fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel("Book Genre", fontsize=12)
axs[0].set_ylabel("Total Sales (in thousands)", fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Second subplot: Sorted Bar Chart for Total Monthly Sales
sorted_indices = np.argsort(total_sales)  # Ascending order
sorted_month_names = [month_names[i] for i in sorted_indices]
sorted_total_sales = total_sales[sorted_indices]

axs[1].bar(sorted_month_names, sorted_total_sales, color='lightcoral', alpha=0.7)
axs[1].set_title("Total Monthly Book Sales\nFictional Bookstore (2022)", fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel("Months", fontsize=12)
axs[1].set_ylabel("Total Sales (in thousands)", fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()