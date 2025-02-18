import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solarance_production = [20, 25, 30, 40, 55, 60, 80, 85, 90, 95, 100]
windgen_production = [15, 20, 25, 30, 40, 50, 55, 60, 70, 80, 90]
hydroflow_production = [10, 12, 15, 18, 25, 35, 50, 55, 60, 65, 70]
geothermal_production = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]  # New data series
biomass_production = [8, 13, 18, 23, 30, 35, 40, 50, 55, 60, 65]  # New data series

plt.figure(figsize=(14, 8))

plt.plot(years, solarance_production, marker='D', linestyle='-.', color='#ff5733', linewidth=2)
plt.plot(years, windgen_production, marker='x', linestyle=':', color='#33c4ff', linewidth=2)
plt.plot(years, hydroflow_production, marker='+', linestyle='--', color='#82e0aa', linewidth=2)
plt.plot(years, geothermal_production, marker='o', linestyle='-', color='#8e44ad', linewidth=2)  # Plot for geothermal
plt.plot(years, biomass_production, marker='s', linestyle='-', color='#f39c12', linewidth=2)  # Plot for biomass

plt.legend(['Solarance Production', 'Windgen Production', 'Hydroflow Production', 'Geothermal Production', 'Biomass Production'], loc='upper left')

plt.grid(True, linestyle=':', alpha=0.9)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(10, 111, step=10))

plt.tight_layout()
plt.show()