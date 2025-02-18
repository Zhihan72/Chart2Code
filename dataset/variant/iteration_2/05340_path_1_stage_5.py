import matplotlib.pyplot as plt
import numpy as np

# Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
apples_sales = np.array([120, 130, 110, 150, 180, 200, 220, 240, 200, 150, 140, 130])
bananas_sales = np.array([90, 100, 110, 120, 130, 140, 150, 160, 150, 140, 130, 110])
oranges_sales = np.array([80, 90, 100, 110, 120, 130, 140, 150, 140, 130, 120, 100])
berries_sales = np.array([70, 80, 90, 100, 110, 120, 130, 140, 130, 120, 110, 90])
grapes_sales = np.array([60, 80, 100, 110, 90, 110, 130, 120, 100, 90, 100, 110])
mangoes_sales = np.array([50, 70, 90, 110, 130, 150, 170, 180, 160, 140, 120, 100])

# Create the figure and subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot diverging bar chart
baseline = np.zeros(len(months))
ax.bar(months, apples_sales, bottom=baseline, label='Apples', color='red')
baseline += apples_sales

ax.bar(months, -bananas_sales, bottom=-baseline, label='Bananas', color='yellow')
baseline -= bananas_sales

ax.bar(months, oranges_sales, bottom=baseline, label='Oranges', color='orange')
baseline += oranges_sales

ax.bar(months, -berries_sales, bottom=-baseline, label='Berries', color='purple')
baseline -= berries_sales

ax.bar(months, grapes_sales, bottom=baseline, label='Grapes', color='green')
baseline += grapes_sales

ax.bar(months, -mangoes_sales, bottom=-baseline, label='Mangoes', color='magenta')
baseline -= mangoes_sales

# Add labels, grid, and title
ax.set_title('Diverging Monthly Sales Volume of Fruits\n(2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales Volume', fontsize=12)
ax.grid(True, linestyle='-', linewidth=0.5, alpha=0.8)
ax.legend(loc='lower left', fontsize=11)

# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()