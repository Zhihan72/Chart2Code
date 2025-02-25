import matplotlib.pyplot as plt
import numpy as np

# Define regions and sales data
regions = ['North', 'South', 'East', 'West']
fruit_juice_sales = [1200, 1500, 1400, 1300]
soda_sales = [1800, 1600, 1700, 1500]

# Sort sales data in descending order along with corresponding regions
sorted_data = sorted(zip(fruit_juice_sales, soda_sales, regions), reverse=True)
fruit_juice_sales, soda_sales, regions = zip(*sorted_data)

# Position of bars on x-axis
x = np.arange(len(regions))

# Width of a bar
width = 0.35

# Create a single subplot
fig, ax1 = plt.subplots(figsize=(9, 8))

# Bar chart for sales performance
ax1.bar(x - width/2, fruit_juice_sales, width, color='#ff9999')
ax1.bar(x + width/2, soda_sales, width, color='#66b3ff')

# Customization
ax1.set_xticks(x)
ax1.set_xticklabels([])  # Remove x-axis labels
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.legend().set_visible(False)  # Remove legend

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()