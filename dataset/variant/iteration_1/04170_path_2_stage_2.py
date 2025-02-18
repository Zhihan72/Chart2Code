import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

solar_temps = [30, 32, 31, 29, 28, 27, 26]
rain_temps = [22, 24, 23, 21, 20, 19, 18]

day_indices = np.arange(len(days))

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(day_indices, solar_temps, marker='x', markersize=7, color='orange', label='Solaris', linestyle='-.', linewidth=2)
ax.plot(day_indices, rain_temps, marker='s', markersize=7, color='blue', label='Rainfall', linestyle='--', linewidth=2)

ax.set_title('Daily Temperature Variations in Fictional Cities\nSolaris & Rainfall', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Days of the Week', fontsize=12, weight='bold')
ax.set_ylabel('Temperature (°C)', fontsize=12, weight='bold')

ax.set_xticks(day_indices)
ax.set_xticklabels(days, rotation=45, ha='right')

ax.grid(visible=True, linestyle=':', alpha=0.5)

ax.legend(loc='lower left', fontsize=11, title='Cities')

highlight_days = [2, 5]
for day in highlight_days:
    ax.axvline(x=day, color='grey', linestyle='-.', linewidth=1)

ax.annotate('Midweek Peak\nin Solaris', xy=(2, 31), xytext=(3, 33),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

plt.xlim(-1, 7)
plt.ylim(17, 35)

plt.tight_layout()
plt.show()