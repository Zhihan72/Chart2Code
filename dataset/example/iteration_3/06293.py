import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# The chart is designed to show the progress of renewable energy sources 
# over decades (from 1980 to 2030) and their contribution to the total global energy consumption.
# The focus is on solar, wind, hydro, and geothermal energy sources.

# Define the decades
decades = np.arange(1980, 2031, 10)

# Artificial data representing the percentage of total global energy consumption
# contributed by each source over the decades
solar_energy = [0.1, 0.5, 2, 5, 15, 25]  # percentages
wind_energy = [0.3, 1, 3, 8, 20, 30]
hydro_energy = [5, 6, 8, 10, 12, 15]
geothermal_energy = [0.2, 0.4, 0.7, 1, 2, 5]

# Combine the data above into a list for ease of use
data = [solar_energy, wind_energy, hydro_energy, geothermal_energy]

# Labels for each renewable energy source
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']

# Colors for the line plots
colors = ['#FFA07A', '#20B2AA', '#1E90FF', '#CD5C5C']

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each energy source's contribution over the decades
for i, source in enumerate(energy_sources):
    ax.plot(decades, data[i], marker='o', color=colors[i], linewidth=2, linestyle='-', label=source)

# Customize the chart title and axis labels
ax.set_title("Growth of Renewable Energy Sources (1980-2030):\nA Decadal Analysis", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage of Total Global Energy Consumption (%)', fontsize=12)

# Ensure the x and y axis limits are clear for comparison
ax.set_xlim(1980, 2030)
ax.set_ylim(0, 35)

# Display a legend to identify different energy sources
ax.legend(title='Energy Sources', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines to improve readability
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust subplots to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()