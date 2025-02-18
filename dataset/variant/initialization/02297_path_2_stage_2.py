import matplotlib.pyplot as plt
import numpy as np

sales_contributions_instore = [200, -50, 250, -100, 400, 300, -200, 150, 50, 100]
sales_contributions_online = [-30, 150, -80, 200, 100, 250, -150, 350, 80, 60]
labels = ["Initial Sales", "Spring Collection", "Returns", "Summer Collection", "Discounts", 
          "Autumn Collection", "Winter Collection", "End of Year Promotions", "New Year Sale", "Clearance"]

cumulative_sales_instore = np.cumsum(sales_contributions_instore)
cumulative_sales_instore = np.insert(cumulative_sales_instore, 0, 0)

cumulative_sales_online = np.cumsum(sales_contributions_online)
cumulative_sales_online = np.insert(cumulative_sales_online, 0, 0)

step_values_instore = np.zeros_like(cumulative_sales_instore)
step_values_instore[1:] = cumulative_sales_instore[:-1]

step_values_online = np.zeros_like(cumulative_sales_online)
step_values_online[1:] = cumulative_sales_online[:-1]

colors_instore = plt.cm.RdYlGn((np.array(sales_contributions_instore) + 250) / 500)
colors_online = plt.cm.PuBuGn((np.array(sales_contributions_online) + 250) / 500)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].bar(labels, sales_contributions_instore, bottom=step_values_instore[1:], color=colors_instore, edgecolor='grey')

for i, change in enumerate(sales_contributions_instore):
    ax[0].text(i, step_values_instore[i + 1] + change / 2, f"{change:+}", ha='center', va='center', color='black', fontsize=9, fontweight='bold')

ax[0].step(range(len(labels) + 1), cumulative_sales_instore, where='mid', color='blue', linestyle='--', linewidth=2)

ax[0].set_title("In-Store Sales Contributions Across Collections\nwith Variability", fontsize=14, fontweight='bold', pad=15)
ax[0].set_ylabel('Sales Contribution ($1000s)', fontsize=10)
ax[0].grid(axis='y', linestyle='--', alpha=0.6)

ax[1].bar(labels, sales_contributions_online, bottom=step_values_online[1:], color=colors_online, edgecolor='grey')

for i, change in enumerate(sales_contributions_online):
    ax[1].text(i, step_values_online[i + 1] + change / 2, f"{change:+}", ha='center', va='center', color='black', fontsize=9, fontweight='bold')

ax[1].step(range(len(labels) + 1), cumulative_sales_online, where='mid', color='purple', linestyle='--', linewidth=2)

ax[1].set_title("Online Sales Contributions Across Collections\nwith Variability", fontsize=14, fontweight='bold', pad=15)
ax[1].set_ylabel('Sales Contribution ($1000s)', fontsize=10)
ax[1].set_xlabel('Fashion Collections and Adjustments', fontsize=10)
ax[1].grid(axis='y', linestyle='--', alpha=0.6)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()