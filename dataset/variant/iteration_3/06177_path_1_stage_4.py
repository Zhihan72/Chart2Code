import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
avg_temps = np.array([5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6])
precipitation = np.array([70, 55, 60, 80, 90, 100, 45, 40, 75, 85, 95, 80])
humidity = np.array([80, 75, 70, 65, 60, 55, 50, 55, 60, 70, 75, 80])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, avg_temps, color='darkred', marker='D', linestyle='-', linewidth=3, label='Temp (°C)')
ax1.set_title('Climate: Coastal Town', fontsize=18, pad=15)
ax1.set_xlabel('Mo', fontsize=14)
ax1.set_ylabel('Temp (°C)', fontsize=14, color='darkred')
ax1.tick_params(axis='y', labelcolor='darkred')

ax2 = ax1.twinx()
ax2.plot(months, precipitation, color='darkblue', marker='x', linestyle='-.', linewidth=3, label='Precip (mm)')
ax2.set_ylabel('Precip (mm)', fontsize=14, color='darkblue')
ax2.tick_params(axis='y', labelcolor='darkblue')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 80))
ax3.plot(months, humidity, color='darkgreen', marker='1', linestyle=':', linewidth=3, label='Humid (%)')
ax3.set_ylabel('Humid (%)', fontsize=14, color='darkgreen')
ax3.tick_params(axis='y', labelcolor='darkgreen')

ax1.legend(loc='lower left')
ax2.legend(loc='lower center')
ax3.legend(loc='lower right')

ax1.grid(True, linestyle='-', alpha=0.3)

ax1.annotate('Peak Heat', xy=('Jul', 28), xytext=('Nov', 32),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

plt.tight_layout()
plt.show()