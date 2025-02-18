import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solarance_production = [20, 25, 30, 40, 55, 60, 80, 85, 90, 95, 100]
hydroflow_production = [10, 12, 15, 18, 25, 35, 50, 55, 60, 65, 70]

plt.figure(figsize=(14, 8))

# Alter color, marker, line style, and width
plt.plot(years, solarance_production, marker='^', linestyle='--', color='green', linewidth=3, label='Solarance Production')
plt.plot(years, hydroflow_production, marker='x', linestyle='-.', color='purple', linewidth=2, label='Hydroflow Production')

# Customize grid
plt.grid(True, linestyle='-', linewidth=0.5, color='gray', alpha=0.8)

# Add legend with altered positioning and other properties
plt.legend(loc='upper left', fontsize='large', frameon=True, shadow=True)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(10, 111, step=10))
plt.tight_layout()

plt.show()