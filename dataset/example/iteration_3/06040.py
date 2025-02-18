import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are visualizing the impact of technology advancement on the sales of various household appliances from 2010 to 2020.

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Data for appliance sales in thousands of units
televisions = np.array([120, 115, 110, 105, 100, 98, 95, 92, 90, 85, 80])
microwaves = np.array([60, 62, 65, 67, 70, 72, 75, 77, 80, 82, 85])
refrigerators = np.array([85, 85, 88, 90, 93, 95, 98, 100, 103, 105, 108])
washing_machines = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

# Create the figure and the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each appliance sales data with different colors and marker styles
ax.plot(years, televisions, label='Televisions', color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)
ax.plot(years, microwaves, label='Microwaves', color='green', marker='s', linestyle='--', linewidth=2, markersize=6)
ax.plot(years, refrigerators, label='Refrigerators', color='red', marker='^', linestyle='-.', linewidth=2, markersize=6)
ax.plot(years, washing_machines, label='Washing Machines', color='purple', marker='d', linestyle=':', linewidth=2, markersize=6)

# Customize the plot with titles, labels, legend, and grid
ax.set_title('Impact of Technology Advancement on Household Appliance Sales (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sales (in thousands of units)', fontsize=14)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(title='Appliances', fontsize=12, title_fontsize=14, loc='best')
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()