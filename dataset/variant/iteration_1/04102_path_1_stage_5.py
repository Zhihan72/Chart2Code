import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
ads_seen = np.array([2, 5, 8, 12, 15, 16, 17, 18, 15, 10, 8])
products_purchased = np.array([1, 2, 4, 7, 8, 7, 6, 5, 4, 3, 2])
articles_read = np.array([3, 3, 4, 5, 6, 4, 3, 2, 2, 1, 1])

fig, ax = plt.subplots(figsize=(12, 8))

# Creating a stacked bar chart with altered style elements
ax.bar(age_groups, ads_seen, label='Ads Seen', color='skyblue', edgecolor='darkblue')
ax.bar(age_groups, products_purchased, bottom=ads_seen, label='Products Purchased', color='lightgreen', edgecolor='darkgreen', hatch='/')
ax.bar(age_groups, articles_read, bottom=ads_seen + products_purchased, label='Articles Read', color='coral', edgecolor='darkred', hatch='\\')

ax.set_title("Ads' Influence on Purchasing and Reading", fontsize=14, fontweight='heavy', pad=10)
ax.set_xlabel('Age (Years)', fontsize=11)
ax.set_ylabel('Total Count', fontsize=11)

# Altering legend location and appearance
ax.legend(loc='upper right', fontsize=10, frameon=False)

# Modifying grid style
ax.grid(visible=True, linestyle=':', alpha=0.7, linewidth=1)

# Removing borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()