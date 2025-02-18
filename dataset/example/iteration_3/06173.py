import matplotlib.pyplot as plt
import numpy as np

# Company Performance Metrics over a Decade
years = np.arange(2012, 2022)
revenues = [5, 6, 7, 8, 9, 10, 11, 12, 14, 16]  # in billion dollars
expenses = [3, 3.5, 3.5, 4, 4, 4.5, 5, 5.5, 6, 6.5]  # in billion dollars
profits = np.array(revenues) - np.array(expenses)  # derived data
market_shares = [16, 18, 20, 22, 23, 25, 26, 27, 29, 31]  # in percentage

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar plot for Revenues and Expenses
bar_width = 0.4
ax1.bar(years - bar_width/2, revenues, width=bar_width, color='dodgerblue', label='Revenue ($ billion)')
ax1.bar(years + bar_width/2, expenses, width=bar_width, color='tomato', label='Expense ($ billion)')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Revenue and Expense (in billion $)', fontsize=14, color='black')
ax1.set_title('Company Performance Metrics over a Decade', fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(years)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', fontsize=12)

# Second y-axis for Profit
ax2 = ax1.twinx()
ax2.plot(years, profits, color='forestgreen', marker='o', linestyle='-', linewidth=2, label='Profit ($ billion)')
ax2.set_ylabel('Profit (in billion $)', fontsize=14, color='forestgreen')
for i, profit in enumerate(profits):
    ax2.text(years[i], profit + 0.2, f'{profit:.1f}', color='forestgreen', ha='center')

# Third y-axis for Market Share
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, market_shares, color='purple', marker='d', linestyle='-', linewidth=2, label='Market Share (%)')
ax3.set_ylabel('Market Share (%)', fontsize=14, color='purple')
for i, share in enumerate(market_shares):
    ax3.text(years[i], share + 0.5, f'{share}%', color='purple', ha='center')

# Right-spine for ax3 to distinguish from ax1 and ax2
ax3.spines['right'].set_visible(True)

# Legends for ax2 and ax3
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3, fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()