import matplotlib.pyplot as plt
import numpy as np

decades = ['1990s', '2000s', '2010s', '2020s', '2030s', '2040s']
contributors = ['Residential PV', 'Commercial PV', 'Utility PV', 'CSP', 'Offshore Wind', 'Onshore Wind']

solar_adoption = np.array([
    [20, 30, 40, 10, 5, 5],  # Added Offshore Wind and Onshore Wind
    [25, 35, 30, 10, 10, 5],
    [30, 30, 30, 10, 15, 5],
    [35, 25, 30, 10, 20, 10],
    [40, 20, 25, 15, 20, 20],
    [50, 15, 20, 15, 25, 25]
])

plt.figure(figsize=(14, 8))
new_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4'] # Added colors for new data
plt.stackplot(decades, solar_adoption.T, colors=new_colors, alpha=0.85)

plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()