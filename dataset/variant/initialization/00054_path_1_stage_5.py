import matplotlib.pyplot as plt
import numpy as np

continents = ['Asia', 'Africa', 'South America', 'Europe', 'North America', 'Oceania']
capacities = np.array([
    [500, 100, 300, 200],  # Asia
    [80, 40, 120, 200],    # Africa
    [90, 40, 160, 180],    # South America
    [150, 250, 60, 300],   # Europe
    [240, 50, 100, 180],   # North America
    [70, 30, 100, 120],    # Oceania
])

total_capacities = capacities.sum(axis=1)
sorted_continents = ['Asia', 'Africa', 'South America', 'Europe', 'North America', 'Oceania']
sorted_capacities = [1100, 440, 470, 760, 570, 320]

fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(sorted_continents, sorted_capacities, color='skyblue')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()