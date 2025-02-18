import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December'])

water_levels = np.array([1.5, 1.7, 1.8, 2.0, 2.1, 2.2, 2.5, 2.3, 2.1, 1.9, 1.6, 1.4])
temperatures = np.array([2, 3, 8, 15, 20, 25, 28, 27, 22, 16, 9, 4])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, water_levels, color='green', marker='o', linestyle='-', linewidth=2, markersize=8)
ax1.tick_params(axis='y', colors='green')
ax1.set_ylim(0, 3)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(months, temperatures, color='orange', marker='s', linestyle='-', linewidth=2, markersize=8)
ax2.tick_params(axis='y', colors='orange')
ax2.set_ylim(0, 30)

plt.tight_layout()
plt.show()