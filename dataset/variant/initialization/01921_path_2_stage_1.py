import matplotlib.pyplot as plt
import numpy as np

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
renewable_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']

renewable_data = np.array([
    [40, 25, 30, 3, 2],
    [35, 15, 40, 5, 5],
    [20, 35, 25, 10, 10],
    [25, 30, 30, 5, 10],
    [15, 20, 50, 5, 10],
    [45, 30, 10, 10, 5]
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