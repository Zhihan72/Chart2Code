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

colors = ['steelblue', 'orange', 'green', 'red', 'purple']

fig, ax = plt.subplots(figsize=(14, 8))

center_value = 50  # Central value for the diverging bars
for i, (continent, data) in enumerate(zip(continents, renewable_data)):
    left = center_value
    # Plot positive deviations
    for j, percent in enumerate(data):
        if percent > center_value:
            ax.barh(continent, percent - left, color=colors[j], edgecolor='black', left=left)
            left = percent
    left = center_value
    # Plot negative deviations
    for j, percent in enumerate(data):
        if percent < center_value:
            ax.barh(continent, -left + percent, color=colors[j], edgecolor='black', left=left)
            left = percent

ax.axvline(center_value, color='black', linewidth=0.8)  # Add central axis line
ax.set_xlim(0, 100)

plt.tight_layout()
plt.show()