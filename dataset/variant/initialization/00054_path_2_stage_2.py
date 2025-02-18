import matplotlib.pyplot as plt
import numpy as np

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
capacities = np.array([
    [120, 200, 80, 40],    # Africa
    [300, 500, 200, 100],  # Asia
    [250, 300, 150, 60],   # Europe
    [180, 240, 100, 50],   # North America
    [160, 180, 90, 40],    # South America
    [100, 120, 70, 30],    # Oceania
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