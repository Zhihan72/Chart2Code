import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
rainfall = [50, 60, 80, 100, 120, 150, 180, 170, 140, 100, 80, 60]
temperature = [5, 7, 12, 18, 22, 25, 27, 26, 22, 16, 10, 6]

fig, (ax2, ax1) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

ax2.plot(months, temperature, color='skyblue', marker='o', linestyle='-', linewidth=2, markersize=5, label='Temp (°C)')
ax2.set_ylabel('Temp (°C)', fontsize=12)
ax2.legend(loc='upper right')
ax2.grid(True, which='both', linestyle='--', alpha=0.6)

ax1.fill_between(months, rainfall, color='orange', alpha=0.6, label='Rain (mm)')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Rain (mm)', fontsize=12)
ax1.set_title('WeatherVille Weather Trends', fontsize=16, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, which='both', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()