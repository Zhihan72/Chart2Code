import matplotlib.pyplot as plt
import numpy as np

# Data for months and fruits
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
fruits = ['Elderberries', 'Apples', 'Cherries', 'Bananas', 'Dates', 'Honeydew', 'Figs', 'Jackfruit', 'Grapes']

# Sales data for fruits
sales_apples = np.array([4, 5, 6, 7, 5, 6, 8, 7, 6, 5, 4, 5])
sales_bananas = np.array([6, 7, 8, 9, 8, 7, 8, 9, 6, 7, 6, 5])
sales_cherries = np.array([2, 3, 4, 5, 4, 3, 5, 6, 5, 4, 3, 3])
sales_grapes = np.array([3, 4, 4, 5, 3, 4, 5, 6, 4, 3, 4, 4])
sales_dates = np.array([1, 2, 2, 3, 2, 1, 2, 2, 3, 4, 5, 4])
sales_elderberries = np.array([0.5, 1, 1.5, 2, 2, 1.5, 2, 2.5, 2, 1.5, 1, 1.5])
sales_figs = np.array([1, 1.5, 2, 2.5, 2, 2.5, 3, 2.5, 2, 2.5, 3, 3.5])
sales_honeydew = np.array([2, 2, 2.5, 3, 2.5, 3, 3.5, 3, 2.5, 3, 3.5, 3])
sales_jackfruit = np.array([0.8, 1, 1.2, 1.5, 1.3, 1.6, 2, 1.8, 2, 2.2, 1.8, 2])

positive_data = np.array([sales_honeydew, sales_apples, sales_cherries, sales_bananas, sales_grapes])
negative_data = np.array([sales_jackfruit, sales_figs, sales_elderberries, sales_dates])

n_months = len(months)
x = np.arange(n_months)
bar_width = 0.4

fig, ax = plt.subplots(figsize=(14, 8))

# Positive sales data plotting
positive_colors = ['#E37222', '#FFE4B5', '#FF9999', '#DA70D6', '#87CEFA']
bottom = np.zeros(n_months)
for i, (sales, color) in enumerate(zip(positive_data, positive_colors)):
    ax.bar(x, sales, width=bar_width, color=color, label=fruits[i + 1], bottom=bottom, edgecolor='black', hatch='//')
    bottom += sales

# Negative sales data plotting
negative_colors = ['#8FBC8F', '#FFD700', '#DB7093', '#8B4513']
bottom = np.zeros(n_months)
for i, (sales, color) in enumerate(zip(negative_data, negative_colors)):
    ax.bar(x, -sales, width=bar_width, color=color, label=fruits[i + 5], bottom=bottom, edgecolor='black', linestyle=':')
    bottom -= sales

# Changed textual elements
ax.set_xlabel('Calendar Month', fontsize=10)
ax.set_ylabel('Fruit Sales (in 1000s)', fontsize=10)
ax.set_title('Fruit Sales Trends over the Year', fontsize=15, fontweight='bold')

# Gridlines and x-ticks
ax.yaxis.grid(True, linestyle='-.', alpha=0.3)
plt.xticks(rotation=45, ha='right')

# Central axis
ax.axhline(0, color='blue', linewidth=1, linestyle='--')

# Legend
ax.legend(title='Type of Fruit', fontsize=9, loc='upper right')

plt.tight_layout()
plt.show()