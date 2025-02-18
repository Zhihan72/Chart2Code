import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
brands = ["CrunchyBites", "FruitMunch", "ChocoDelight", "NuttyCrave"]

sales_north = np.array([
    [150, 170, 180, 200, 210], 
    [120, 140, 160, 170, 180], 
    [130, 160, 190, 210, 220], 
    [90, 100, 120, 130, 140]    
])

sales_east = np.array([
    [160, 180, 190, 210, 230], 
    [130, 150, 170, 180, 190], 
    [150, 180, 200, 220, 240], 
    [100, 110, 130, 140, 160]   
])

sales_west = np.array([
    [140, 160, 170, 190, 200], 
    [110, 130, 150, 160, 170], 
    [120, 150, 180, 200, 210], 
    [80, 90, 110, 120, 130]     
])

def sort_sales(sales):
    total_sales = sales.sum(axis=1)
    sorted_indices = np.argsort(-total_sales)
    return sales[sorted_indices], [brands[i] for i in sorted_indices]

sales_north_sorted, brands_north_sorted = sort_sales(sales_north)
sales_east_sorted, brands_east_sorted = sort_sales(sales_east)
sales_west_sorted, brands_west_sorted = sort_sales(sales_west)

fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Switching the order of regions: previously "North", "East", "West"
for ax, region, sales, region_brands in zip(
    axes, 
    ["East", "West", "North"],  # Changed the order deliberately
    [sales_east_sorted, sales_west_sorted, sales_north_sorted], 
    [brands_east_sorted, brands_west_sorted, brands_north_sorted]
):
    bar_width = 0.2
    index = np.arange(len(years))
    
    for i, (brand, color) in enumerate(zip(region_brands, colors)):
        ax.bar(index + (i * bar_width), sales[i], bar_width, label=brand, color=color)
    
    ax.set_title(f'Sales in {region} Region', fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_xticks(index + bar_width * 1.5)
    ax.set_xticklabels(years, rotation=45)
    ax.legend(title='Snack Brands')

axes[0].set_ylabel('Sales (in \'000 units)', fontsize=12)
fig.suptitle('Annual Sales Performance of Snack Brands (2018-2022)', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()