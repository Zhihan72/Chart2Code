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

# First subplot: Stacked Area Chart with shuffled colors
axs[0].stackplot(month_names, fiction_sales, non_fiction_sales, children_sales, educational_sales, sci_fi_sales, biography_sales,
                 labels=['Fiction', 'Non-Fiction', 'Children', 'Educational', 'Sci-Fi', 'Biography'],
                 colors=['#FFC300', '#99FF99', '#C70039', '#FF9999', '#FFCC99', '#66B2FF'], alpha=0.8)
axs[0].set_title("Monthly Book Sales by Genre\nFictional Bookstore (2022)", fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel("Months", fontsize=12)
axs[0].set_ylabel("Sales (in thousands)", fontsize=12)
axs[0].legend(title="Book Genre", loc="upper left", fontsize=11, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].yaxis.set_ticks(np.arange(0, 180, 10))

# Second subplot: Total Monthly Sales Line Chart with Bar
axs[1].bar(month_names, total_sales, color='lightcoral', alpha=0.7)
axs[1].plot(month_names, total_sales, label='Total Sales', color='#FF5733', linewidth=2, marker='o')
axs[1].set_title("Total Monthly Book Sales\nFictional Bookstore (2022)", fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel("Months", fontsize=12)
axs[1].set_ylabel("Total Sales (in thousands)", fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.5)
for index, value in enumerate(total_sales):
    axs[1].text(index, value + 2, f'{value}k', ha='center', va='bottom', fontsize=9)

# Annotations
axs[0].annotate('Holiday Season Boost', xy=('Dec', 140), xytext=('Oct', 150),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
axs[1].annotate('Peak Sales', xy=('Dec', 160), xytext=('Sep', 170),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

plt.tight_layout()
plt.show()