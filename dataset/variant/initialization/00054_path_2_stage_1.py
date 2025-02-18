import matplotlib.pyplot as plt
import numpy as np

# Data preparation
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
capacities = np.array([
    [120, 200, 80, 40],    # Africa
    [300, 500, 200, 100],  # Asia
    [250, 300, 150, 60],   # Europe
    [180, 240, 100, 50],   # North America
    [160, 180, 90, 40],    # South America
    [100, 120, 70, 30],    # Oceania
])

# Use the sum of each continent's energy capacities for each bar height
total_capacities = capacities.sum(axis=1)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting data
ax.bar(continents, total_capacities, color='skyblue')

# Adding labels and title
ax.set_xlabel('Continent')
ax.set_ylabel('Total Renewable Energy Capacity (GW)')
ax.set_title('Total Renewable Energy Projections for 2025 by Continent')

# Display the plot
plt.tight_layout()
plt.show()