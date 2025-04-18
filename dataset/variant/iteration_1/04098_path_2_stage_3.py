import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart, similar dimension but altered data randomly
markets = ["Asia", "North America", "Europe", "Latin America"]
user_growth = [10, 25, 15, 20]  # altered values
customer_satisfaction = [80, 88, 75, 85]  # altered values
revenue = [450, 200, 500, 300]  # altered values

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.set_title("InnovateX Software Performance Across Key Markets - 2023", fontsize=16, fontweight='bold')
ax1.set_xlabel("Markets", fontsize=12)

bar_width = 0.2
bar_l = np.arange(len(markets))

bars1 = ax1.bar(bar_l - bar_width, user_growth, width=bar_width, color='#1f77b4', label='User Growth (%)')
bars2 = ax1.bar(bar_l, customer_satisfaction, width=bar_width, color='#ff7f0e', label='Customer Satisfaction (%)')

ax2 = ax1.twinx()
bars3 = ax2.bar(bar_l + bar_width, revenue, width=bar_width, color='#2ca02c', label='Revenue ($M)')

ax1.set_xticks(bar_l)
ax1.set_xticklabels(markets)

ax1.set_ylabel("User Growth & Customer Satisfaction (%)", fontsize=12)
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

plt.tight_layout()
plt.show()