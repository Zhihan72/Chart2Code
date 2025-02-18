import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart will represent the "Journey of a Startup" over 5 years, highlighting different metrics' progression:
# Revenue, Expenses, and Profit. The purpose is to show the growth and sustainability of a startup over time.

# Define years
years = np.arange(2018, 2023)

# Define metrics: Revenue, Expenses, and Profit (in thousands of dollars)
revenue = np.array([50, 120, 180, 260, 350])
expenses = np.array([30, 70, 110, 130, 150])
profit = revenue - expenses

# Preamble: Creating the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each line with different styles
ax.plot(years, revenue, marker='o', linestyle='-', linewidth=2, color='blue', label='Revenue')
ax.plot(years, expenses, marker='s', linestyle='--', linewidth=2, color='red', label='Expenses')
ax.plot(years, profit, marker='^', linestyle=':', linewidth=2, color='green', label='Profit')

# Add labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Amount (in thousands of dollars)', fontsize=12)
ax.set_title("Journey of a Startup:\nRevenue, Expenses, and Profit (2018-2022)", fontsize=14, fontweight='bold', pad=20)

# Adding a legend
ax.legend(title='Metrics', loc='upper left', fontsize=10)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Annotate specific data points
ax.annotate('First Major Profit', xy=(2019, profit[1]), xytext=(2019, profit[1] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Expense Control Achieved', xy=(2021, expenses[3]), xytext=(2020, expenses[3] + 30),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Saving figure before display (optional)
# plt.savefig('startup_journey.png', dpi=300)

# Display the plot
plt.show()