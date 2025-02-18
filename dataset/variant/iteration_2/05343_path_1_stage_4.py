import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1800, 1820, 1840, 1860, 1880])

black_beard_fleet = np.array([500, 1200, 2300, 1800, 700])
red_beard_fleet = np.array([300, 700, 1100, 1300, 500])
storm_riders_fleet = np.array([0, 300, 800, 1100, 1200])
shadow_reapers_fleet = np.array([100, 600, 1000, 1300, 1800])
golden_skull_fleet = np.array([200, 500, 900, 1500, 1600])

plt.figure(figsize=(12, 8))

plt.plot(decades, black_beard_fleet, marker='H', linestyle=':', linewidth=2, color='blue')
plt.plot(decades, red_beard_fleet, marker='>', linestyle='-', linewidth=1.5, color='red')
plt.plot(decades, storm_riders_fleet, marker='o', linestyle='-.', linewidth=2.5, color='darkgreen')
plt.plot(decades, shadow_reapers_fleet, marker='*', linestyle='--', linewidth=1, color='violet')
plt.plot(decades, golden_skull_fleet, marker='+', linestyle='-', linewidth=2, color='brown')

plt.grid(False)
plt.tight_layout()

plt.show()