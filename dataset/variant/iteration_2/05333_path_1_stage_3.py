import matplotlib.pyplot as plt
import numpy as np

campaigns = ['Social Media', 'TV Ads', 'Email Marketing', 'Billboards', 'Trade Shows']

Q1_sales = np.array([12000, 25000, 15000, 18000, 20000])
Q2_sales = np.array([13000, 26000, 16000, 21000, 19000])
Q3_sales = np.array([22000, 17000, 14000, 27000, 20000])
Q4_sales = np.array([23000, 28000, 21000, 15000, 18000])

colors_campaigns = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
positions = np.arange(len(campaigns))

ax.bar(positions - 1.5*bar_width, Q1_sales, width=bar_width, color=colors_campaigns, edgecolor='black')
ax.bar(positions - 0.5*bar_width, Q2_sales, width=bar_width, color=colors_campaigns, edgecolor='black', alpha=0.9)
ax.bar(positions + 0.5*bar_width, Q3_sales, width=bar_width, color=colors_campaigns, edgecolor='black', alpha=0.8)
ax.bar(positions + 1.5*bar_width, Q4_sales, width=bar_width, color=colors_campaigns, edgecolor='black', alpha=0.7)

total_sales = Q1_sales + Q2_sales + Q3_sales + Q4_sales
ax.plot(positions, total_sales, color='purple', marker='o', linestyle='-', linewidth=2, markersize=8)

plt.tight_layout()
plt.show()