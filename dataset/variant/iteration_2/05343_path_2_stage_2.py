import matplotlib.pyplot as plt
import numpy as np

# Decades from 1800 to 1880
decades = np.array([1800, 1820, 1840, 1860, 1880])

# Captured territories (in square miles) by different pirate fleets
black_beard_fleet = np.array([500, 1200, 2300, 1800, 700])
red_beard_fleet = np.array([300, 700, 1100, 1300, 500])
shadow_reapers_fleet = np.array([100, 600, 1000, 1300, 1800])

plt.figure(figsize=(12, 8))

plt.plot(decades, black_beard_fleet, marker='o', linestyle='-', linewidth=2, color='red', label='Black Beard Fleet')
plt.plot(decades, red_beard_fleet, marker='s', linestyle='--', linewidth=2, color='purple', label='Red Beard Fleet')
plt.plot(decades, shadow_reapers_fleet, marker='d', linestyle='--', linewidth=2, color='black', label='Shadow Reapers Fleet')

plt.xlabel('Decade', fontsize=12)
plt.ylabel('Captured Territories (sq. miles)', fontsize=12)
plt.title('Rise and Fall of Pirate Fleets (1800-1880)', fontsize=16, fontweight='bold', pad=20)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=12)
plt.tight_layout()
plt.show()