import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Data for appliance sales in thousands of units
televisions = np.array([120, 115, 110, 105, 100, 98, 95, 92, 90, 85, 80])
refrigerators = np.array([85, 85, 88, 90, 93, 95, 98, 100, 103, 105, 108])
washing_machines = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

# Create the figure and the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each appliance sales data with different colors and marker styles
ax.plot(years, televisions, label='TVs', color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)
ax.plot(years, refrigerators, label='Fridges', color='red', marker='^', linestyle='-.', linewidth=2, markersize=6)
ax.plot(years, washing_machines, label='Washers', color='purple', marker='d', linestyle=':', linewidth=2, markersize=6)

# Customize with altered titles, labels, legend, and grid
ax.set_title('Tech Boom: Appliance Sales Trends (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Fiscal Year', fontsize=14)
ax.set_ylabel('Units Sold (000s)', fontsize=14)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(title='Device Types', fontsize=12, title_fontsize=14, loc='best')
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()