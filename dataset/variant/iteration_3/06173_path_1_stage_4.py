import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
revenues = [5, 6, 7, 8, 9, 10, 11, 12, 14, 16]
profits = [2, 2.5, 3.5, 4, 5, 5.5, 6, 6.5, 8, 9.5]
market_shares = [16, 18, 20, 22, 23, 25, 26, 27, 29, 31]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 0.4
ax1.bar(years, revenues, width=bar_width, color='maroon', label='Income (Billion $)')
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Income Streams (B$)', fontsize=14, color='black')
ax1.set_title('Decade Overview of Business Indicators', fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.set_xticklabels(years)

ax1.grid(visible=True, which='major', linestyle='--', linewidth=0.7, color='grey')

ax1.legend(loc='lower left', fontsize=12)

ax2 = ax1.twinx()
ax2.plot(years, profits, color='seagreen', marker='x', linestyle='--', linewidth=2, label='Earnings (Billion $)')
ax2.set_ylabel('Net Income (B$)', fontsize=14, color='seagreen')
for i, profit in enumerate(profits):
    ax2.text(years[i], profit + 0.2, f'{profit:.1f}', color='seagreen', ha='center')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, market_shares, color='darkorange', marker='v', linestyle='-', linewidth=2, label='Market Dominance (%)')
ax3.set_ylabel('Dominance (%)', fontsize=14, color='darkorange')
for i, share in enumerate(market_shares):
    ax3.text(years[i], share + 0.5, f'{share}%', color='darkorange', ha='center')
ax3.spines['right'].set_visible(True)

fig.legend(loc='lower right', bbox_to_anchor=(0.9, -0.04), ncol=3, fontsize=12)

plt.tight_layout()
plt.show()