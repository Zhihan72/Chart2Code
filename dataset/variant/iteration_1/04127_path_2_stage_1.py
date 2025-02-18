import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)
revenue = [55, 60, 72, 88, 104, 130, 160, 190]
profit_margin = [10, 12, 14, 13, 16, 18, 19, 20]

profit = [r * p / 100 for r, p in zip(revenue, profit_margin)]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(years, revenue, color='blue', marker='o', linestyle='-')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue (Millions)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(years, profit, color='green', marker='s', linestyle='--')
ax2.set_ylabel('Profit (Millions)', color='green', fontsize=12)
ax2.tick_params(axis='y', labelcolor='green')

plt.title("Tracking Tech Company's Yearly Revenue and Profit Trends\nfrom 2015-2022",
          fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()