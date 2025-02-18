import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
revenues = [5, 6, 7, 8, 9, 10, 11, 12, 14, 16]
profits = [2, 2.5, 3.5, 4, 5, 5.5, 6, 6.5, 8, 9.5]
market_shares = [16, 18, 20, 22, 23, 25, 26, 27, 29, 31]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_height = 0.4
ax1.barh(years, revenues, height=bar_height, color='maroon', label='Income (Billion $)')
ax1.set_ylabel('Timeline', fontsize=14)
ax1.set_xlabel('Income Streams (B$)', fontsize=14, color='black')
ax1.set_title('Decade Overview of Business Indicators', fontsize=16, fontweight='bold', pad=20)
ax1.set_yticks(years)
ax1.set_yticklabels(years)

ax1.grid(visible=True, which='major', linestyle='--', linewidth=0.7, color='grey')

ax1.legend(loc='lower left', fontsize=12)

ax2 = ax1.twiny()
ax2.plot(profits, years, color='seagreen', marker='x', linestyle='--', linewidth=2, label='Earnings (Billion $)')
ax2.set_xlabel('Net Income (B$)', fontsize=14, color='seagreen')
for i, profit in enumerate(profits):
    ax2.text(profit + 0.2, years[i], f'{profit:.1f}', color='seagreen', va='center')

ax3 = ax1.twiny()
ax3.spines['top'].set_position(('outward', 60))
ax3.plot(market_shares, years, color='darkorange', marker='v', linestyle='-', linewidth=2, label='Market Dominance (%)')
ax3.set_xlabel('Dominance (%)', fontsize=14, color='darkorange')
for i, share in enumerate(market_shares):
    ax3.text(share + 0.5, years[i], f'{share}%', color='darkorange', va='center')
ax3.spines['top'].set_visible(True)

fig.legend(loc='lower right', bbox_to_anchor=(0.9, -0.04), ncol=3, fontsize=12)

plt.tight_layout()
plt.show()