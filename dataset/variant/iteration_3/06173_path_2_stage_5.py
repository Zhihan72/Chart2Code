import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
revenues = [10, 6, 9, 8, 9, 12, 11, 14, 5, 16]
expenses = [5, 4, 4, 5, 3, 6.5, 3.5, 5, 6.5, 4]

profits = np.array(revenues) - np.array(expenses)
market_shares = [16, 18, 20, 22, 23, 25, 26, 27, 29, 31]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_height = 0.4
ax1.barh(years - bar_height/2, revenues, height=bar_height, color='lightcoral', label='Revenues')
ax1.barh(years + bar_height/2, expenses, height=bar_height, color='skyblue', label='Expenses')
ax1.set_yticks(years)
ax1.grid(True, which='both', axis='x', linestyle='--', linewidth=0.7, color='gray')

ax2 = ax1.twiny()
ax2.plot(profits, years, color='darkviolet', marker='x', linestyle='--', linewidth=1.5, label='Profits')
for i, profit in enumerate(profits):
    ax2.text(profit + 0.2, years[i], f'{profit:.1f}', color='darkviolet', va='center')

ax3 = ax1.twiny()
ax3.spines['top'].set_position(('outward', 50))
ax3.plot(market_shares, years, color='forestgreen', marker='s', linestyle=':', linewidth=1.0, label='Market Shares')
for i, share in enumerate(market_shares):
    ax3.text(share + 0.2, years[i], f'{share}%', color='forestgreen', va='center')

ax3.spines['top'].set_visible(True)

ax1.spines['left'].set_color('crimson')
ax2.spines['top'].set_visible(False)
ax1.spines['top'].set_visible(False)

ax1.legend(loc='lower right')
ax2.legend(loc='upper right')
ax3.legend(loc='upper left', bbox_to_anchor=(0.5, 1.15), ncol=3)

plt.tight_layout()
plt.show()