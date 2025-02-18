import matplotlib.pyplot as plt
import numpy as np

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
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Bio', 'Geo'], colors=colors, alpha=0.8)

# Overlay line plot for total energy generation
ax.plot(years, total_energy, color='black', linestyle='--', linewidth=2, label='Total')

# Set titles and labels
ax.set_title('Renewable Growth (2010-22)', fontsize=15, weight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Energy (GWh)', fontsize=12)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Enhance the grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Annotate significant points
ax.annotate('Solar Surge', xy=(2015, 50), xytext=(2011, 180),
            arrowprops=dict(facecolor='yellow', arrowstyle='->'),
            fontsize=10, color='orange')

ax.annotate('Wind Growth', xy=(2021, 420), xytext=(2017, 490),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=10, color='blue')

# Adjust layout automatically
plt.tight_layout()

# Show the plot
plt.show()