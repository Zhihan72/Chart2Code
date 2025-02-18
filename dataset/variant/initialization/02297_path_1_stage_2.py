import matplotlib.pyplot as plt
import numpy as np

sales_contributions_instore = [150, 200, -50, 300, -100, 250, 400, -200, 100, 50]
sales_contributions_online = [100, 150, -30, 250, -80, 200, 350, -150, 80, 60]
labels = ["Init", "Spring", "Returns", "Summer", "Discounts", 
          "Autumn", "Winter", "EoY Promo", "NY Sale", "Clearance"]

sorted_indices_instore = np.argsort(sales_contributions_instore)
sorted_indices_online = np.argsort(sales_contributions_online)

sales_contributions_instore_sorted = np.array(sales_contributions_instore)[sorted_indices_instore]
labels_instore_sorted = np.array(labels)[sorted_indices_instore]

sales_contributions_online_sorted = np.array(sales_contributions_online)[sorted_indices_online]
labels_online_sorted = np.array(labels)[sorted_indices_online]

colors_instore = plt.cm.RdYlGn((np.array(sales_contributions_instore_sorted) + 250) / 500)
colors_online = plt.cm.PuBuGn((np.array(sales_contributions_online_sorted) + 250) / 500)

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

ax[0].bar(labels_instore_sorted, sales_contributions_instore_sorted, color=colors_instore, edgecolor='grey')
ax[0].set_title("In-Store Sales", fontsize=14, fontweight='bold', pad=15)
ax[0].set_ylabel('Contribution ($k)', fontsize=10)
ax[0].grid(axis='y', linestyle='--', alpha=0.6)

ax[1].bar(labels_online_sorted, sales_contributions_online_sorted, color=colors_online, edgecolor='grey')
ax[1].set_title("Online Sales", fontsize=14, fontweight='bold', pad=15)
ax[1].set_ylabel('Contribution ($k)', fontsize=10)
ax[1].set_xlabel('Collections/Adjustments', fontsize=10)
ax[1].grid(axis='y', linestyle='--', alpha=0.6)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()