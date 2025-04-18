import matplotlib.pyplot as plt
import numpy as np

# Original sales contributions
sales_contributions_instore = [150, 200, -50, 300, -100, 250, 400, -200, 100, 50]
sales_contributions_online = [100, 150, -30, 250, -80, 200, 350, -150, 80, 60]

# New "Wholesale" sales contributions
sales_contributions_wholesale = [120, 180, -60, 270, -90, 220, 380, -180, 110, 70]

labels = ["Init", "Spring", "Returns", "Summer", "Discounts", 
          "Autumn", "Winter", "EoY Promo", "NY Sale", "Clearance"]

# Sort indices for each sales category
sorted_indices_instore = np.argsort(sales_contributions_instore)
sorted_indices_online = np.argsort(sales_contributions_online)
sorted_indices_wholesale = np.argsort(sales_contributions_wholesale)

# Sort data by the determined indices
sales_contributions_instore_sorted = np.array(sales_contributions_instore)[sorted_indices_instore]
sales_contributions_online_sorted = np.array(sales_contributions_online)[sorted_indices_online]
sales_contributions_wholesale_sorted = np.array(sales_contributions_wholesale)[sorted_indices_wholesale]

labels_instore_sorted = np.array(labels)[sorted_indices_instore]
labels_online_sorted = np.array(labels)[sorted_indices_online]
labels_wholesale_sorted = np.array(labels)[sorted_indices_wholesale]

# Create subplots for each sales category
fig, ax = plt.subplots(3, 1, figsize=(14, 15))

ax[0].bar(labels_instore_sorted, sales_contributions_instore_sorted, color='skyblue', edgecolor='grey')
ax[0].set_title("In-Store Sales", fontsize=14, fontweight='bold', pad=15)
ax[0].set_ylabel('Contribution ($k)', fontsize=10)
ax[0].grid(axis='y', linestyle='--', alpha=0.6)

ax[1].bar(labels_online_sorted, sales_contributions_online_sorted, color='lightcoral', edgecolor='grey')
ax[1].set_title("Online Sales", fontsize=14, fontweight='bold', pad=15)
ax[1].set_ylabel('Contribution ($k)', fontsize=10)
ax[1].grid(axis='y', linestyle='--', alpha=0.6)

ax[2].bar(labels_wholesale_sorted, sales_contributions_wholesale_sorted, color='mediumseagreen', edgecolor='grey')
ax[2].set_title("Wholesale Sales", fontsize=14, fontweight='bold', pad=15)
ax[2].set_ylabel('Contribution ($k)', fontsize=10)
ax[2].set_xlabel('Collections/Adjustments', fontsize=10)
ax[2].grid(axis='y', linestyle='--', alpha=0.6)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()