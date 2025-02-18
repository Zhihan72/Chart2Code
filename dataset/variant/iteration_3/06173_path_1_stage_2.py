import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
revenues = [5, 6, 7, 8, 9, 10, 11, 12, 14, 16]
profits = [2, 2.5, 3.5, 4, 5, 5.5, 6, 6.5, 8, 9.5]
market_shares = [16, 18, 20, 22, 23, 25, 26, 27, 29, 31]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 0.4
ax1.bar(years, revenues, width=bar_width, color='darkorange', label='Revenue ($ billion)')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Revenue (in billion $)', fontsize=14, color='black')
ax1.set_title('Company Performance Metrics over a Decade', fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.set_xticklabels(years)

ax1.grid(visible=True, which='major', linestyle='--', linewidth=0.7, color='grey')

# Move legend to bottom
ax1.legend(loc='lower left', fontsize=12)

ax2 = ax1.twinx()
ax2.plot(years, profits, color='maroon', marker='x', linestyle='--', linewidth=2, label='Profit ($ billion)')
ax2.set_ylabel('Profit (in billion $)', fontsize=14, color='maroon')
for i, profit in enumerate(profits):
    ax2.text(years[i], profit + 0.2, f'{profit:.1f}', color='maroon', ha='center')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, market_shares, color='seagreen', marker='v', linestyle='-', linewidth=2, label='Market Share (%)')
ax3.set_ylabel('Market Share (%)', fontsize=14, color='seagreen')
for i, share in enumerate(market_shares):
    ax3.text(years[i], share + 0.5, f'{share}%', color='seagreen', ha='center')
ax3.spines['right'].set_visible(True)

fig.legend(loc='lower right', bbox_to_anchor=(0.9, -0.04), ncol=3, fontsize=12)

plt.tight_layout()
plt.show()