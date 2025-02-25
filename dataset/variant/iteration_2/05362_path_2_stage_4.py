import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2050, 2061)
neo_tokyo_consumption = np.array([320, 330, 305, 295, 310, 290, 280, 275, 265, 250, 240])
metropolis_consumption = np.array([345, 340, 335, 320, 315, 310, 300, 285, 270, 260, 255])
omega_city_consumption = np.array([290, 295, 285, 280, 275, 265, 255, 250, 245, 230, 220])
superville_consumption = np.array([310, 320, 315, 305, 300, 290, 280, 270, 260, 250, 240])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, neo_tokyo_consumption, marker='x', linestyle='--', color='purple', linewidth=2.5, markersize=10, label='Neo Tokyo')
ax.plot(years, metropolis_consumption, marker='v', linestyle=':', color='blue', linewidth=1.5, markersize=9, label='Metropolis')
ax.plot(years, omega_city_consumption, marker='*', linestyle='-', color='green', linewidth=3, markersize=11, label='Omega City')
ax.plot(years, superville_consumption, marker='p', linestyle='-.', color='magenta', linewidth=2, markersize=8, label='Superville')

ax.grid(True, linestyle='-', alpha=0.5)
ax.legend(loc='upper right', frameon=False)
plt.tight_layout()
plt.show()