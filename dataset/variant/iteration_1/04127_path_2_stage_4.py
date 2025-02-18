import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)

revenue = [55, 60, 72, 88, 104, 130, 160, 190]
profit_margin = [10, 12, 14, 13, 16, 18, 19, 20]
marketing_spend = [5, 6, 7, 9, 10, 12, 15, 18]  # New data series for marketing spend

profit = [r * p / 100 for r, p in zip(revenue, profit_margin)]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(years, revenue, color='purple', marker='o', linestyle='-')
ax1.set_xlabel('Yr', fontsize=12)
ax1.set_ylabel('Rev (M)', color='purple', fontsize=12)
ax1.tick_params(axis='y', labelcolor='purple')

ax2 = ax1.twinx()
ax2.plot(years, profit, color='purple', marker='s', linestyle='--', label='Profit')
ax2.plot(years, marketing_spend, color='orange', marker='^', linestyle=':', label='Marketing Spend')  # Added chart for marketing spend
ax2.set_ylabel('Value (M)', fontsize=12)
ax2.tick_params(axis='y')

ax2.legend(loc='upper left')  # Added legend for data series

plt.title("Tech Co. Rev, Prof & Marketing Spend (2015-22)", fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()