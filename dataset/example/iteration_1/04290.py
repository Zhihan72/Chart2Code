import matplotlib.pyplot as plt
import numpy as np

# Title and Backstory:
# We are visualizing the annual sales performance of four fictional snack brands over five years across three regions.

# Years for the data
years = np.array([2018, 2019, 2020, 2021, 2022])

# Snack Brands
brands = ["CrunchyBites", "FruitMunch", "ChocoDelight", "NuttyCrave"]

# Sales data in three regions: North, East, West
sales_north = np.array([
    [150, 170, 180, 200, 210],  # CrunchyBites
    [120, 140, 160, 170, 180],  # FruitMunch
    [130, 160, 190, 210, 220],  # ChocoDelight
    [90, 100, 120, 130, 140]    # NuttyCrave
])

sales_east = np.array([
    [160, 180, 190, 210, 230],  # CrunchyBites
    [130, 150, 170, 180, 190],  # FruitMunch
    [150, 180, 200, 220, 240],  # ChocoDelight
    [100, 110, 130, 140, 160]   # NuttyCrave
])

sales_west = np.array([
    [140, 160, 170, 190, 200],  # CrunchyBites
    [110, 130, 150, 160, 170],  # FruitMunch
    [120, 150, 180, 200, 210],  # ChocoDelight
    [80, 90, 110, 120, 130]     # NuttyCrave
])

# Plot configuration
fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

# Define colors for each brand
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create bar charts for each region
for ax, region, sales in zip(axes, ["North", "East", "West"], [sales_north, sales_east, sales_west]):
    bar_width = 0.2
    index = np.arange(len(years))
    
    for i, (brand, color) in enumerate(zip(brands, colors)):
        ax.bar(index + (i * bar_width), sales[i], bar_width, label=brand, color=color)
    
    ax.set_title(f'Sales in {region} Region', fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_xticks(index + bar_width * 1.5)
    ax.set_xticklabels(years, rotation=45)
    ax.legend(title='Snack Brands')

# Sharing the Y-axis
axes[0].set_ylabel('Sales (in \'000 units)', fontsize=12)

# Adding main title
fig.suptitle('Annual Sales Performance of Snack Brands (2018-2022)', fontsize=16, fontweight='bold')

# Adjusting layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()