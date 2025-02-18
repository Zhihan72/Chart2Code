import numpy as np
import matplotlib.pyplot as plt

# Timeline - lettuces sold per month
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Lettuce varieties
lettuce_varieties = ['Romaine', 'Butterhead', 'Iceberg', 'Arugula']

# Sales data (in thousands of heads)
sales_data = np.array([
    [10, 12, 14, 15, 18, 20, 22, 23, 21, 19, 15, 11],  # Romaine
    [8, 9, 10, 12, 14, 17, 19, 18, 16, 14, 10, 9],      # Butterhead
    [9, 11, 13, 14, 16, 18, 20, 21, 20, 18, 13, 10],    # Iceberg
    [5, 6, 8, 10, 12, 14, 16, 17, 15, 12, 8, 6]         # Arugula
])

# Colors for lettuce varieties
colors = ['#4CAF50', '#8BC34A', '#FFEB3B', '#FFC107']

# Set up the figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 10), constrained_layout=True)

# 1st subplot: Monthly Lettuce Sales
for idx, variety in enumerate(lettuce_varieties):
    axs[0].bar(months, sales_data[idx], color=colors[idx], alpha=0.7, label=variety)

axs[0].set_title('Monthly Lettuce Sales in 2023', fontsize=16, weight='bold')
axs[0].set_xlabel('Month', fontsize=12)
axs[0].set_ylabel('Sales (Thousands of Heads)', fontsize=12)
axs[0].legend(title='Lettuce Variety', loc='upper right')

# Enable grid
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5)

# 2nd subplot: Stacked Bar Chart Showing the Portion of Each Variety Sold Each Month
cumulative_sales_data = np.cumsum(sales_data, axis=0)

bottom = np.zeros(len(months))
for idx, (variety, color) in enumerate(zip(lettuce_varieties, colors)):
    axs[1].bar(months, sales_data[idx], bottom=bottom, color=color, alpha=0.7, label=variety)
    bottom += sales_data[idx]

axs[1].set_title('Portion of Lettuce Varieties Sold Each Month in 2023', fontsize=16, weight='bold')
axs[1].set_xlabel('Month', fontsize=12)
axs[1].set_ylabel('Sales (Thousands of Heads)', fontsize=12)
axs[1].legend(title='Lettuce Variety', loc='upper right')

# Enable grid
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5)

# Automatically adjust the layout for optimal spacing
plt.tight_layout()

# Show the plot
plt.show()