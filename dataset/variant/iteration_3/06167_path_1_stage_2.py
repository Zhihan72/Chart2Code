import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Butterscotch']
region1_sales = np.array([
    [50, 60, 65, 70, 80, 90],
    [40, 55, 60, 65, 70, 80],
    [30, 40, 45, 50, 55, 65],
    [20, 30, 35, 45, 50, 60],
    [40, 45, 55, 60, 70, 80]
])
region2_sales = np.array([
    [55, 65, 70, 75, 85, 95],
    [45, 60, 65, 70, 75, 85],
    [35, 45, 50, 55, 60, 70],
    [25, 35, 40, 50, 55, 65],
    [45, 50, 60, 65, 75, 85]
])

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Plot for Region 2-first
axes[0].bar(years - 0.2, region2_sales[0], width=0.1, label='Vanilla', color='#DAA520')
axes[0].bar(years - 0.1, region2_sales[1], width=0.1, label='Chocolate', color='#FFD700')
axes[0].bar(years, region2_sales[2], width=0.1, label='Strawberry', color='#8B4513')
axes[0].bar(years + 0.1, region2_sales[3], width=0.1, label='Mint', color='#FF69B4')
axes[0].bar(years + 0.2, region2_sales[4], width=0.1, label='Butterscotch', color='#98FB98')

axes[0].set_title("Ice Cream Sales in Region 2 (2015-2020)", fontsize=13, fontweight='bold', pad=20)
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Sales (in thousands)", fontsize=12)
axes[0].legend(loc='upper left')
axes[0].set_xticks(years)
axes[0].grid(True, linestyle='--', alpha=0.6)

# Plot for Region 1 second
axes[1].bar(years - 0.2, region1_sales[0], width=0.1, label='Vanilla', color='#DAA520')
axes[1].bar(years - 0.1, region1_sales[1], width=0.1, label='Chocolate', color='#FFD700')
axes[1].bar(years, region1_sales[2], width=0.1, label='Strawberry', color='#8B4513')
axes[1].bar(years + 0.1, region1_sales[3], width=0.1, label='Mint', color='#FF69B4')
axes[1].bar(years + 0.2, region1_sales[4], width=0.1, label='Butterscotch', color='#98FB98')

axes[1].set_title("Ice Cream Sales in Region 1 (2015-2020)", fontsize=13, fontweight='bold', pad=20)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Sales (in thousands)", fontsize=12)
axes[1].legend(loc='upper left')
axes[1].set_xticks(years)
axes[1].grid(True, linestyle='--', alpha=0.6)

fig.suptitle("Comparative Ice Cream Sales Performance Over 6 Years", fontsize=16, fontweight='bold', y=1.05)

plt.tight_layout()
plt.show()