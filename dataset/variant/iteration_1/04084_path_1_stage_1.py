import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2040
years = np.arange(2000, 2041)

# Hypothetical data for different renewable energy sources over the years
solar_power = np.linspace(5, 35, len(years))
wind_power = np.linspace(7, 25, len(years))
hydropower = np.linspace(20, 22, len(years))  # Stable, minor growth
geothermal_power = np.linspace(1, 10, len(years))
biomass_power = np.linspace(3, 8, len(years))

# Combine the data into a list for stacking
renewable_sources = np.array([solar_power, wind_power, hydropower, geothermal_power, biomass_power])

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, renewable_sources, colors=['#FDB813', '#77B5FE', '#4682B4', '#D2691E', '#32CD32'], alpha=0.85)

# Set title and labels for the consumption plot
ax.set_title("Growth of Renewable Energy Sources from 2000 to 2040", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production Share (%)', fontsize=12, color='black')

# Customize x-axis tick labels to avoid overlap
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()