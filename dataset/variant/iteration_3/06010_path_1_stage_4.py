import matplotlib.pyplot as plt
import numpy as np

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
fiction_sales = np.array([28, 25, 33, 30, 23, 40, 35, 20, 27, 32, 35, 30])
non_fiction_sales = np.array([25, 18, 24, 22, 20, 33, 28, 15, 27, 28, 30, 25])
children_sales = np.array([18, 12, 21, 18, 10, 25, 22, 15, 20, 21, 23, 20])
educational_sales = np.array([12, 7, 16, 10, 8, 18, 15, 5, 14, 14, 16, 13])

total_sales = fiction_sales + non_fiction_sales + children_sales + educational_sales

fig, axs = plt.subplots(1, 2, figsize=(18, 7))

# Stacked Horizontal Bar Chart for Sales by Genre
bar_width = 0.5
axs[0].barh(month_names, fiction_sales, color='#FF9999', alpha=0.8, label='Fiction')
axs[0].barh(month_names, non_fiction_sales, color='#66B2FF', alpha=0.8, left=fiction_sales, label='Non-Fiction')
axs[0].barh(month_names, children_sales, color='#99FF99', alpha=0.8, left=fiction_sales + non_fiction_sales, label='Children')
axs[0].barh(month_names, educational_sales, color='#FFCC99', alpha=0.8, left=fiction_sales + non_fiction_sales + children_sales, label='Educational')
axs[0].set_title("Sales by Genre\n2022", fontsize=14, fontweight='bold', pad=20)
axs[0].set_ylabel("Months", fontsize=12)
axs[0].set_xlabel("Sales (k)", fontsize=12)
axs[0].legend(loc='upper left', fontsize=9)

# Horizontal Bar Chart for Total Monthly Sales
axs[1].barh(month_names, total_sales, color='lightcoral', alpha=0.7)
axs[1].set_title("Total Sales\n2022", fontsize=14, fontweight='bold', pad=20)
axs[1].set_ylabel("Months", fontsize=12)
axs[1].set_xlabel("Total Sales (k)", fontsize=12)
for index, value in enumerate(total_sales):
    axs[1].text(value + 2, index, f'{value}k', va='center', fontsize=9)

# Annotations adjusted for horizontal orientation
axs[0].annotate('Holiday Boost', xy=(90, 'Dec'), xytext=(100, 'Oct'),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
axs[1].annotate('Peak', xy=(116, 'Dec'), xytext=(120, 'Sep'),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

plt.tight_layout()
plt.show()