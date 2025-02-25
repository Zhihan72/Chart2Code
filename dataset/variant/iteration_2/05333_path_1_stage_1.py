import matplotlib.pyplot as plt
import numpy as np

campaigns = ['Social Media', 'TV Ads', 'Email Marketing', 'Billboards', 'Trade Shows']

# Manually shuffled sales impacts
Q1_sales = np.array([12000, 25000, 15000, 18000, 20000])
Q2_sales = np.array([13000, 26000, 16000, 21000, 19000])
Q3_sales = np.array([22000, 17000, 14000, 27000, 20000])
Q4_sales = np.array([23000, 28000, 21000, 15000, 18000])

total_sales = Q1_sales + Q2_sales + Q3_sales + Q4_sales

colors_campaigns = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
positions = np.arange(len(campaigns))

bars_Q1 = ax.bar(positions - 1.5*bar_width, Q1_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q1')
bars_Q2 = ax.bar(positions - 0.5*bar_width, Q2_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q2', alpha=0.9)
bars_Q3 = ax.bar(positions + 0.5*bar_width, Q3_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q3', alpha=0.8)
bars_Q4 = ax.bar(positions + 1.5*bar_width, Q4_sales, width=bar_width, color=colors_campaigns, edgecolor='black', label='Q4', alpha=0.7)

total_positions = np.arange(len(campaigns))
ax.plot(total_positions, total_sales, color='purple', marker='o', linestyle='-', linewidth=2, markersize=8, label='Total Sales')

for i, total_val in enumerate(total_sales):
    ax.text(i, total_val + 500, f'${int(total_val)}', ha='center', va='bottom', fontsize=10, color='purple')

ax.set_title("Impact of Different Marketing Campaigns on Product Sales\nAcross Four Quarters", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Marketing Campaigns", fontsize=12)
ax.set_ylabel("Sales in USD", fontsize=12)
ax.set_xticks(positions)
ax.set_xticklabels(campaigns, fontsize=12)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()