import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart illustrates the evolution of various greenhouse gases emissions (CO2, CH4, N2O, and F-gases) from industrial activities over the decades 1970 to 2020.
# This data helps to understand the relative contributions of different gases over time and highlights significant changes in industrial processes and policies.

# Define the decades from 1970 to 2020
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Data for each gas in million metric tons
co2_emissions = np.array([7000, 9000, 11000, 13000, 15000, 16000])
ch4_emissions = np.array([1500, 1700, 1800, 1900, 2000, 2100])
n2o_emissions = np.array([300, 350, 400, 450, 500, 550])
fgases_emissions = np.array([50, 100, 150, 200, 250, 300])

# Combine data into a stacked array
emissions_data = np.vstack([co2_emissions, ch4_emissions, n2o_emissions, fgases_emissions])

# Colors for each gas
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked area chart
ax.stackplot(decades, emissions_data, labels=['CO2', 'CH4', 'N2O', 'F-gases'], colors=colors, alpha=0.85)

# Set the title and labels with line breaks for clarity and readability
ax.set_title('Industrial Greenhouse Gas Emissions Over Decades\n(1970-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=14)
ax.set_ylabel('Emissions (Million Metric Tons)', fontsize=14)

# Add legend and position it outside the plot area
ax.legend(title='Greenhouse Gas', loc='upper left', bbox_to_anchor=(1.05, 1))

# Enable grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels to prevent overlap
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=45)

# Annotate important milestones
ax.annotate('Kyoto Protocol Adopted', xy=(2000, 14000), xytext=(2005, 17000),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()