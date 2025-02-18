import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1800, 1820, 1840, 1860, 1880])
black_beard_fleet = np.array([500, 1200, 2300, 1800, 700])
red_beard_fleet = np.array([300, 700, 1100, 1300, 500])
shadow_reapers_fleet = np.array([100, 600, 1000, 1300, 1800])

plt.figure(figsize=(12, 8))

plt.plot(decades, black_beard_fleet, marker='v', linestyle='-.', linewidth=1.5, color='blue')
plt.plot(decades, red_beard_fleet, marker='^', linestyle='-', linewidth=2.5, color='green')
plt.plot(decades, shadow_reapers_fleet, marker='x', linestyle=':', linewidth=1, color='orange')

plt.grid(True, linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()