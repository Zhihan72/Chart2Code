import matplotlib.pyplot as plt
import numpy as np

# Data for revenue (in millions) and profit margin (in percentage) from 2015 to 2022
years = np.arange(2015, 2023)

# Manually constructed data
revenue = [55, 60, 72, 88, 104, 130, 160, 190]
profit_margin = [10, 12, 14, 13, 16, 18, 19, 20]  # in percentage

# Convert profit margin to actual profit in millions
profit = [r * p / 100 for r, p in zip(revenue, profit_margin)]

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot revenue data
ax1.plot(years, revenue, color='blue', marker='o', linestyle='-')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis for profit
ax2 = ax1.twinx()
ax2.plot(years, profit, color='green', marker='s', linestyle='--')
ax2.tick_params(axis='y', labelcolor='green')

# Grid for better readability
ax1.grid(True, linestyle='--', color='grey', alpha=0.6)

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()