import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A community in Green Valley has been tracking their renewable energy usage to become more sustainable.
# The chart shows the increase in energy generated from Solar, Wind, Biomass, and Geothermal sources over the years.
# Additionally, the overall energy usage trend is highlighted.

# Define the years for the x-axis
years = np.arange(2010, 2023)

# Energy generation data (in gigawatt hours) for different renewable sources
solar_energy = np.array([10, 20, 35, 50, 70, 95, 120, 150, 190, 240, 300, 370, 450])
wind_energy = np.array([5, 15, 30, 50, 80, 115, 155, 200, 250, 300, 360, 420, 490])
biomass_energy = np.array([3, 5, 10, 20, 35, 55, 80, 105, 140, 180, 230, 280, 340])
geothermal_energy = np.array([1, 3, 5, 10, 18, 28, 35, 47, 60, 80, 100, 130, 160])

# Stack data for plotting
energy_data = np.vstack([solar_energy, wind_energy, biomass_energy, geothermal_energy])

# Calculate total energy generation for overlay line plot
total_energy = solar_energy + wind_energy + biomass_energy + geothermal_energy

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF4500']

# Plot the stackplot
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Biomass', 'Geothermal'], colors=colors, alpha=0.8)

# Overlay line plot for total energy generation
ax.plot(years, total_energy, color='black', linestyle='--', linewidth=2, label='Total Energy')

# Set titles and labels
ax.set_title('Green Valley: Growth of Renewable Energy Usage (2010-2022)', fontsize=15, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generated (GWh)', fontsize=12)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Enhance the grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Annotate significant points
ax.annotate('Rapid Solar Expansion', xy=(2015, 50), xytext=(2011, 180),
            arrowprops=dict(facecolor='yellow', arrowstyle='->'),
            fontsize=10, color='orange')

ax.annotate('Wind Power Growth', xy=(2021, 420), xytext=(2017, 490),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=10, color='blue')

# Adjust layout automatically
plt.tight_layout()

# Show the plot
plt.show()