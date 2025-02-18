import matplotlib.pyplot as plt
import numpy as np

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
renewable_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']

renewable_data = np.array([
    [30, 40, 25, 3, 2],  
    [15, 35, 40, 5, 5],  
    [25, 20, 35, 10, 10],  
    [30, 25, 30, 10, 5],  
    [20, 15, 50, 5, 10],  
    [30, 45, 10, 5, 10]  
])

# New set of colors for the chart
colors = ['steelblue', 'orange', 'green', 'red', 'purple']

fig, ax = plt.subplots(figsize=(14, 8))

for i, (continent, data) in enumerate(zip(continents, renewable_data)):
    bottom = 0
    for j, percent in enumerate(data):
        ax.barh(continent, percent, color=colors[j], edgecolor='black', left=bottom)
        bottom += percent

ax.set_xlim(0, 100)

plt.tight_layout()
plt.show()