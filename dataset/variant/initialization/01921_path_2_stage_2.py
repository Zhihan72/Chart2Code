import matplotlib.pyplot as plt
import numpy as np

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
renewable_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']

renewable_data = np.array([
    [30, 40, 25, 3, 2],  # Swapped the first two values
    [15, 35, 40, 5, 5],  # Swapped the first two values
    [25, 20, 35, 10, 10],  # Swapped the first two values
    [30, 25, 30, 10, 5],  # Swapped the first two values
    [20, 15, 50, 5, 10],  # Swapped the first two values
    [30, 45, 10, 5, 10]  # Changed last two numbers within permissible limits
])

colors = plt.cm.Paired(np.arange(len(renewable_sources)))

fig, ax = plt.subplots(figsize=(14, 8))

for i, (continent, data) in enumerate(zip(continents, renewable_data)):
    bottom = 0
    for j, percent in enumerate(data):
        ax.barh(continent, percent, color=colors[j], edgecolor='black', left=bottom)
        bottom += percent

ax.set_xlim(0, 100)

ax.xaxis.grid(True, linestyle='--', alpha=0.6)
ax.yaxis.grid(False)

plt.tight_layout()
plt.show()