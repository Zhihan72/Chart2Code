import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
ads_seen = np.array([2, 5, 8, 12, 15, 16, 17, 18, 15, 10, 8])
products_purchased = np.array([1, 2, 4, 7, 8, 7, 6, 5, 4, 3, 2])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Use a single consistent color for the scatter plot
scatter = ax1.scatter(
    ads_seen, 
    products_purchased, 
    color='blue',
    s=150, 
    edgecolor='gray', 
    alpha=0.7
)

ax1.set_title('Ads Effect on Age Groups\' Purchases', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Ads Seen Count', fontsize=12)
ax1.set_ylabel('Products Bought Count', fontsize=12)
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Use the same color 'blue' for additional plots
ax2 = fig.add_axes([0.65, 0.15, 0.25, 0.25])
ax2.scatter(age_groups, ads_seen, color='blue', edgecolor='black', alpha=0.6)
ax2.set_title('Ads vs. Age', fontsize=10)
ax2.set_xlabel('Age (Years)', fontsize=8)
ax2.set_ylabel('Ads Count', fontsize=8)
ax2.grid(visible=True, linestyle='--', alpha=0.3)

ax3 = fig.add_axes([0.15, 0.55, 0.25, 0.25])
ax3.scatter(age_groups, products_purchased, color='blue', edgecolor='black', alpha=0.6)
ax3.set_title('Purchases by Age', fontsize=10)
ax3.set_xlabel('Age (Years)', fontsize=8)
ax3.set_ylabel('Bought Items', fontsize=8)
ax3.grid(visible=True, linestyle='--', alpha=0.3)

plt.tight_layout()

plt.show()