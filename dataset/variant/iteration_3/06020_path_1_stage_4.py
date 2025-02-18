import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperatures = np.array([5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6])
rainfall = np.array([70, 50, 60, 45, 55, 65, 75, 70, 60, 50, 55, 65])
wind_speed = np.array([3, 3.5, 3, 2.5, 2, 2.5, 3, 4, 4.5, 4, 3.5, 3])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Changed the marker and line style for temperatures
ax1.plot(months, temperatures, color='tab:blue', marker='*', markersize=10, linestyle='--', linewidth=2)
ax1.set_ylabel('Temperature (°C)', color='tab:blue')
ax1.tick_params(axis='y', colors='tab:blue')
ax1.grid(False)  # Disabled the grid

ax2 = ax1.twinx()

# Changed the marker and line style for rainfall
ax2.plot(months, rainfall, color='tab:green', marker='x', markersize=8, linestyle='-.', linewidth=2)
ax2.set_ylabel('Rainfall (mm)', color='tab:green')
ax2.tick_params(axis='y', colors='tab:green')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))

# Changed the marker and line style for wind speed
ax3.plot(months, wind_speed, color='tab:red', marker='d', markersize=7, linestyle=':', linewidth=2)
ax3.set_ylabel('Wind Speed (m/s)', color='tab:red')
ax3.tick_params(axis='y', colors='tab:red')

# Changed borders color and added a legend
plt.legend(['Temperature', 'Rainfall', 'Wind Speed'], loc='upper left')
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3.spines['top'].set_visible(False)

fig.tight_layout()

plt.show()