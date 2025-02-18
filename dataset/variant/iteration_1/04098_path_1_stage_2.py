import matplotlib.pyplot as plt
import numpy as np

markets = ["Europe", "North America", "Asia", "Latin America"]
user_growth = [15, 20, 25, 10]
customer_satisfaction = [80, 85, 88, 75]
revenue = [300, 450, 500, 200]
market_penetration = [30, 40, 50, 35]

fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.set_title("InnovateX Software Performance Across Key Markets - 2023", fontsize=16, fontweight='bold')
ax1.set_xlabel("Markets", fontsize=12)

bar_width = 0.15
bar_l = np.arange(len(markets))

# Changed the order of colors for each data group/type
bars1 = ax1.bar(bar_l - 1.5 * bar_width, user_growth, width=bar_width, color='coral', label='User Growth (%)')
bars2 = ax1.bar(bar_l - 0.5 * bar_width, customer_satisfaction, width=bar_width, color='orange', label='Customer Satisfaction (%)')
bars4 = ax1.bar(bar_l + 0.5 * bar_width, market_penetration, width=bar_width, color='lightgreen', label='Market Penetration (%)')

ax2 = ax1.twinx()
bars3 = ax2.bar(bar_l + 1.5 * bar_width, revenue, width=bar_width, color='skyblue', label='Revenue ($M)')

ax1.set_xticks(bar_l)
ax1.set_xticklabels(markets)

ax1.set_ylabel("Performance Metrics (%)", fontsize=12)
ax2.set_ylabel("Revenue (in $ millions)", fontsize=12)

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left', fontsize=12)

for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, yval + 1, f'{yval}%', ha='center', color='black')

for bar in bars2:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, yval + 1, f'{yval}%', ha='center', color='black')

for bar in bars3:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2.0, yval + 10, f'${yval}M', ha='center', color='black')

for bar in bars4:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, yval + 1, f'{yval}%', ha='center', color='black')

plt.tight_layout()
plt.show()