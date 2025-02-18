import matplotlib.pyplot as plt
import numpy as np

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
capacities = np.array([
    [120, 220, 70, 50],    # Africa
    [310, 480, 210, 90],   # Asia
    [230, 320, 140, 80],   # Europe
    [170, 250, 110, 60],   # North America
    [150, 190, 80, 50],    # South America
    [110, 130, 60, 40],    # Oceania
])

total_capacities = capacities.sum(axis=1)

fig, ax = plt.subplots(figsize=(10, 6))

# Shuffled color order
colors = ['lightgreen', 'coral', 'gold', 'lightsalmon', 'plum', 'skyblue']

ax.bar(continents, total_capacities, color=colors)

ax.set_xlabel('Continent')
ax.set_ylabel('Total Renewable Energy Capacity (GW)')
ax.set_title('Total Renewable Energy Projections for 2025 by Continent')

plt.tight_layout()
plt.show()