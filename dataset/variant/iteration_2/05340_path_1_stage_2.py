import matplotlib.pyplot as plt
import numpy as np

# Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
apples_sales = np.array([120, 130, 110, 150, 180, 200, 220, 240, 200, 150, 140, 130])
bananas_sales = np.array([90, 100, 110, 120, 130, 140, 150, 160, 150, 140, 130, 110])
oranges_sales = np.array([80, 90, 100, 110, 120, 130, 140, 150, 140, 130, 120, 100])
berries_sales = np.array([70, 80, 90, 100, 110, 120, 130, 140, 130, 120, 110, 90])

# Create the figure and subplot
fig, ax = plt.subplots(figsize=(14, 6))

# Line chart of cumulative monthly sales with altered styles
ax.plot(months, apples_sales + bananas_sales + oranges_sales + berries_sales, label='Total Sales', color='green', marker='x', linestyle='--', linewidth=2, markersize=8)

# Add labels, grid, and title with changed styles
ax.set_title('Cumulative Monthly Sales Volume of All Fruits\n(2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Cumulative Sales Volume', fontsize=12)
ax.grid(True, linestyle='-', linewidth=0.5, alpha=0.8)
ax.legend(loc='lower right', fontsize=11)

# Add values above the cumulative sales line plot
cumulative_sales = apples_sales + bananas_sales + oranges_sales + berries_sales
for i, value in enumerate(cumulative_sales):
    ax.text(i, value + 10, f'{value}', ha='center', va='bottom', fontsize=10, color='green')

# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()