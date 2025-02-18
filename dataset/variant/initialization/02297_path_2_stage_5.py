import matplotlib.pyplot as plt
import numpy as np

sales_contributions_instore = [400, 250, 200, 150, 100, 50, -50, -100, -200, -50]
sales_contributions_online = [350, 250, 200, 150, 100, 80, 60, -30, -80, -150]
labels = ["Autumn", "Returns", "Init", "Year End Promos", "Clearance", 
          "New Year", "Spring", "Summer", "Winter", "Discounts"]

cumulative_sales_instore = np.cumsum(np.insert(sales_contributions_instore, 0, 0))
cumulative_sales_online = np.cumsum(np.insert(sales_contributions_online, 0, 0))

colors_instore = plt.cm.cool((np.array(sales_contributions_instore) + 250) / 500)
colors_online = plt.cm.winter((np.array(sales_contributions_online) + 250) / 500)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].bar(labels, sales_contributions_instore, color=colors_instore, edgecolor='darkgreen', hatch='//')

for i, change in enumerate(sales_contributions_instore):
    ax[0].text(i, change / 2, f"${change:+}", ha='center', va='center', color='darkblue', fontsize=10, fontstyle='italic')

ax[0].step(range(len(labels) + 1), cumulative_sales_instore, where='mid', color='darkred', linestyle='-.', linewidth=2.5)

ax[0].set_facecolor('#f2f0e6')
ax[0].set_title("In-Store Sales Contributions", fontsize=14, fontweight='bold', pad=15, style='italic')
ax[0].set_ylabel('Sales ($1k)', fontsize=11)
ax[0].grid(axis='y', linestyle=':', alpha=0.8)

ax[1].bar(labels, sales_contributions_online, color=colors_online, edgecolor='darkblue', hatch='\\')

for i, change in enumerate(sales_contributions_online):
    ax[1].text(i, change / 2, f"${change:+}", ha='center', va='center', color='darkgreen', fontsize=10, fontstyle='italic')

ax[1].step(range(len(labels) + 1), cumulative_sales_online, where='mid', color='gold', linestyle=':', linewidth=2.5)

ax[1].set_facecolor('#eaf2f8')
ax[1].set_title("Online Sales Contributions", fontsize=14, fontweight='bold', pad=15, style='italic')
ax[1].set_ylabel('Sales ($1k)', fontsize=11)
ax[1].set_xlabel('Collections & Adjusts', fontsize=11)
ax[1].grid(axis='y', linestyle=':', alpha=0.8)

plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.tight_layout()

plt.show()