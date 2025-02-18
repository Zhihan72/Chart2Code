import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
ads_seen = np.array([2, 5, 8, 12, 15, 16, 17, 18, 15, 10, 8])
products_purchased = np.array([1, 2, 4, 7, 8, 7, 6, 5, 4, 3, 2])

fig, ax = plt.subplots(figsize=(12, 8))

# Creating a stacked bar chart
ax.bar(age_groups, ads_seen, label='Ads Seen', color='blue')
ax.bar(age_groups, products_purchased, bottom=ads_seen, label='Products Purchased', color='green')

ax.set_title('Ads Effect on Age Groups\' Purchases', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Age (Years)', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.legend()
ax.grid(visible=True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()