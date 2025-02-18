import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
flavors = ['Vanilla', 'Choco', 'Straw', 'Mint', 'Butter'] 
region1_sales = np.array([
    [60, 70, 80, 90, 40, 55],
    [50, 60, 65, 70, 80, 90],
    [30, 40, 45, 50, 55, 65],
    [40, 45, 55, 60, 70, 80],
    [20, 30, 35, 45, 50, 60]
])
region2_sales = np.array([
    [65, 75, 85, 95, 45, 60],
    [55, 65, 70, 75, 85, 95],
    [35, 45, 50, 55, 60, 70],
    [45, 50, 60, 65, 75, 85],
    [25, 35, 40, 50, 55, 65]
])

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Plot for Region 2-first
axes[0].barh(years - 0.2, region2_sales[0], height=0.1, label='Vanilla', color='#DAA520')
axes[0].barh(years - 0.1, region2_sales[1], height=0.1, label='Choco', color='#FFD700')
axes[0].barh(years, region2_sales[2], height=0.1, label='Straw', color='#8B4513')
axes[0].barh(years + 0.1, region2_sales[3], height=0.1, label='Mint', color='#FF69B4')
axes[0].barh(years + 0.2, region2_sales[4], height=0.1, label='Butter', color='#98FB98')

axes[0].set_title("Region 2 Sales", fontsize=13, fontweight='bold', pad=20)
axes[0].set_ylabel("Year", fontsize=12)
axes[0].set_xlabel("Sales (k)", fontsize=12)
axes[0].legend(loc='upper right')
axes[0].set_yticks(years)
axes[0].grid(True, linestyle='--', alpha=0.6)

# Plot for Region 1 second
axes[1].barh(years - 0.2, region1_sales[0], height=0.1, label='Vanilla', color='#DAA520')
axes[1].barh(years - 0.1, region1_sales[1], height=0.1, label='Choco', color='#FFD700')
axes[1].barh(years, region1_sales[2], height=0.1, label='Straw', color='#8B4513')
axes[1].barh(years + 0.1, region1_sales[3], height=0.1, label='Mint', color='#FF69B4')
axes[1].barh(years + 0.2, region1_sales[4], height=0.1, label='Butter', color='#98FB98')

axes[1].set_title("Region 1 Sales", fontsize=13, fontweight='bold', pad=20)
axes[1].set_ylabel("Year", fontsize=12)
axes[1].set_xlabel("Sales (k)", fontsize=12)
axes[1].legend(loc='upper right')
axes[1].set_yticks(years)
axes[1].grid(True, linestyle='--', alpha=0.6)

fig.suptitle("Ice Cream Sales (2015-2020)", fontsize=16, fontweight='bold', y=1.05)

plt.tight_layout()
plt.show()