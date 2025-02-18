import matplotlib.pyplot as plt
import numpy as np

# Define regions and data
regions = ['North', 'South', 'East', 'West']
fruit_juice_sales = [1200, 1500, 1400, 1300]
soda_sales = [1800, 1600, 1700, 1500]
percentage_increase = [10, 12, 8, 15]

# Position of bars on x-axis
x = np.arange(len(regions))

# Width of a bar
width = 0.35

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Bar chart for sales performance (first subplot)
ax1.bar(x - width/2, fruit_juice_sales, width, color='#ff9999')
ax1.bar(x + width/2, soda_sales, width, color='#66b3ff')

# Customization
ax1.set_xticks(x)
ax1.set_xticklabels([])  # Remove x-axis labels
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.legend().set_visible(False)  # Remove legend

# Bar chart for percentage increase (second subplot)
ax2.bar(x, percentage_increase, color='#ffcc99')

# Customization
ax2.set_xticks(x)
ax2.set_xticklabels([])  # Remove x-axis labels
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()