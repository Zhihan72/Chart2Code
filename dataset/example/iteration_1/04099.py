import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are illustrating the fictional evolution of different types of energy sources powering a futuristic city named "NeoCity" from 2025 to 2050.
# The main goal is to visualize the rise of renewable energy sources replacing traditional fossil fuels over the span of 25 years.

# Data Preparation
years = np.arange(2025, 2051)
fossil_fuels = np.array([85, 83, 80, 76, 71, 65, 58, 50, 41, 32, 23, 15, 8, 4, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
solar_power = np.array([2, 4, 7, 11, 16, 22, 30, 40, 50, 60, 70, 78, 85, 90, 93, 94, 95, 95, 96, 97, 98, 98, 98, 98, 98, 98])
wind_power = np.array([5, 6, 8, 9, 10, 12, 15, 20, 25, 30, 35, 38, 40, 42, 45, 48, 50, 52, 53, 54, 54, 55, 55, 55, 55, 55])
hydro_power = np.array([3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22])
nuclear_power = np.array([5, 7, 10, 12, 13, 15, 17, 20, 23, 25, 30, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33])

# Stack the data for plotting
energy_data = np.vstack([fossil_fuels, solar_power, wind_power, hydro_power, nuclear_power])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Use stackplot to create the chart
ax.stackplot(years, energy_data, labels=['Fossil Fuels', 'Solar Power', 'Wind Power', 'Hydro Power', 'Nuclear Power'], 
             colors=['#d73027', '#ffd700', '#1f78b4', '#33a02c', '#6a3d9a'], alpha=0.8)

# Customize the chart with title and labels
ax.set_title('Energy Transition in NeoCity\n(2025-2050)', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, weight='bold')
ax.set_ylabel('Energy Production (TWh)', fontsize=14, weight='bold')

# Rotate x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Position the legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Energy Sources', fontsize=12)

# Improve layout to prevent overlap
plt.tight_layout()

# Annotate significant milestones
ax.annotate('Solar Dominates', xy=(2041, 90), xytext=(2030, 120),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, weight='bold')
ax.annotate('Fossil Fuels Phase Out', xy=(2040, 3), xytext=(2028, 30),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, weight='bold')

# Show the plot
plt.show()