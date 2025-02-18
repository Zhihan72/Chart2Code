import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# "Tracking Tech Company's Yearly Revenue and Profit Trends from 2015-2022"
# A tech company has been steadily growing over the past years. We want to track and visualize 
# both their revenue and profit margins over time to identify trends.

# Data for revenue (in millions) and profit margin (in percentage) from 2015 to 2022
years = np.arange(2015, 2023)

# Manually constructed data (no random values as requested)
revenue = [55, 60, 72, 88, 104, 130, 160, 190]
profit_margin = [10, 12, 14, 13, 16, 18, 19, 20]  # in percentage

# Convert profit margin to actual profit in millions
profit = [r * p / 100 for r, p in zip(revenue, profit_margin)]

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot revenue data
ax1.plot(years, revenue, color='blue', marker='o', linestyle='-', label="Revenue (Millions)")
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue (Millions)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis for profit
ax2 = ax1.twinx()
ax2.plot(years, profit, color='green', marker='s', linestyle='--', label="Profit (Millions)")
ax2.set_ylabel('Profit (Millions)', color='green', fontsize=12)
ax2.tick_params(axis='y', labelcolor='green')

# Titles and labels
plt.title("Tracking Tech Company's Yearly Revenue and Profit Trends\nfrom 2015-2022",
          fontsize=14, fontweight='bold', pad=20)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Grid for better readability
ax1.grid(True, linestyle='--', color='grey', alpha=0.6)

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()