import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Ice Cream Sales Performance Over Years in Different Regions
# Dataset represents ice cream sales (in thousands of units) of 5 different flavors over the years in two different regions.

# Construct contextual data inputs
years = np.arange(2015, 2021)
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Butterscotch']
region1_sales = np.array([
    [50, 60, 65, 70, 80, 90],  # Vanilla
    [40, 55, 60, 65, 70, 80],  # Chocolate
    [30, 40, 45, 50, 55, 65],  # Strawberry
    [20, 30, 35, 45, 50, 60],  # Mint
    [40, 45, 55, 60, 70, 80]   # Butterscotch
])
region2_sales = np.array([
    [55, 65, 70, 75, 85, 95],  # Vanilla
    [45, 60, 65, 70, 75, 85],  # Chocolate
    [35, 45, 50, 55, 60, 70],  # Strawberry
    [25, 35, 40, 50, 55, 65],  # Mint
    [45, 50, 60, 65, 75, 85]   # Butterscotch
])

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# First bar chart for Region 1
axes[0].bar(years - 0.2, region1_sales[0], width=0.1, label='Vanilla', color='#FFD700')
axes[0].bar(years - 0.1, region1_sales[1], width=0.1, label='Chocolate', color='#8B4513')
axes[0].bar(years, region1_sales[2], width=0.1, label='Strawberry', color='#FF69B4')
axes[0].bar(years + 0.1, region1_sales[3], width=0.1, label='Mint', color='#98FB98')
axes[0].bar(years + 0.2, region1_sales[4], width=0.1, label='Butterscotch', color='#DAA520')

# Customize the first subplot
axes[0].set_title("Ice Cream Sales in Region 1 (2015-2020)", fontsize=13, fontweight='bold', pad=20)
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Sales (in thousands)", fontsize=12)
axes[0].legend(loc='upper left')
axes[0].set_xticks(years)
axes[0].grid(True, linestyle='--', alpha=0.6)

# Second bar chart for Region 2
axes[1].bar(years - 0.2, region2_sales[0], width=0.1, label='Vanilla', color='#FFD700')
axes[1].bar(years - 0.1, region2_sales[1], width=0.1, label='Chocolate', color='#8B4513')
axes[1].bar(years, region2_sales[2], width=0.1, label='Strawberry', color='#FF69B4')
axes[1].bar(years + 0.1, region2_sales[3], width=0.1, label='Mint', color='#98FB98')
axes[1].bar(years + 0.2, region2_sales[4], width=0.1, label='Butterscotch', color='#DAA520')

# Customize the second subplot
axes[1].set_title("Ice Cream Sales in Region 2 (2015-2020)", fontsize=13, fontweight='bold', pad=20)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Sales (in thousands)", fontsize=12)
axes[1].legend(loc='upper left')
axes[1].set_xticks(years)
axes[1].grid(True, linestyle='--', alpha=0.6)

# Add global title to the entire figure
fig.suptitle("Comparative Ice Cream Sales Performance Over 6 Years", fontsize=16, fontweight='bold', y=1.05)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()