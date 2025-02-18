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

fig, ax1 = plt.subplots(figsize=(12, 8))

# Indices for placement of bars
y_indexes = np.arange(len(days))
height = 0.2

# Horizontal bar plots for each fruit type
ax1.barh(y_indexes - 1.5*height, apples_sales, height=height, color='red', label='GrannySmiths')
ax1.barh(y_indexes - 0.5*height, bananas_sales, height=height, color='yellow', label='Minions')
ax1.barh(y_indexes + 0.5*height, oranges_sales, height=height, color='orange', label='Clementines')
ax1.barh(y_indexes + 1.5*height, grapes_sales, height=height, color='purple', label='Blushers')

# Set up secondary axis for prices
ax2 = ax1.twiny()

# Prices data
fruit_prices = [1.0, 0.5, 0.75, 2.0]

# Plot fruit prices on secondary axis
ax2.plot(fruit_prices, fruit_types, 'o--', color='blue', lw=2)

# Titles and labels
ax1.set_ylabel('Weekly Cycle', fontsize=12)
ax1.set_xlabel('Sold Units', fontsize=12)
ax2.set_xlabel('Unit Price ($)', fontsize=12, color='blue')

# Customizing ticks
ax1.set_yticks(y_indexes)
ax1.set_yticklabels(days)

# Annotating each bar with the sales numbers
for i, sales in enumerate(apples_sales):
    ax1.text(apples_sales[i] + 2, i - 1.5*height, f'{apples_sales[i]}', va='center', ha='left', fontsize=9, color='red')
for i, sales in enumerate(bananas_sales):
    ax1.text(bananas_sales[i] + 2, i - 0.5*height, f'{bananas_sales[i]}', va='center', ha='left', fontsize=9, color='yellow')
for i, sales in enumerate(oranges_sales):
    ax1.text(oranges_sales[i] + 2, i + 0.5 * height, f'{oranges_sales[i]}', va='center', ha='left', fontsize=9, color='orange')
for i, sales in enumerate(grapes_sales):
    ax1.text(grapes_sales[i] + 2, i + 1.5 * height, f'{grapes_sales[i]}', va='center', ha='left', fontsize=9, color='purple')

# Legend
ax1.legend()

plt.tight_layout()
plt.show()