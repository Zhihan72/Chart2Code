import matplotlib.pyplot as plt
import numpy as np

# Data preparation
categories = ['Solar Panels', 'Wind Turbines', 'Electric Vehicles', 'Battery Storage', 'Hydrogen Fuel Cells']

solar_panels_sales = [35, 40, 42, 45, 50, 60, 65, 55, 70, 75, 80]
wind_turbines_sales = [20, 25, 28, 30, 35, 40, 42, 38, 45, 50, 52]
electric_vehicles_sales = [15, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70]
battery_storage_sales = [10, 12, 15, 18, 22, 25, 30, 35, 40, 42, 45]
hydrogen_fuel_cells_sales = [5, 6, 7, 9, 10, 12, 14, 16, 20, 22, 25]

sales_data = [solar_panels_sales, wind_turbines_sales, electric_vehicles_sales,
               battery_storage_sales, hydrogen_fuel_cells_sales]

average_sales = np.mean([solar_panels_sales, wind_turbines_sales, electric_vehicles_sales,
                         battery_storage_sales, hydrogen_fuel_cells_sales], axis=0)
years = list(range(2010, 2020 + 1))

# Plot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Horizontal Box Plot
ax1.boxplot(sales_data, patch_artist=True, labels=categories, notch=True, vert=False,
            boxprops=dict(facecolor='lightgreen', color='darkgreen'),
            whiskerprops=dict(color='darkgreen'),
            capprops=dict(color='darkgreen'),
            medianprops=dict(color='red', linewidth=1.5))

colors = ['lightcoral', 'lightblue', 'lightpink', 'palegreen', 'khaki']
for patch, color in zip(ax1.patches, colors):
    patch.set_facecolor(color)

ax1.set_title('Renewable Energy Product Sales (2010-2020)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Annual Sales (in thousands)', fontsize=12)
ax1.set_ylabel('Product Categories', fontsize=12)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax1.legend(handles, categories, title='Categories', loc='upper right')

# Second subplot: Line Plot for average annual sales
ax2.plot(years, average_sales, marker='o', linestyle='-', color='blue', label='Average Sales')
ax2.set_title('Average Annual Sales of Renewable Energy Products (2010-2020)', fontsize=16, weight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Average Sales (in thousands)', fontsize=12)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()