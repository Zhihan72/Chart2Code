import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define coffee and energy drink consumption in cups per day
coffee_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
energy_drink_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Define productivity measured in tasks completed per day for both data series
productivity_coffee = np.array([3, 5, 8, 10, 11, 12, 11, 9, 6])
productivity_energy_drink = np.array([2, 4, 6, 8, 9, 10, 9, 7, 5])

# Create smooth lines for the scatter plots using spline interpolation
coffee_spline = make_interp_spline(coffee_consumption, productivity_coffee)
energy_drink_spline = make_interp_spline(energy_drink_consumption, productivity_energy_drink)

# Generate new consumption values for smooth lines
consumption_new = np.linspace(0, 8, 300)
productivity_coffee_smooth = coffee_spline(consumption_new)
productivity_energy_smooth = energy_drink_spline(consumption_new)

plt.figure(figsize=(12, 7))

# Scatter and smooth line plots for coffee consumption vs productivity
plt.scatter(coffee_consumption, productivity_coffee, color='brown', label='Coffee Data', s=100, edgecolor='black')
plt.plot(consumption_new, productivity_coffee_smooth, color='green', linestyle='-', linewidth=2, alpha=0.7)

# Scatter and smooth line plots for energy drink consumption vs productivity
plt.scatter(energy_drink_consumption, productivity_energy_drink, color='blue', label='Energy Drink Data', s=100, edgecolor='black')
plt.plot(consumption_new, productivity_energy_smooth, color='red', linestyle='-', linewidth=2, alpha=0.7)

# Add titles and labels
plt.title('Consumption vs Productivity in a Tech Startup', fontsize=16, fontweight='bold')
plt.xlabel('Consumption (Cups per Day)', fontsize=12)
plt.ylabel('Productivity (Tasks Completed per Day)', fontsize=12)

# Ticks and grid for readability
plt.xticks(np.arange(0, 9, step=1))
plt.yticks(np.arange(2, 14, step=2))
plt.grid(alpha=0.3, linestyle='--')

# Legend to differentiate between data series
plt.legend(fontsize=10, loc='upper left', edgecolor='gray')

plt.tight_layout()
plt.show()