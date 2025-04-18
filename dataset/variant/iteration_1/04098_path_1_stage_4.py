import matplotlib.pyplot as plt
import numpy as np

# Group labels altered
markets = ["EU", "NA", "Asia-Pacific", "LatAm"]
user_growth = [15, 20, 25, 10]
customer_satisfaction = [80, 85, 88, 75]
revenue = [300, 450, 500, 200]
market_penetration = [30, 40, 50, 35]

fig, ax1 = plt.subplots(figsize=(12, 8))

# Title altered
ax1.set_title("2023 Global Software Metrics - InnovateX", fontsize=16, fontweight='bold')

# Y-axis label altered
ax1.set_ylabel("Regions", fontsize=12)

bar_width = 0.15
bar_l = np.arange(len(markets))

bars1 = ax1.barh(bar_l - 1.5 * bar_width, user_growth, height=bar_width, color='coral', label='Growth of Users (%)')
bars2 = ax1.barh(bar_l - 0.5 * bar_width, customer_satisfaction, height=bar_width, color='orange', label='Satisfaction of Customers (%)')
bars4 = ax1.barh(bar_l + 0.5 * bar_width, market_penetration, height=bar_width, color='lightgreen', label='Penetration in Market (%)')

ax2 = ax1.twiny()
bars3 = ax2.barh(bar_l + 1.5 * bar_width, revenue, height=bar_width, color='skyblue', label='Earnings ($M)')

# Y-axis ticks altered
ax1.set_yticks(bar_l)
ax1.set_yticklabels(markets)

# X-axis labels altered
ax1.set_xlabel("Metric Performance (%)", fontsize=12)
ax2.set_xlabel("Earnings (in $ millions)", fontsize=12)

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='lower right', fontsize=12)

# Bars text annotations
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