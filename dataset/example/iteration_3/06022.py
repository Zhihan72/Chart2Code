import matplotlib.pyplot as plt
import numpy as np

# Backstory: 
# We are investigating the popularity of different fruit types in a local market over a week. 
# We will also compare the sale prices of these fruits in a secondary axis.

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fruit_types = ['Apples', 'Bananas', 'Oranges', 'Grapes']

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
x_indexes = np.arange(len(days))
width = 0.2  # width of bars

# Bar plots for each fruit type
ax1.bar(x_indexes - 1.5*width, apples_sales, width=width, color='red', label='Apples')
ax1.bar(x_indexes - 0.5*width, bananas_sales, width=width, color='yellow', label='Bananas')
ax1.bar(x_indexes + 0.5*width, oranges_sales, width=width, color='orange', label='Oranges')
ax1.bar(x_indexes + 1.5*width, grapes_sales, width=width, color='purple', label='Grapes')

# Set up secondary axis for prices
ax2 = ax1.twinx()

# Plot fruit prices on secondary axis
ax2.plot(fruit_types, fruit_prices, 'o--', color='blue', lw=2, label='Fruit Prices')

# Titles and labels
ax1.set_title('Fruit Sales and Prices in a Local Market Over a Week', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Day of the Week', fontsize=12)
ax1.set_ylabel('Number of Units Sold', fontsize=12)
ax2.set_ylabel('Price per Unit ($)', fontsize=12, color='blue')

# Customizing ticks and gridlines
ax1.set_xticks(x_indexes)
ax1.set_xticklabels(days, rotation=45, ha='right')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adding legends
fig.legend(loc='upper right')

# Annotating each bar with the sales numbers for clarity
for i, sales in enumerate(apples_sales):
    ax1.text(i - 1.5*width, apples_sales[i] + 2, f'{apples_sales[i]}', ha='center', va='bottom', fontsize=9, color='red')
for i, sales in enumerate(bananas_sales):
    ax1.text(i - 0.5 * width, bananas_sales[i] + 2, f'{bananas_sales[i]}', ha='center', va='bottom', fontsize=9, color='yellow')
for i, sales in enumerate(oranges_sales):
    ax1.text(i + 0.5 * width, oranges_sales[i] + 2, f'{oranges_sales[i]}', ha='center', va='bottom', fontsize=9, color='orange')
for i, sales in enumerate(grapes_sales):
    ax1.text(i + 1.5 * width, grapes_sales[i] + 2, f'{grapes_sales[i]}', ha='center', va='bottom', fontsize=9, color='purple')

# Adjusting layout
plt.tight_layout()

# Display the plot
plt.show()