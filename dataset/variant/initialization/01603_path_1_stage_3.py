import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

coffee_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
energy_drink_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

productivity_coffee = np.array([3, 5, 8, 10, 11, 12, 11, 9, 6])
productivity_energy_drink = np.array([2, 4, 6, 8, 9, 10, 9, 7, 5])

coffee_spline = make_interp_spline(coffee_consumption, productivity_coffee)
energy_drink_spline = make_interp_spline(energy_drink_consumption, productivity_energy_drink)

consumption_new = np.linspace(0, 8, 300)
productivity_coffee_smooth = coffee_spline(consumption_new)
productivity_energy_smooth = energy_drink_spline(consumption_new)

plt.figure(figsize=(12, 7))

plt.scatter(coffee_consumption, productivity_coffee, color='blue', label='Coffee', s=100, edgecolor='black')
plt.plot(consumption_new, productivity_coffee_smooth, color='red', linestyle='-', linewidth=2, alpha=0.7)

plt.scatter(energy_drink_consumption, productivity_energy_drink, color='brown', label='Energy Drink', s=100, edgecolor='black')
plt.plot(consumption_new, productivity_energy_smooth, color='green', linestyle='-', linewidth=2, alpha=0.7)

plt.title('Consumption vs Productivity', fontsize=16, fontweight='bold')
plt.xlabel('Cups/Day', fontsize=12)
plt.ylabel('Tasks/Day', fontsize=12)

plt.xticks(np.arange(0, 9, step=1))
plt.yticks(np.arange(2, 14, step=2))
plt.grid(alpha=0.3, linestyle='--')

plt.legend(fontsize=10, loc='upper left', edgecolor='gray')

plt.tight_layout()
plt.show()