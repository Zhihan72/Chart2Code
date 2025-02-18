import matplotlib.pyplot as plt
import numpy as np

sales_contributions_instore = [200, -50, 250, -100, 400, 300, -200, 150, 50, 100]
sales_contributions_online = [-30, 150, -80, 200, 100, 250, -150, 350, 80, 60]
labels = ["Init", "Spring", "Returns", "Summer", "Discounts", 
          "Autumn", "Winter", "Year End Promos", "New Year", "Clearance"]

sorted_indices_instore = np.argsort(sales_contributions_instore)[::-1]
sales_contributions_instore = np.array(sales_contributions_instore)[sorted_indices_instore]
labels_instore = np.array(labels)[sorted_indices_instore]
cumulative_sales_instore = np.cumsum(np.insert(sales_contributions_instore, 0, 0))

sorted_indices_online = np.argsort(sales_contributions_online)[::-1]
sales_contributions_online = np.array(sales_contributions_online)[sorted_indices_online]
labels_online = np.array(labels)[sorted_indices_online]
cumulative_sales_online = np.cumsum(np.insert(sales_contributions_online, 0, 0))

colors_instore = plt.cm.RdYlGn((np.array(sales_contributions_instore) + 250) / 500)
colors_online = plt.cm.PuBuGn((np.array(sales_contributions_online) + 250) / 500)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].bar(labels_instore, sales_contributions_instore, color=colors_instore, edgecolor='grey')

for i, change in enumerate(sales_contributions_instore):
    ax[0].text(i, change / 2, f"{change:+}", ha='center', va='center', color='black', fontsize=9, fontweight='bold')

ax[0].step(range(len(labels_instore) + 1), cumulative_sales_instore, where='mid', color='blue', linestyle='--', linewidth=2)

ax[0].set_title("In-Store Sales Contributions\nSorted Desc", fontsize=14, fontweight='bold', pad=15)
ax[0].set_ylabel('Sales ($1k)', fontsize=10)
ax[0].grid(axis='y', linestyle='--', alpha=0.6)

ax[1].bar(labels_online, sales_contributions_online, color=colors_online, edgecolor='grey')

for i, change in enumerate(sales_contributions_online):
    ax[1].text(i, change / 2, f"{change:+}", ha='center', va='center', color='black', fontsize=9, fontweight='bold')

ax[1].step(range(len(labels_online) + 1), cumulative_sales_online, where='mid', color='purple', linestyle='--', linewidth=2)

ax[1].set_title("Online Sales Contributions\nSorted Desc", fontsize=14, fontweight='bold', pad=15)
ax[1].set_ylabel('Sales ($1k)', fontsize=10)
ax[1].set_xlabel('Collections & Adjusts', fontsize=10)
ax[1].grid(axis='y', linestyle='--', alpha=0.6)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()