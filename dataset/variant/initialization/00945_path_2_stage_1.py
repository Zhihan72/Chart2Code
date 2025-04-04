import matplotlib.pyplot as plt
import numpy as np

# Define years for the analysis
years = np.array([2018, 2019, 2020, 2021, 2022])

# Economic contributions (in million USD) for each sector
solar_contribution = np.array([50, 70, 90, 110, 130])
wind_contribution = np.array([40, 60, 85, 95, 105])
hydro_contribution = np.array([45, 50, 55, 60, 65])
biomass_contribution = np.array([25, 30, 35, 40, 45])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked bars
ax.bar(years, solar_contribution, color='#FDB813', edgecolor='none', alpha=0.9)
ax.bar(years, wind_contribution, bottom=solar_contribution, color='#00A86B', edgecolor='none', alpha=0.9)
ax.bar(years, hydro_contribution, bottom=solar_contribution + wind_contribution, color='#1F78B4', edgecolor='none', alpha=0.9)
ax.bar(years, biomass_contribution, bottom=solar_contribution + wind_contribution + hydro_contribution, color='#8B4513', edgecolor='none', alpha=0.9)

# Title and labels
ax.set_title("Economic Contribution of Renewable Energy\nin GreenVille (2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Economic Contribution (Million USD)", fontsize=14)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()