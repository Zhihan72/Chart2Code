import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solarance_production = [20, 25, 30, 40, 55, 60, 80, 85, 90, 95, 100]
windgen_production = [15, 20, 25, 30, 40, 50, 55, 60, 70, 80, 90]
hydroflow_production = [10, 12, 15, 18, 25, 35, 50, 55, 60, 65, 70]

plt.figure(figsize=(14, 8))

# Random changes in markers, line styles, and colors
plt.plot(years, solarance_production, marker='D', linestyle='-.', color='#ff5733', linewidth=2)  # Modified marker, linestyle, and color
plt.plot(years, windgen_production, marker='x', linestyle=':', color='#33c4ff', linewidth=2)  # Modified marker, linestyle, and color
plt.plot(years, hydroflow_production, marker='+', linestyle='--', color='#82e0aa', linewidth=2)  # Modified marker, linestyle, and color

# Added legend with modified positions
plt.legend(['Solarance Production', 'Windgen Production', 'Hydroflow Production'], loc='upper left')

# Changed grid style
plt.grid(True, linestyle=':', alpha=0.9)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(10, 111, step=10))

plt.tight_layout()
plt.show()