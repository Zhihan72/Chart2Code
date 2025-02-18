import matplotlib.pyplot as plt
import numpy as np

# Data for average monthly temperatures, rainfall, and wind speed
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperatures = np.array([5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6])
rainfall = np.array([70, 50, 60, 45, 55, 65, 75, 70, 60, 50, 55, 65])
wind_speed = np.array([3, 3.5, 3, 2.5, 2, 2.5, 3, 4, 4.5, 4, 3.5, 3])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, temperatures, color='tab:red', marker='o', markersize=8, linestyle='-', linewidth=2)
ax1.tick_params(axis='y', colors='tab:red')
ax1.grid(True, linestyle='--', alpha=0.3)

ax2 = ax1.twinx()
ax2.plot(months, rainfall, color='tab:blue', marker='s', markersize=8, linestyle='-', linewidth=2)
ax2.tick_params(axis='y', colors='tab:blue')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(months, wind_speed, color='tab:green', marker='^', markersize=8, linestyle='-', linewidth=2)
ax3.tick_params(axis='y', colors='tab:green')

fig.tight_layout()

plt.show()