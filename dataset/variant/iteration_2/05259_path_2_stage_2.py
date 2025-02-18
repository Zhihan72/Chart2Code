import matplotlib.pyplot as plt
import numpy as np

# Define the years and corresponding atmospheric CO2 levels and global mean temperatures
years = np.arange(2000, 2021)
co2_levels = [369, 371, 373, 376, 379, 382, 384, 387, 390, 392, 394, 397, 400, 403, 405, 407, 410, 412, 414, 416, 418]
global_temps = [14.3, 14.4, 14.2, 14.5, 14.6, 14.7, 14.5, 14.8, 14.9, 15.0, 14.9, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.6, 15.7, 15.8, 15.9]

population_million = [6112.8, 6235.1, 6364.7, 6493.4, 6622.4, 6751.2, 6880.1, 7009.1, 7138.2, 7267.4, 7396.8, 7526.2, 7655.8, 7785.6, 7915.4, 8045.4, 8175.5, 8305.7, 8436.0, 8566.4, 8697.0]
co2_emissions = [27.5, 28.2, 28.9, 29.5, 30.1, 30.8, 31.5, 32.0, 32.6, 33.2, 33.9, 34.5, 35.1, 35.8, 36.4, 37.0, 37.6, 38.2, 38.9, 39.5, 40.1]
per_capita_emissions = [co2/pop for co2, pop in zip(co2_emissions, population_million)]

renewable_energy_adoption = [4.0, 4.2, 4.5, 4.7, 5.0, 5.4, 5.9, 6.5, 7.1, 7.8, 8.6, 9.5, 10.5, 11.6, 12.8, 14.1, 15.5, 17.0, 18.6, 20.3, 22.1] 

# Initialize the plot with multiple subplots and switch the positions of ax1 and ax2
fig, (ax2, ax1, ax3) = plt.subplots(3, 1, figsize=(14, 15), dpi=100)

# Plot the per capita CO2 emissions in the first subplot (previously second subplot)
ax2.plot(years, per_capita_emissions, color='green', linestyle='-', linewidth=2, marker='o', label='Per Capita CO2 Emissions (Metric Ton/Person)')
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax2.set_title('Global Per Capita CO2 Emissions (2000-2020)', fontsize=16, weight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Per Capita CO2 Emissions\n(Metric Ton/Person)', fontsize=14, color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.annotate('Sharp Increase', xy=(2015, per_capita_emissions[15]), xytext=(2010, 4.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

# Plot the CO2 levels and global temperature on the second subplot (previously first subplot)
ax1.plot(years, co2_levels, color='darkred', linestyle='-', linewidth=2, marker='o', label='Atmospheric CO2 Levels (ppm)')
ax1.plot(years, global_temps, color='darkblue', linestyle='--', linewidth=2, marker='s', label='Global Mean Temperature (°C)')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_title('Global Climate Metrics (2000-2020)\nCO2 Levels and Temperature Dynamics', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('CO2 Levels (ppm)', fontsize=14, color='darkred')
ax1.tick_params(axis='y', labelcolor='darkred')
ax1_secondary = ax1.twinx()
ax1_secondary.set_ylabel('Global Temperature (°C)', fontsize=14, color='darkblue')
ax1_secondary.plot(years, global_temps, color='darkblue', linestyle='--', linewidth=2, marker='s')
ax1_secondary.tick_params(axis='y', labelcolor='darkblue')
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax1_secondary.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)
ax1.annotate('Kyoto Protocol Ends', xy=(2012, co2_levels[12]), xytext=(2008, 410),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

# Plot the renewable energy adoption in the third subplot
ax3.plot(years, renewable_energy_adoption, color='purple', linestyle='-', linewidth=2, marker='^', label='Renewable Energy Adoption (%)')
ax3.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax3.set_title('Global Renewable Energy Adoption (2000-2020)', fontsize=16, weight='bold')
ax3.set_xlabel('Year', fontsize=14)
ax3.set_ylabel('Renewable Energy (%)', fontsize=14, color='purple')
ax3.tick_params(axis='y', labelcolor='purple')
ax3.annotate('Renewable Surge', xy=(2017, renewable_energy_adoption[17]), xytext=(2014, 15),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

plt.tight_layout()
plt.show()