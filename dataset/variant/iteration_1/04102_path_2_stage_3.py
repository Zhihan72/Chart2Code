import matplotlib.pyplot as plt
import numpy as np

# Data: Age groups (in years), Number of Ads Seen, Number of Products Purchased
age_groups = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
ads_seen = np.array([5, 2, 9, 11, 14, 15, 19, 17, 13, 9, 7])  # Manually altered values and shuffled 
products_purchased = np.array([2, 1, 5, 6, 9, 6, 7, 4, 5, 3, 3])  # Manually altered values and shuffled

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(age_groups, ads_seen, color='teal', label='Ads Seen')
ax.barh(age_groups, -products_purchased, color='salmon', label='Products Purchased')

ax.set_title('Diverging Bar Chart of Advertisement Impact', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Ads Seen / Products Purchased', fontsize=12)
ax.set_ylabel('Age Group (Years)', fontsize=12)
ax.grid(visible=True, linestyle='--', alpha=0.5)
ax.axvline(0, color='black', linewidth=0.8)

ax.legend()

plt.tight_layout()

plt.show()