import matplotlib.pyplot as plt
import numpy as np

markets = ["Asia", "North America", "Europe", "Latin America"]
user_growth = [10, 25, 15, 20]
customer_satisfaction = [80, 88, 75, 85]
revenue = [450, 200, 500, 300]

fig, ax1 = plt.subplots(figsize=(12, 8))

bar_width = 0.2
bar_l = np.arange(len(markets))

ax1.bar(bar_l - bar_width, user_growth, width=bar_width, color='#1f77b4')
ax1.bar(bar_l, customer_satisfaction, width=bar_width, color='#ff7f0e')

ax2 = ax1.twinx()
ax2.bar(bar_l + bar_width, revenue, width=bar_width, color='#2ca02c')

ax1.set_xticks(bar_l)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()