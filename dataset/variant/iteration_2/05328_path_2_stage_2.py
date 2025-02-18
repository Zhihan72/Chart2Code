import matplotlib.pyplot as plt
import numpy as np

# Define the years (limited to 2005-2020)
years = np.arange(2005, 2021)

# Data for CO2 emissions (in million metric tons, matched to selected years)
co2_emissions = [335, 325, 315, 310, 305, 295, 280, 270, 260, 250, 240, 235, 229, 225, 220, 210]

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 6))

# Plot CO2 emissions as a line chart
ax1.plot(years, co2_emissions, label='CO2 Emissions', color='red', linewidth=2, marker='o', linestyle='-', markersize=6)
ax1.set_title('CO2 Emissions Over 16 Years', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('CO2 Emissions (Million Metric Tons)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', fontsize=10)

# Annotate significant events
ax1.annotate('Peak CO2 Emissions', xy=(2010, 340), xytext=(2008, 350),
             arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), fontsize=10, color='red')

# Automatically adjust layout to prevent overlap and clipping
plt.tight_layout()

# Rotate x-axis labels for readability
plt.xticks(years, rotation=45)

# Display the plot
plt.show()