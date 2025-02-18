import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
# Randomly altered revenues and expenses while maintaining their dimensions
revenues = [10, 6, 9, 8, 9, 12, 11, 14, 5, 16] 
expenses = [5, 4, 4, 5, 3, 6.5, 3.5, 5, 6.5, 4]

profits = np.array(revenues) - np.array(expenses)
market_shares = [16, 18, 20, 22, 23, 25, 26, 27, 29, 31]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 0.4
ax1.bar(years - bar_width/2, revenues, width=bar_width, color='steelblue', label='Revenue ($ billion)')
ax1.bar(years + bar_width/2, expenses, width=bar_width, color='salmon', label='Expense ($ billion)')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Revenue and Expense (in billion $)', fontsize=14, color='black')
ax1.set_title('Company Performance Metrics over a Decade', fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', fontsize=12)

ax2 = ax1.twinx()
ax2.plot(years, profits, color='darkorange', marker='o', linestyle='-', linewidth=2, label='Profit ($ billion)')
ax2.set_ylabel('Profit (in billion $)', fontsize=14, color='darkorange')
for i, profit in enumerate(profits):
    ax2.text(years[i], profit + 0.2, f'{profit:.1f}', color='darkorange', ha='center')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, market_shares, color='mediumseagreen', marker='d', linestyle='-', linewidth=2, label='Market Share (%)')
ax3.set_ylabel('Market Share (%)', fontsize=14, color='mediumseagreen')
for i, share in enumerate(market_shares):
    ax3.text(years[i], share + 0.5, f'{share}%', color='mediumseagreen', ha='center')

ax3.spines['right'].set_visible(True)

fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3, fontsize=12)

plt.tight_layout()

plt.show()