import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_power = [5, 6, 8, 12, 15, 19, 25, 30, 40, 45, 50]
wind_energy = [10, 12, 15, 17, 21, 24, 28, 32, 37, 39, 42]
hydroelectric_power = [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

plt.figure(figsize=(12, 8))

plt.plot(years, solar_power, marker='D', linestyle=':', color='#FFA07A', linewidth=1.5)
plt.plot(years, wind_energy, marker='p', linestyle='-', color='#6495ED', linewidth=2.5)
plt.plot(years, hydroelectric_power, marker='*', linestyle='--', color='#90EE90', linewidth=1)

plt.xticks(years, rotation=45)
plt.grid(True, linestyle='-', alpha=0.3)
plt.tight_layout()
plt.show()