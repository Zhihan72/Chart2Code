import matplotlib.pyplot as plt
import numpy as np

# Backstory: "The Impact of Advertisements on Different Age Groups' Product Purchases"
# The chart examines how different age groups responded to a series of advertisement campaigns over a year.

# Data: Age groups (in years), Number of Ads Seen, Number of Products Purchased
age_groups = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
ads_seen = np.array([2, 5, 8, 12, 15, 16, 17, 18, 15, 10, 8])
products_purchased = np.array([1, 2, 4, 7, 8, 7, 6, 5, 4, 3, 2])

# Create figure and main scatter plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Main scatter plot
scatter = ax1.scatter(
    ads_seen, 
    products_purchased, 
    c=age_groups,
    cmap='plasma', 
    s=150, 
    edgecolor='gray', 
    alpha=0.7
)

# Add color bar for age groups
cbar = plt.colorbar(scatter)
cbar.set_label('Age Group (Years)', fontsize=12)

# Customize axes and labels
ax1.set_title('Impact of Advertisements on Different Age Groups\' Product Purchases', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Number of Ads Seen', fontsize=12)
ax1.set_ylabel('Number of Products Purchased', fontsize=12)
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Subplot: Age Group vs. Number of Ads Seen
ax2 = fig.add_axes([0.65, 0.15, 0.25, 0.25])
ax2.scatter(age_groups, ads_seen, color='green', edgecolor='black', alpha=0.6)
ax2.set_title('Ads Seen by Age Group', fontsize=10)
ax2.set_xlabel('Age Group (Years)', fontsize=8)
ax2.set_ylabel('Ads Seen', fontsize=8)
ax2.grid(visible=True, linestyle='--', alpha=0.3)

# Subplot: Age Group vs. Number of Products Purchased
ax3 = fig.add_axes([0.15, 0.55, 0.25, 0.25])
ax3.scatter(age_groups, products_purchased, color='red', edgecolor='black', alpha=0.6)
ax3.set_title('Purchases by Age Group', fontsize=10)
ax3.set_xlabel('Age Group (Years)', fontsize=8)
ax3.set_ylabel('Products Purchased', fontsize=8)
ax3.grid(visible=True, linestyle='--', alpha=0.3)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()