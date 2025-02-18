import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

revenue = np.array([180, 120, 350, 50, 260])
expenses = np.array([110, 70, 150, 30, 130])
profit = np.array([70, 50, 200, 20, 130])

fig, ax = plt.subplots(figsize=(12, 7))

# Shuffle the assigned colors for each data group
ax.plot(years, revenue, marker='o', linestyle='-', linewidth=2, color='red', label='Revenue')
ax.plot(years, expenses, marker='s', linestyle='--', linewidth=2, color='green', label='Expenses')
ax.plot(years, profit, marker='^', linestyle=':', linewidth=2, color='blue', label='Profit')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Amount (in thousands of dollars)', fontsize=12)
ax.set_title("Journey of a Startup:\nRevenue, Expenses, and Profit (2018-2022)", fontsize=14, fontweight='bold', pad=20)

ax.legend(title='Metrics', loc='upper left', fontsize=10)

ax.grid(True, linestyle='--', alpha=0.6)

ax.annotate('First Major Profit', xy=(2019, profit[1]), xytext=(2019, profit[1] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Expense Control Achieved', xy=(2021, expenses[3]), xytext=(2020, expenses[3] + 30),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()

plt.show()