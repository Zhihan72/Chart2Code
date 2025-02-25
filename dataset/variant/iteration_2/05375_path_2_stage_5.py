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

# Stacked bar chart
x_indices = np.arange(len(months))
ax1.bar(x_indices, electronics_sales, label='Gadgets', color='salmon', hatch='/')
ax1.bar(x_indices, furniture_sales, bottom=electronics_sales, label='Chairs', color='lightseagreen', hatch='\\')
ax1.bar(x_indices, clothing_sales, bottom=np.array(electronics_sales)+np.array(furniture_sales), label='Attires', color='goldenrod', hatch='.')
ax1.bar(x_indices, books_sales, bottom=np.array(electronics_sales)+np.array(furniture_sales)+np.array(clothing_sales), label='Literature', color='slateblue', hatch='x')

ax1.set_title("Assorted Sales Data", fontsize=16)
ax1.set_xlabel("Period", fontsize=13)
ax1.set_ylabel("Revenue (in thousands)", fontsize=13)
ax1.set_xticks(x_indices)
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