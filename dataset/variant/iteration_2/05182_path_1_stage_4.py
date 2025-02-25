import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature_celsius = np.array([-5, -2, 4, 10, 16, 21, 25, 24, 19, 12, 5, -1])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, temperature_celsius, color='darkorange', marker='s', linestyle='--', linewidth=2, markersize=8, label='Temp (°C)')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Temperature (°C)', fontsize=14, color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')
ax1.set_ylim(-10, 30)

plt.title('WeatherVille Annual Temperature', fontsize=16, fontweight='bold')

ax1.legend(loc='upper right')

ax1.grid(True, linestyle=':', alpha=0.8)
plt.tight_layout()
plt.show()