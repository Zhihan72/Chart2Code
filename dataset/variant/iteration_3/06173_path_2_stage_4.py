import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
revenues = [10, 6, 9, 8, 9, 12, 11, 14, 5, 16]
expenses = [5, 4, 4, 5, 3, 6.5, 3.5, 5, 6.5, 4]

profits = np.array(revenues) - np.array(expenses)
market_shares = [16, 18, 20, 22, 23, 25, 26, 27, 29, 31]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 0.4
ax1.bar(years - bar_width/2, revenues, width=bar_width, color='lightcoral')
ax1.bar(years + bar_width/2, expenses, width=bar_width, color='skyblue')
ax1.set_xticks(years)
ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, color='gray')

ax2 = ax1.twinx()
ax2.plot(years, profits, color='darkviolet', marker='x', linestyle='--', linewidth=1.5)
for i, profit in enumerate(profits):
    ax2.text(years[i], profit + 0.2, f'{profit:.1f}', color='darkviolet', ha='center')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 80))
ax3.plot(years, market_shares, color='forestgreen', marker='s', linestyle=':', linewidth=1.0)
for i, share in enumerate(market_shares):
    ax3.text(years[i], share + 0.5, f'{share}%', color='forestgreen', ha='center')

ax3.spines['right'].set_visible(True)

ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_color('crimson')
ax1.spines['right'].set_color('darkgreen')

ax1.legend(['Revenues', 'Expenses'], loc='upper left')
ax2.legend(['Profits'], loc='upper right')
ax3.legend(['Market Shares'], loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)

plt.tight_layout()
plt.show()