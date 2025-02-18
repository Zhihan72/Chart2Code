import matplotlib.pyplot as plt
import numpy as np

# Data
days = ['Funday', 'Workday', 'Humpday', 'AlmostFriday', 'CasualDay', 'Funday', 'LazyDay']
fruit_types = ['GrannySmiths', 'Minions', 'Clementines', 'Blushers']

# Sales data
apples_sales = [30, 25, 50, 55, 60, 75, 80]
bananas_sales = [40, 35, 45, 50, 55, 65, 70]
oranges_sales = [20, 25, 30, 35, 40, 50, 55]
grapes_sales = [10, 15, 20, 25, 30, 40, 45]

# Set up figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Indices for placement of bars
x_indexes = np.arange(len(days))
width = 0.2

# Bar plots for each fruit type
ax1.bar(x_indexes - 1.5*width, apples_sales, width=width, color='red')
ax1.bar(x_indexes - 0.5*width, bananas_sales, width=width, color='yellow')
ax1.bar(x_indexes + 0.5*width, oranges_sales, width=width, color='orange')
ax1.bar(x_indexes + 1.5*width, grapes_sales, width=width, color='purple')

# Set up secondary axis for prices
ax2 = ax1.twinx()

# Prices data
fruit_prices = [1.0, 0.5, 0.75, 2.0]

# Plot fruit prices on secondary axis
ax2.plot(fruit_types, fruit_prices, 'o--', color='blue', lw=2)

# Titles and labels
ax1.set_xlabel('Weekly Cycle', fontsize=12)
ax1.set_ylabel('Sold Units', fontsize=12)
ax2.set_ylabel('Unit Price ($)', fontsize=12, color='blue')

# Customizing ticks
ax1.set_xticks(x_indexes)
ax1.set_xticklabels(days, rotation=45, ha='right')

# Annotating each bar with the sales numbers
for i, sales in enumerate(apples_sales):
    ax1.text(i - 1.5*width, apples_sales[i] + 2, f'{apples_sales[i]}', ha='center', va='bottom', fontsize=9, color='red')
for i, sales in enumerate(bananas_sales):
    ax1.text(i - 0.5*width, bananas_sales[i] + 2, f'{bananas_sales[i]}', ha='center', va='bottom', fontsize=9, color='yellow')
for i, sales in enumerate(oranges_sales):
    ax1.text(i + 0.5 * width, oranges_sales[i] + 2, f'{oranges_sales[i]}', ha='center', va='bottom', fontsize=9, color='orange')
for i, sales in enumerate(grapes_sales):
    ax1.text(i + 1.5 * width, grapes_sales[i] + 2, f'{grapes_sales[i]}', ha='center', va='bottom', fontsize=9, color='purple')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()