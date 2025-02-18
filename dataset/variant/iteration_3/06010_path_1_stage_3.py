import matplotlib.pyplot as plt
import numpy as np

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
fiction_sales = np.array([28, 25, 33, 30, 23, 40, 35, 20, 27, 32, 35, 30])
non_fiction_sales = np.array([25, 18, 24, 22, 20, 33, 28, 15, 27, 28, 30, 25])
children_sales = np.array([18, 12, 21, 18, 10, 25, 22, 15, 20, 21, 23, 20])
educational_sales = np.array([12, 7, 16, 10, 8, 18, 15, 5, 14, 14, 16, 13])

total_sales = fiction_sales + non_fiction_sales + children_sales + educational_sales

fig, axs = plt.subplots(1, 2, figsize=(18, 7))

# Stacked Area Chart
axs[0].stackplot(month_names, fiction_sales, non_fiction_sales, children_sales, educational_sales,
                 colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'], alpha=0.8)
axs[0].set_title("Sales by Genre\n2022", fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel("Months", fontsize=12)
axs[0].set_ylabel("Sales (k)", fontsize=12)
axs[0].yaxis.set_ticks(np.arange(0, 130, 10))

# Total Monthly Sales Chart
axs[1].bar(month_names, total_sales, color='lightcoral', alpha=0.7)
axs[1].plot(month_names, total_sales, color='#FF5733', linewidth=2, marker='o')
axs[1].set_title("Total Sales\n2022", fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel("Months", fontsize=12)
axs[1].set_ylabel("Total Sales (k)", fontsize=12)
for index, value in enumerate(total_sales):
    axs[1].text(index, value + 2, f'{value}k', ha='center', va='bottom', fontsize=9)

# Annotations
axs[0].annotate('Holiday Boost', xy=('Dec', 90), xytext=('Oct', 100),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
axs[1].annotate('Peak', xy=('Dec', 116), xytext=('Sep', 120),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

plt.tight_layout()
plt.show()