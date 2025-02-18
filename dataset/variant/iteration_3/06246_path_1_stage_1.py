import matplotlib.pyplot as plt
import numpy as np

# Data for cities and months
cities = ['City A', 'City B', 'City C', 'City D', 'City E']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Rainfall data
rainfall_data = np.array([
    [78, 95, 89, 120, 150, 80, 70, 55, 60, 85, 100, 110],
    [52, 65, 70, 85, 100, 65, 50, 45, 55, 75, 80, 90],
    [85, 90, 95, 105, 120, 90, 80, 60, 70, 95, 110, 130],
    [60, 75, 80, 95, 110, 75, 65, 55, 60, 80, 95, 105],
    [90, 105, 110, 130, 150, 100, 90, 75, 85, 110, 125, 140]
])

# Temperature data
temperature_data = np.array([
    [5, 7, 10, 13, 17, 21, 24, 23, 20, 15, 10, 6],
    [2, 4, 7, 10, 15, 19, 22, 22, 18, 13, 8, 3],
    [8, 10, 12, 15, 20, 25, 28, 27, 24, 18, 12, 9],
    [4, 6, 9, 12, 16, 20, 23, 22, 19, 14, 9, 5],
    [3, 5, 8, 11, 16, 19, 21, 20, 17, 12, 7, 4]
])

# Colors for plotting
color_rainfall = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
color_temperature = ['#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot average monthly rainfall data as stacked bar for each city
bottoms = np.zeros(len(months))
for idx, city in enumerate(cities):
    ax1.bar(months, rainfall_data[idx], bottom=bottoms, color=color_rainfall[idx], alpha=0.7, label=f'{city} Drizzle')
    bottoms += rainfall_data[idx]

# Set title and axis labels for rainfall data
ax1.set_title('Yearly Precipitation & Heat Allocation\nin Prominent Urban Areas', fontsize=18, fontweight='bold')
ax1.set_xlabel('Time Periods', fontsize=14)
ax1.set_ylabel('Average Raindrop Quantity (mm)', fontsize=14, color='navy')
ax1.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax1.tick_params(axis='y', labelcolor='navy')
ax1.legend(loc='upper left', title='Areas', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# Create a twin y-axis for temperature data
ax2 = ax1.twinx()
for idx, city in enumerate(cities):
    ax2.plot(months, temperature_data[idx], marker='o', color=color_temperature[idx], linestyle='-', linewidth=2, markersize=6, label=f'{city} Warmth')

# Set properties for temperature axis
ax2.set_ylabel('Mean Heat (°C)', fontsize=14, color='firebrick')
ax2.tick_params(axis='y', labelcolor='firebrick')

# Optimize layout to avoid overlapping
fig.tight_layout()

# Display the chart
plt.show()