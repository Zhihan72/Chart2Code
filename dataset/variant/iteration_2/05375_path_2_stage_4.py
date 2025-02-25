import matplotlib.pyplot as plt
import numpy as np

# Monthly sales data with altered labels
months = ['Fbp', 'Aar', 'Nvo', 'Jul', 'Dec', 'May', 'Jan', 'Sep', 'Oct', 'Apr', 'Mar', 'Aug']
electronics_sales = [25, 30, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75]
furniture_sales = [20, 25, 22, 30, 35, 40, 38, 42, 45, 50, 48, 52]
clothing_sales = [15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
books_sales = [10, 12, 15, 18, 20, 22, 27, 30, 35, 40, 45, 50]

# Overall sales distribution with shuffled categories
overall_sales = np.array([sum(electronics_sales), sum(furniture_sales), sum(clothing_sales), sum(books_sales)])
categories = ['Books', 'Electronics', 'Clothing', 'Furniture']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Bar chart with grouped bars
bar_width = 0.2
x_indices = np.arange(len(months))

ax1.bar(x_indices, electronics_sales, bar_width, label='Gadgets', color='salmon', hatch='/')
ax1.bar(x_indices + bar_width, furniture_sales, bar_width, label='Chairs', color='lightseagreen', hatch='\\')
ax1.bar(x_indices + 2 * bar_width, clothing_sales, bar_width, label='Attires', color='goldenrod', hatch='.')
ax1.bar(x_indices + 3 * bar_width, books_sales, bar_width, label='Literature', color='slateblue', hatch='x')

ax1.set_title("Assorted Sales Data", fontsize=16)
ax1.set_xlabel("Period", fontsize=13)
ax1.set_ylabel("Revenue (in thousands)", fontsize=13)
ax1.set_xticks(x_indices + 1.5 * bar_width)
ax1.set_xticklabels(months, rotation=60, horizontalalignment='right')
ax1.legend(title="Category", fontsize=9, loc="upper left", frameon=False)
ax1.grid(axis='y', linestyle='-', color='lightgrey')

# Pie chart
ax2.pie(overall_sales, labels=categories, autopct='%1.1f%%', startangle=90, 
        colors=['slateblue', 'salmon', 'goldenrod', 'lightseagreen'], 
        wedgeprops=dict(edgecolor='k'))

ax2.set_title("Overall Revenue Split", fontsize=16)

plt.tight_layout(pad=3.0)
plt.show()