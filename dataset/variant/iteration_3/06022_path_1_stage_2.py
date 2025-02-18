import matplotlib.pyplot as plt
import numpy as np

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Sales data: lists of number of fruits sold each day 
apples_sales = [30, 25, 50, 55, 60, 75, 80]
bananas_sales = [40, 35, 45, 50, 55, 65, 70]
oranges_sales = [20, 25, 30, 35, 40, 50, 55]
grapes_sales = [10, 15, 20, 25, 30, 40, 45]

# Prices data: price per unit in dollars
fruit_prices = [1.0, 0.5, 0.75, 2.0]  # Prices of Apples, Bananas, Oranges, Grapes

# Setting up figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Indices for placement of bars
y_indexes = np.arange(len(days))
height = 0.2  # height of bars in horizontal bar chart

# Single color for all bar plots
bar_color = 'green'

# Horizontal bar plots for each fruit type
ax1.barh(y_indexes - 1.5 * height, apples_sales, height=height, color=bar_color, label='Apples')
ax1.barh(y_indexes - 0.5 * height, bananas_sales, height=height, color=bar_color, label='Bananas')
ax1.barh(y_indexes + 0.5 * height, oranges_sales, height=height, color=bar_color, label='Oranges')
ax1.barh(y_indexes + 1.5 * height, grapes_sales, height=height, color=bar_color, label='Grapes')

# Set up secondary axis for prices
ax2 = ax1.twiny()

# Plot fruit prices - considering it secondary to the main horizontal bar chart, this plot might not make sense as before,
# thus it is better to reconsider how to represent this secondary data if needed.

# Titles and labels
ax1.set_title('Fruit Sales and Prices in a Local Market Over a Week', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Day of the Week', fontsize=12)
ax1.set_xlabel('Number of Units Sold', fontsize=12)

# Customizing ticks and gridlines
ax1.set_yticks(y_indexes)
ax1.set_yticklabels(days)
ax1.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adding legends
fig.legend(loc='upper right')

# Annotating each bar with the sales numbers for clarity
for i, sales in enumerate(apples_sales):
    ax1.text(apples_sales[i] + 2, i - 1.5 * height, f'{apples_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(bananas_sales):
    ax1.text(bananas_sales[i] + 2, i - 0.5 * height, f'{bananas_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(oranges_sales):
    ax1.text(oranges_sales[i] + 2, i + 0.5 * height, f'{oranges_sales[i]}', va='center', fontsize=9, color=bar_color)
for i, sales in enumerate(grapes_sales):
    ax1.text(grapes_sales[i] + 2, i + 1.5 * height, f'{grapes_sales[i]}', va='center', fontsize=9, color=bar_color)

# Adjusting layout
plt.tight_layout()

# Display the plot
plt.show()