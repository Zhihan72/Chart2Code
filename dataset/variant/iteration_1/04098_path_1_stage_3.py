import matplotlib.pyplot as plt
import numpy as np

markets = ["Europe", "North America", "Asia", "Latin America"]
user_growth = [15, 20, 25, 10]
customer_satisfaction = [80, 85, 88, 75]
revenue = [300, 450, 500, 200]
market_penetration = [30, 40, 50, 35]

fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.set_title("InnovateX Software Performance Across Key Markets - 2023", fontsize=16, fontweight='bold')
ax1.set_ylabel("Markets", fontsize=12)

bar_width = 0.15
bar_l = np.arange(len(markets))

# Changed to horizontal bars
bars1 = ax1.barh(bar_l - 1.5 * bar_width, user_growth, height=bar_width, color='coral', label='User Growth (%)')
bars2 = ax1.barh(bar_l - 0.5 * bar_width, customer_satisfaction, height=bar_width, color='orange', label='Customer Satisfaction (%)')
bars4 = ax1.barh(bar_l + 0.5 * bar_width, market_penetration, height=bar_width, color='lightgreen', label='Market Penetration (%)')

ax2 = ax1.twiny()
bars3 = ax2.barh(bar_l + 1.5 * bar_width, revenue, height=bar_width, color='skyblue', label='Revenue ($M)')

ax1.set_yticks(bar_l)
ax1.set_yticklabels(markets)

ax1.set_xlabel("Performance Metrics (%)", fontsize=12)
ax2.set_xlabel("Revenue (in $ millions)", fontsize=12)

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='lower right', fontsize=12)

for bar in bars1:
    xval = bar.get_width()
    ax1.text(xval + 1, bar.get_y() + bar.get_height() / 2.0, f'{xval}%', va='center', color='black')

for bar in bars2:
    xval = bar.get_width()
    ax1.text(xval + 1, bar.get_y() + bar.get_height() / 2.0, f'{xval}%', va='center', color='black')

for bar in bars3:
    xval = bar.get_width()
    ax2.text(xval + 10, bar.get_y() + bar.get_height() / 2.0, f'${xval}M', va='center', color='black')

for bar in bars4:
    xval = bar.get_width()
    ax1.text(xval + 1, bar.get_y() + bar.get_height() / 2.0, f'{xval}%', va='center', color='black')

plt.tight_layout()
plt.show()