import matplotlib.pyplot as plt
import numpy as np

# Define months and fruits
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Figs']

# Sales data (in thousands of units)
sales_apples = np.array([4, 5, 6, 7, 5, 6, 8, 7, 6, 5, 4, 5])
sales_bananas = np.array([6, 7, 8, 9, 8, 7, 8, 9, 6, 7, 6, 5])
sales_cherries = np.array([2, 3, 4, 5, 4, 3, 5, 6, 5, 4, 3, 3])
sales_dates = np.array([1, 2, 2, 3, 2, 1, 2, 2, 3, 4, 5, 4])
sales_elderberries = np.array([0.5, 1, 1.5, 2, 2, 1.5, 2, 2.5, 2, 1.5, 1, 1.5])
sales_figs = np.array([1, 1.5, 2, 2.5, 2, 2.5, 3, 2.5, 2, 2.5, 3, 3.5])

# Positive and negative data (splitting data for diverging chart)
positive_data = np.array([sales_apples, sales_bananas, sales_cherries])
negative_data = np.array([sales_dates, sales_elderberries, sales_figs])

# Determine the number of months
n_months = len(months)

# Define the positions of the bars
x = np.arange(n_months)
bar_width = 0.4

# Create the main plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot diverging bars for positive sales
bottom = np.zeros(n_months)
positive_colors = ['#FF9999', '#FFE4B5', '#E37222']
for i, (sales, color) in enumerate(zip(positive_data, positive_colors)):
    ax.bar(x, sales, width=bar_width, color=color, label=fruits[i], bottom=bottom)
    bottom += sales

# Plot diverging bars for negative sales (inverted)
bottom = np.zeros(n_months)
negative_colors = ['#8B4513', '#8FBC8F', '#DB7093']
for i, (sales, color) in enumerate(zip(negative_data, negative_colors)):
    ax.bar(x, -sales, width=bar_width, color=color, label=fruits[i + 3], bottom=bottom)
    bottom -= sales

# Add labels and title
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales (in thousands of units)', fontsize=12)
ax.set_title('Monthly Fruit Sales Performance (Diverging) in Grocery Store\n(Jan - Dec)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(months)

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=30, ha='right')

# Highlight the central axis
ax.axhline(0, color='gray', linewidth=0.8)

# Add a legend
ax.legend(title='Fruits', fontsize=10)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()