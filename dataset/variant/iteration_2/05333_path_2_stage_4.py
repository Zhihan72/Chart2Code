import matplotlib.pyplot as plt
import numpy as np

campaigns = ['Social Media', 'TV Ads', 'Email Marketing', 'Billboards', 'Trade Shows']

# Original sales data are shuffled within arrays
Q1_sales = np.array([18000, 12000, 25000, 15000, 20000])  # Shuffled
Q2_sales = np.array([26000, 13000, 16000, 21000, 19000])  # Shuffled
Q3_sales = np.array([17000, 22000, 14000, 27000, 20000])  # Shuffled
Q4_sales = np.array([15000, 21000, 23000, 28000, 18000])  # Shuffled

total_sales = Q1_sales + Q2_sales + Q3_sales + Q4_sales
colors_campaigns = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231']

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.2
positions = np.arange(len(campaigns))

ax.barh(positions - 1.5*bar_height, Q1_sales, height=bar_height, color=colors_campaigns, edgecolor='grey', label='Q1', alpha=0.7)
ax.barh(positions - 0.5*bar_height, Q2_sales, height=bar_height, color=colors_campaigns, edgecolor='grey', label='Q2', alpha=0.6)
ax.barh(positions + 0.5*bar_height, Q3_sales, height=bar_height, color=colors_campaigns, edgecolor='grey', label='Q3', alpha=0.5)
ax.barh(positions + 1.5*bar_height, Q4_sales, height=bar_height, color=colors_campaigns, edgecolor='grey', label='Q4', alpha=0.4)

ax.plot(total_sales, positions, color='violet', marker='s', linestyle='--', linewidth=1.5, markersize=7, label='Total Sales')

for i, total_val in enumerate(total_sales):
    ax.text(total_val + 1000, i, f'${int(total_val)}', ha='left', va='center', fontsize=10, color='violet')

ax.set_title("Impact of Marketing Campaigns on Sales\nAcross Quarters", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sales in USD", fontsize=12)
ax.set_ylabel("Marketing Campaigns", fontsize=12)

ax.set_yticks(positions)
ax.set_yticklabels(campaigns, fontsize=12)

ax.xaxis.grid(True, linestyle='-.', alpha=0.6)

ax.legend(frameon=False, loc='best')

plt.tight_layout()
plt.show()