import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
solar_growth = [1, 2, 3, 5, 7, 10, 14, 19, 25, 30, 35, 40, 45, 48, 52, 56, 60, 65, 70, 75, 80]
wind_growth = [2, 3, 5, 8, 11, 15, 20, 25, 30, 36, 42, 49, 55, 61, 68, 75, 82, 90, 97, 104, 110]

plt.figure(figsize=(12, 7))

# Altering the stylistic elements
plt.plot(years, solar_growth, color='green', marker='x', linewidth=3, linestyle=':')
plt.plot(years, wind_growth, color='purple', marker='s', linewidth=3, linestyle='-.')

# Modifying the grid and other elements
plt.grid(True, linestyle='-', alpha=0.7)
plt.xticks(years[::3], rotation=60)
plt.yticks(np.arange(0, 121, 15))

plt.legend(['Solar Growth', 'Wind Growth'], loc='upper left', fontsize=12, frameon=False)
plt.tight_layout()
plt.show()