import matplotlib.pyplot as plt
import numpy as np

# Define the years and corresponding atmospheric CO2 levels and global mean temperatures
years = np.arange(2000, 2021)
co2_levels = [369, 371, 373, 376, 379, 382, 384, 387, 390, 392, 394, 397, 400, 403, 405, 407, 410, 412, 414, 416, 418]
global_temps = [14.3, 14.4, 14.2, 14.5, 14.6, 14.7, 14.5, 14.8, 14.9, 15.0, 14.9, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.6, 15.7, 15.8, 15.9]

# Define a new metric: per capita CO2 emissions
population_million = [6112.8, 6235.1, 6364.7, 6493.4, 6622.4, 6751.2, 6880.1, 7009.1, 7138.2, 7267.4, 7396.8, 7526.2, 7655.8, 7785.6, 7915.4, 8045.4, 8175.5, 8305.7, 8436.0, 8566.4, 8697.0]
co2_emissions = [27.5, 28.2, 28.9, 29.5, 30.1, 30.8, 31.5, 32.0, 32.6, 33.2, 33.9, 34.5, 35.1, 35.8, 36.4, 37.0, 37.6, 38.2, 38.9, 39.5, 40.1]
per_capita_emissions = [co2/pop for co2, pop in zip(co2_emissions, population_million)]

# Initialize the plot with multiple subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), dpi=100)

# Plot the CO2 levels and global temperature on the primary y-axis of the first subplot
ax1.plot(years, co2_levels, color='darkred', linestyle='-', linewidth=2, marker='o', label='Atmospheric CO2 Levels (ppm)')
ax1.plot(years, global_temps, color='darkblue', linestyle='--', linewidth=2, marker='s', label='Global Mean Temperature (°C)')

# Add grid and layout to the first subplot
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_title('Global Climate Metrics (2000-2020)\nCO2 Levels and Temperature Dynamics', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('CO2 Levels (ppm)', fontsize=14, color='darkred')
ax1.tick_params(axis='y', labelcolor='darkred')

# Create a secondary y-axis for the global mean temperature
ax1_secondary = ax1.twinx()
ax1_secondary.set_ylabel('Global Temperature (°C)', fontsize=14, color='darkblue')
ax1_secondary.plot(years, global_temps, color='darkblue', linestyle='--', linewidth=2, marker='s')
ax1_secondary.tick_params(axis='y', labelcolor='darkblue')

# Legends for the first subplot
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax1_secondary.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# Plot the per capita CO2 emissions in the second subplot
ax2.plot(years, per_capita_emissions, color='green', linestyle='-', linewidth=2, marker='o', label='Per Capita CO2 Emissions (Metric Ton/Person)')

# Add grid and layout to the second subplot
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax2.set_title('Global Per Capita CO2 Emissions (2000-2020)', fontsize=16, weight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Per Capita CO2 Emissions\n(Metric Ton/Person)', fontsize=14, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Annotations for significant data points
ax1.annotate('Kyoto Protocol Ends', xy=(2012, co2_levels[12]), xytext=(2008, 410),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

ax2.annotate('Sharp Increase', xy=(2015, per_capita_emissions[15]), xytext=(2010, 4.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()