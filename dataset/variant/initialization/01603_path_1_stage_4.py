import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data for consumption and productivity
coffee_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
energy_drink_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

productivity_coffee = np.array([3, 5, 8, 10, 11, 12, 11, 9, 6])
productivity_energy_drink = np.array([2, 4, 6, 8, 9, 10, 9, 7, 5])

# Interpolating the data for smooth curves
coffee_spline = make_interp_spline(coffee_consumption, productivity_coffee)
energy_drink_spline = make_interp_spline(energy_drink_consumption, productivity_energy_drink)

consumption_new = np.linspace(0, 8, 300)
productivity_coffee_smooth = coffee_spline(consumption_new)
productivity_energy_smooth = energy_drink_spline(consumption_new)

plt.figure(figsize=(12, 7))

# Altered scatter plot for coffee consumption with a different marker and color
plt.scatter(coffee_consumption, productivity_coffee, color='purple', label='Coffee', s=80, marker='^', edgecolor='gray')
plt.plot(consumption_new, productivity_coffee_smooth, color='orange', linestyle='-.', linewidth=2.5, alpha=0.8)

# Altered scatter plot for energy drink consumption with another marker and color
plt.scatter(energy_drink_consumption, productivity_energy_drink, color='cyan', label='Energy Drink', s=80, marker='s', edgecolor='gray')
plt.plot(consumption_new, productivity_energy_smooth, color='olive', linestyle=':', linewidth=2.5, alpha=0.8)

# Title and labels with changed font sizes
plt.title('Consumption vs Productivity', fontsize=18, fontweight='bold')
plt.xlabel('Cups/Day', fontsize=14)
plt.ylabel('Tasks/Day', fontsize=14)

# Modified x and y ticks
plt.xticks(np.arange(0, 9, step=1))
plt.yticks(np.arange(2, 14, step=2))

# Changed grid style and color
plt.grid(alpha=0.5, linestyle='-', color='lightgray')

# Customized legend
plt.legend(fontsize=11, loc='lower right', edgecolor='black', framealpha=0.6)

plt.tight_layout()
plt.show()