import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
fruits = ['Apples', 'Bananas', 'Cherries', 'Grapes', 'Dates', 'Elderberries', 'Figs', 'Honeydew', 'Jackfruit']

sales_apples = np.array([4, 5, 6, 7, 5, 6, 8, 7, 6, 5, 4, 5])
sales_bananas = np.array([6, 7, 8, 9, 8, 7, 8, 9, 6, 7, 6, 5])
sales_cherries = np.array([2, 3, 4, 5, 4, 3, 5, 6, 5, 4, 3, 3])
sales_grapes = np.array([3, 4, 4, 5, 3, 4, 5, 6, 4, 3, 4, 4])
sales_dates = np.array([1, 2, 2, 3, 2, 1, 2, 2, 3, 4, 5, 4])
sales_elderberries = np.array([0.5, 1, 1.5, 2, 2, 1.5, 2, 2.5, 2, 1.5, 1, 1.5])
sales_figs = np.array([1, 1.5, 2, 2.5, 2, 2.5, 3, 2.5, 2, 2.5, 3, 3.5])
sales_honeydew = np.array([2, 2, 2.5, 3, 2.5, 3, 3.5, 3, 2.5, 3, 3.5, 3])
sales_jackfruit = np.array([0.8, 1, 1.2, 1.5, 1.3, 1.6, 2, 1.8, 2, 2.2, 1.8, 2])

positive_data = np.array([sales_apples, sales_bananas, sales_cherries, sales_grapes, sales_honeydew])
negative_data = np.array([sales_dates, sales_elderberries, sales_figs, sales_jackfruit])

n_months = len(months)
x = np.arange(n_months)
bar_width = 0.4

fig, ax = plt.subplots(figsize=(14, 8))

# Altered positive colors and shuffled the order
positive_colors = ['#FFE4B5', '#DA70D6', '#FF9999', '#87CEFA', '#E37222']
bottom = np.zeros(n_months)
for i, (sales, color) in enumerate(zip(positive_data, positive_colors)):
    ax.bar(x, sales, width=bar_width, color=color, label=fruits[i], bottom=bottom, edgecolor='black', hatch='//')
    bottom += sales

# Altered negative colors and shuffled the order
negative_colors = ['#DB7093', '#8B4513', '#FFD700', '#8FBC8F']
bottom = np.zeros(n_months)
for i, (sales, color) in enumerate(zip(negative_data, negative_colors)):
    ax.bar(x, -sales, width=bar_width, color=color, label=fruits[i + 5], bottom=bottom, edgecolor='black', linestyle=':')
    bottom -= sales

ax.set_xlabel('Month', fontsize=10)
ax.set_ylabel('Sales (in thousands)', fontsize=10)
ax.set_title('Monthly Fruit Sales Performance (Diverging)', fontsize=15, fontweight='bold')

# Removed gridlines for a cleaner look
# Added gridlines on y-axis
ax.yaxis.grid(True, linestyle='-.', alpha=0.3)

# Changed rotation of x-axis labels
plt.xticks(rotation=45, ha='right')

# Changed the central axis to a dashed line
ax.axhline(0, color='blue', linewidth=1, linestyle='--')

# Changed the legend location and title
ax.legend(title='Fruit Types', fontsize=9, loc='upper left')

plt.tight_layout()
plt.show()