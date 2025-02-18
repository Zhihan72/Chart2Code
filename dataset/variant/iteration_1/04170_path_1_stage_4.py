import matplotlib.pyplot as plt
import numpy as np

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
solar_temps = [30, 32, 31, 29, 28, 27, 26]
rain_temps = [22, 24, 23, 21, 20, 19, 18]

day_indices = np.arange(len(days))

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(day_indices, solar_temps, marker='^', markersize=7, color='blue', label='Solar', linestyle='--', linewidth=2)
ax.plot(day_indices, rain_temps, marker='s', markersize=6, color='purple', label='Rain', linestyle='-.', linewidth=2)

ax.set_title('Temp Variations\nSolar & Rain', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Days', fontsize=12, weight='bold')
ax.set_ylabel('Temp (°C)', fontsize=12, weight='bold')
ax.set_xticks(day_indices)
ax.set_xticklabels(days, rotation=45, ha='right')

ax.grid(visible=True, linestyle=':', alpha=0.8)
ax.spines['top'].set_color('gray')
ax.spines['right'].set_color('gray')

ax.legend(loc='lower left', fontsize=11, title='Weather')

highlight_days = [2, 5]
for day in highlight_days:
    ax.axvline(x=day, color='orange', linestyle='-', linewidth=1.5)

ax.annotate('Midweek Peak', xy=(2, 31), xytext=(4, 35),
            arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, ha='center')

plt.tight_layout()
plt.show()