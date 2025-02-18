import matplotlib.pyplot as plt
import numpy as np

# Data
days = ['Funday', 'Workday', 'Humpday', 'AlmostFriday', 'CasualDay', 'Funday', 'LazyDay']
fruit_types = ['GrannySmiths', 'Minions', 'Clementines', 'Blushers']

# Sales data (shuffled within each fruit group)
apples_sales = [60, 30, 55, 80, 25, 75, 50]  # Shuffled values for apples
bananas_sales = [70, 50, 35, 45, 55, 40, 65]  # Shuffled values for bananas
oranges_sales = [20, 40, 55, 30, 25, 35, 50]  # Shuffled values for oranges
grapes_sales = [45, 40, 15, 25, 10, 30, 20]  # Shuffled values for grapes

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
    ax1.text(oranges_sales[i] + 2, i + 0.5*height, f'{oranges_sales[i]}', va='center', ha='left', fontsize=9, color='orange')
for i, sales in enumerate(grapes_sales):
    ax1.text(grapes_sales[i] + 2, i + 1.5*height, f'{grapes_sales[i]}', va='center', ha='left', fontsize=9, color='purple')

# Legend
ax1.legend()

plt.tight_layout()
plt.show()