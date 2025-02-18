import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
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
region3_sales = np.array([
    [60, 70, 75, 80, 90, 100],
    [50, 65, 70, 75, 80, 90],
    [40, 50, 55, 60, 65, 75],
    [30, 40, 45, 55, 60, 70],
    [50, 55, 65, 70, 80, 90]
])

colors_region1 = ['#98FB98', '#FF69B4', '#8B4513', '#DAA520', '#FFD700']
colors_region2 = ['#DAA520', '#FFD700', '#8B4513', '#FF69B4', '#98FB98']
colors_region3 = ['#FF6347', '#40E0D0', '#EE82EE', '#4169E1', '#800080']

fig, axes = plt.subplots(1, 3, figsize=(20, 7))

axes[0].bar(years - 0.2, region1_sales[0], width=0.1, color=colors_region1[0])
axes[0].bar(years - 0.1, region1_sales[1], width=0.1, color=colors_region1[1])
axes[0].bar(years, region1_sales[2], width=0.1, color=colors_region1[2])
axes[0].bar(years + 0.1, region1_sales[3], width=0.1, color=colors_region1[3])
axes[0].bar(years + 0.2, region1_sales[4], width=0.1, color=colors_region1[4])
axes[0].set_title("Ice Cream Sales in Region 1 (2015-2020)", fontsize=13, fontweight='bold', pad=20)
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Sales (in thousands)", fontsize=12)
axes[0].set_xticks(years)

axes[1].bar(years - 0.2, region2_sales[0], width=0.1, color=colors_region2[0])
axes[1].bar(years - 0.1, region2_sales[1], width=0.1, color=colors_region2[1])
axes[1].bar(years, region2_sales[2], width=0.1, color=colors_region2[2])
axes[1].bar(years + 0.1, region2_sales[3], width=0.1, color=colors_region2[3])
axes[1].bar(years + 0.2, region2_sales[4], width=0.1, color=colors_region2[4])
axes[1].set_title("Ice Cream Sales in Region 2 (2015-2020)", fontsize=13, fontweight='bold', pad=20)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Sales (in thousands)", fontsize=12)
axes[1].set_xticks(years)

axes[2].bar(years - 0.2, region3_sales[0], width=0.1, color=colors_region3[0])
axes[2].bar(years - 0.1, region3_sales[1], width=0.1, color=colors_region3[1])
axes[2].bar(years, region3_sales[2], width=0.1, color=colors_region3[2])
axes[2].bar(years + 0.1, region3_sales[3], width=0.1, color=colors_region3[3])
axes[2].bar(years + 0.2, region3_sales[4], width=0.1, color=colors_region3[4])
axes[2].set_title("Ice Cream Sales in Region 3 (2015-2020)", fontsize=13, fontweight='bold', pad=20)
axes[2].set_xlabel("Year", fontsize=12)
axes[2].set_ylabel("Sales (in thousands)", fontsize=12)
axes[2].set_xticks(years)

fig.suptitle("Comparative Ice Cream Sales Performance Over 6 Years", fontsize=16, fontweight='bold', y=1.05)

plt.tight_layout()
plt.show()