import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the CO2 Emissions and Renewable Energy Usage Over Time
# This chart shows the changes in CO2 emissions and renewable energy usage in a fictional country from 2000 to 2020.

# Define the years
years = np.arange(2000, 2021)

# Data for CO2 emissions (in million metric tons)
co2_emissions = [300, 310, 320, 330, 340, 335, 325, 315, 310, 305, 295, 280, 270, 260, 250, 240, 235, 229, 225, 220, 210]

# Data for renewable energy usage (in billion kWh)
renewable_energy = [5, 6, 8, 10, 13, 18, 20, 25, 30, 35, 42, 50, 60, 70, 85, 100, 120, 145, 170, 200, 230]

# Create the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# Plot CO2 emissions as a line chart
ax1.plot(years, co2_emissions, label='CO2 Emissions', color='red', linewidth=2, marker='o', linestyle='-', markersize=6)
ax1.set_title('CO2 Emissions and Renewable Energy Usage Over Two Decades', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('CO2 Emissions (Million Metric Tons)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', fontsize=10)

# Plot renewable energy usage as a line chart
ax2.plot(years, renewable_energy, label='Renewable Energy Usage', color='green', linewidth=2, marker='s', linestyle='-', markersize=6)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Renewable Energy (Billion kWh)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left', fontsize=10)

# Annotate the significant events and data points on the charts
ax1.annotate('Peak CO2 Emissions', xy=(2010, 340), xytext=(2005, 350),
             arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), fontsize=10, color='red')

ax2.annotate('Significant Rise in Renewable\nEnergy Usage Starts', xy=(2012, 50), xytext=(2006, 110),
             arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5), fontsize=10, color='green')

# Automatically adjust layout to prevent overlap and clipping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Rotate x-axis labels for readability
plt.xticks(years, rotation=45)

# Display the plot
plt.show()