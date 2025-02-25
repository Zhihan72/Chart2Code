import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1800, 1820, 1840, 1860, 1880])
black_beard_fleet = np.array([500, 1200, 2300, 1800, 700])
red_beard_fleet = np.array([300, 700, 1100, 1300, 500])
shadow_reapers_fleet = np.array([100, 600, 1000, 1300, 1800])

plt.figure(figsize=(12, 8))

# Randomly changed marker types, line styles, colors, and line widths
plt.plot(decades, black_beard_fleet, marker='v', linestyle='-.', linewidth=1.5, color='blue', label='Black Beard Fleet')
plt.plot(decades, red_beard_fleet, marker='^', linestyle='-', linewidth=2.5, color='green', label='Red Beard Fleet')
plt.plot(decades, shadow_reapers_fleet, marker='x', linestyle=':', linewidth=1, color='orange', label='Shadow Reapers Fleet')

plt.xlabel('Decade', fontsize=12)
plt.ylabel('Captured Territories (sq. miles)', fontsize=12)
plt.title('Rise and Fall of Pirate Fleets (1800-1880)', fontsize=16, fontweight='bold', pad=20)

# Randomly changed grid style
plt.grid(True, linestyle='-', alpha=0.3)

# Randomly changed legend position
plt.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()