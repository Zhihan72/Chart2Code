import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are tracking the sales of four different fruit juices (Apple, Orange, Grape, and Pineapple)
# over the last ten years (2013 - 2022). The chart will display the annual sales figures for each
# juice type and the total annual sales.

# Define the time range for the x-axis (years from 2013 to 2022)
years = np.arange(2013, 2023)

# Sales data for each type of fruit juice over the ten years (in thousands of liters)
apple_sales = np.array([50, 55, 60, 70, 80, 85, 90, 100, 110, 120])
orange_sales = np.array([45, 48, 50, 55, 60, 65, 70, 75, 80, 85])
grape_sales = np.array([30, 32, 35, 40, 45, 48, 50, 55, 60, 65])
pineapple_sales = np.array([20, 22, 25, 28, 30, 35, 40, 42, 45, 50])

# Calculate the total annual sales for all juice types combined
total_sales = apple_sales + orange_sales + grape_sales + pineapple_sales

# Create figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the individual sales lines for each juice type
ax.plot(years, apple_sales, marker='o', linestyle='-', color='green', label='Apple Juice')
ax.plot(years, orange_sales, marker='v', linestyle='--', color='orange', label='Orange Juice')
ax.plot(years, grape_sales, marker='s', linestyle='-.', color='purple', label='Grape Juice')
ax.plot(years, pineapple_sales, marker='D', linestyle=':', color='gold', label='Pineapple Juice')

# Plot the total sales line
ax.plot(years, total_sales, marker='*', linestyle='-', linewidth=2, color='black', label='Total Sales', alpha=0.7)

# Set chart title and labels
ax.set_title('Annual Sales of Various Fruit Juices (2013-2022)', fontsize=18, fontweight='bold')
ax.set_xlabel('Years', fontsize=14, labelpad=10)
ax.set_ylabel('Sales (in thousands of liters)', fontsize=14, labelpad=10)

# Customize x-axis ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(title='Juice Type', loc='upper left', fontsize=12, frameon=False)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()