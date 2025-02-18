import matplotlib.pyplot as plt
import numpy as np

# Data: Age groups (in years), Number of Ads Seen, Number of Products Purchased
age_groups = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
ads_seen = np.array([2, 5, 8, 12, 15, 16, 17, 18, 15, 10, 8])
products_purchased = np.array([1, 2, 4, 7, 8, 7, 6, 5, 4, 3, 2])

# Create figure and diverging bar plot
fig, ax = plt.subplots(figsize=(12, 8))

# Calculating mid-point for diverging bars
midpoint = np.zeros_like(ads_seen)

# Plotting the divergent bar chart
ax.barh(age_groups, ads_seen, color='blue', label='Ads Seen')
ax.barh(age_groups, -products_purchased, color='orange', label='Products Purchased')

# Customize axes and labels
ax.set_title('Diverging Bar Chart of Advertisement Impact', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Ads Seen / Products Purchased', fontsize=12)
ax.set_ylabel('Age Group (Years)', fontsize=12)
ax.grid(visible=True, linestyle='--', alpha=0.5)
ax.axvline(0, color='black', linewidth=0.8)

# Add legend
ax.legend()

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()