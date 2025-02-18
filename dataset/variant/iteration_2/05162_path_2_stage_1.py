import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Define hypothetical installation capacity data for three regions: North, Central, and South
north_region = np.array([50, 60, 70, 85, 95, 105, 130, 145, 160, 180, 200])
central_region = np.array([30, 45, 65, 80, 100, 110, 135, 150, 170, 190, 210])
south_region = np.array([20, 25, 35, 50, 65, 75, 90, 100, 115, 130, 150])

# Calculate total capacity over the years
total_capacity = north_region + central_region + south_region

# Plot the data
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot line graphs for each region with shuffled colors
ax1.plot(years, north_region, marker='o', linestyle='-', color='green', linewidth=2, label='North Region')
ax1.plot(years, central_region, marker='s', linestyle='--', color='red', linewidth=2, label='Central Region')
ax1.plot(years, south_region, marker='^', linestyle='-.', color='blue', linewidth=2, label='South Region')

# Plot the total capacity line graph on a secondary y-axis with a different color
ax2 = ax1.twinx()
ax2.plot(years, total_capacity, marker='D', linestyle='-', color='orange', linewidth=2, label='Total Capacity')

# Titles and labels
ax1.set_title('WindCo Annual Wind Farm Installation Capacity (2010-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14, labelpad=15)
ax1.set_ylabel('Installation Capacity (MW) per Region', fontsize=14, labelpad=15)
ax2.set_ylabel('Total Installation Capacity (MW)', fontsize=14, labelpad=15)

# Customize x-ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Add legends
region_legend = ax1.legend(loc='upper left', bbox_to_anchor=(1, 0.7), title='Regions')
total_capacity_legend = ax2.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Total Capacity')

# Ensure the different legends do not overlap
ax1.add_artist(region_legend)

# Annotate key milestones
annotations = {
    2015: ("North Region Expansion", north_region[5]),
    2018: ("Central Region New Projects", central_region[8]),
    2020: ("South Region Major Installation", south_region[10]),
}

for year, (text, y_value) in annotations.items():
    ax1.annotate(text, xy=(year, y_value), xytext=(year, y_value + 20),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

# Add a grid for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()