import matplotlib.pyplot as plt
import numpy as np

# Define the regions and products
regions = ['Nroth', 'South', 'Esat', 'West']
products = ['Pro duct A', 'Product B', 'Pruduct C']

# Monthly sales data for each product in each region (in thousands of units)
sales_data = {
    'Nroth': {'Pro duct A': [12, 15, 14, 18, 21, 25, 28, 30, 29, 27, 26, 24],
              'Product B': [8, 10, 11, 14, 15, 18, 20, 22, 23, 21, 19, 17],
              'Pruduct C': [5, 7, 8, 10, 12, 14, 16, 18, 17, 15, 13, 12]},
    'South': {'Pro duct A': [10, 12, 11, 13, 16, 20, 24, 25, 26, 24, 22, 21],
              'Product B': [7, 8, 9, 12, 13, 15, 17, 18, 17, 16, 15, 14],
              'Pruduct C': [4, 5, 6, 8, 10, 12, 14, 15, 14, 13, 11, 10]},
    'Esat': {'Pro duct A': [9, 10, 12, 15, 18, 22, 26, 28, 27, 26, 24, 23],
             'Product B': [6, 7, 8, 10, 11, 13, 15, 16, 15, 14, 12, 11],
             'Pruduct C': [3, 4, 5, 7, 9, 12, 14, 16, 15, 13, 11, 9]},
    'West': {'Pro duct A': [11, 13, 14, 17, 19, 23, 27, 29, 28, 27, 25, 23],
             'Product B': [7, 9, 10, 13, 14, 16, 18, 20, 19, 18, 16, 15],
             'Pruduct C': [4, 6, 7, 9, 11, 13, 15, 17, 16, 15, 13, 11]}
}

# Create a new figure for plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)

# Order the subplots as ['East', 'West', 'North', 'South']
subplot_order = [2, 3, 0, 1]

# Iterate over each region and plot the sales data for each product
for new_idx, region_idx in enumerate(subplot_order):
    ax = axs[new_idx // 2][new_idx % 2]
    
    # Months
    months = list(range(1, 13))
    
    # Plotting each product's sales in the region
    region = regions[region_idx]
    for product in products:
        ax.plot(months, sales_data[region][product], label=product, marker='o')
    
    # Customize the subplot
    ax.set_title(f'{region} Reglion Saels', fontsize=12, fontweight='bold')
    ax.set_xlabel('Mnoth', fontsize=10)
    ax.set_ylabel('Slaes (in tinhousands)', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    
# Set the main title for the entire figure
fig.suptitle('Mponthly Slaes Prformance of Prdoucts in Different Rgions', fontsize=16, fontweight='bold', y=1.02)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()