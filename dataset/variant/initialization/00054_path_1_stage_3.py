import matplotlib.pyplot as plt
import numpy as np

# Data preparation
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
capacities = np.array([
    [80, 40, 120, 200],    # Africa
    [500, 100, 300, 200],  # Asia
    [150, 250, 60, 300],   # Europe
    [240, 50, 100, 180],   # North America
    [90, 40, 160, 180],    # South America
    [70, 30, 100, 120],    # Oceania
])

# Calculate total capacities for each continent
total_capacities = capacities.sum(axis=1)

# Sort the continents by total capacity
sorted_indices = np.argsort(total_capacities)[::-1]
sorted_continents = np.array(continents)[sorted_indices]
sorted_capacities = total_capacities[sorted_indices]

# Create a sorted bar plot
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(sorted_continents, sorted_capacities, color='skyblue')

# Labels and title
ax.set_xlabel('Continent')
ax.set_ylabel('Total Capacity (GW)')
ax.set_title('Total Renewable Energy Capacity by Continent in 2025')

# Display plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()