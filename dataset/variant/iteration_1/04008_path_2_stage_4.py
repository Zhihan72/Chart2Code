import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

revenue = np.array([180, 120, 350, 50, 260])
expenses = np.array([110, 70, 150, 30, 130])
profit = np.array([70, 50, 200, 20, 130])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, revenue, marker='d', linestyle='-.', linewidth=2, color='purple', label='Revenue')
ax.plot(years, expenses, marker='*', linestyle='-', linewidth=2, color='teal', label='Expenses')
ax.plot(years, profit, marker='p', linestyle='--', linewidth=2, color='orange', label='Profit')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Amount (k$)', fontsize=12)
ax.set_title("Startup Financial Metrics", fontsize=16, fontweight='bold', pad=15)

ax.legend(title='Financial Data', loc='lower right', fontsize=10)

ax.grid(True, linestyle='-', alpha=0.8)

ax.annotate('High Profit', xy=(2019, profit[1]), xytext=(2019, profit[1] + 70),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=11)
ax.annotate('Expense Managed', xy=(2021, expenses[3]), xytext=(2020, expenses[3] + 50),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=11)

plt.tight_layout()

plt.show()