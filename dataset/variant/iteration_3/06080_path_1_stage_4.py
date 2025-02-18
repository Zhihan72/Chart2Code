import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1990, 2021)

avg_temp = np.array([12.3, 12.1, 12.6, 13.0, 13.1, 12.9, 13.5, 13.8, 14.0,
                     14.2, 13.7, 13.5, 13.9, 14.3, 14.5, 14.8, 15.2, 15.1,
                     15.6, 15.7, 16.0, 16.2, 16.4, 16.5, 16.9, 17.0, 17.1,
                     17.3, 17.5, 17.8, 18.0])
avg_precip = np.array([830, 820, 850, 870, 865, 875, 880, 890, 900, 910,
                       920, 915, 930, 950, 965, 970, 975, 980, 990, 995,
                       1000, 1010, 1020, 1030, 1040, 1050, 1070, 1090,
                       1100, 1120, 1140])
avg_wind_speed = np.array([15, 14, 16, 16, 17, 18, 16, 15, 18, 19,
                           17, 18, 19, 16, 17, 15, 14, 16, 17, 18,
                           20, 19, 18, 17, 16, 19, 21, 20, 18, 19, 22])

fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'c'  # Changed from 'darkorange' to 'c'
ax1.set_title('Metropolis Weather Changes (1990-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Annual Period', fontsize=14)
ax1.set_ylabel('Temp Average (°C)', fontsize=14, color=color)
ax1.plot(years, avg_temp, color=color, linestyle='-.', linewidth=2, marker='^', label='Temperature')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'm'  # Changed from 'deepskyblue' to 'm'
ax2.set_ylabel('Rainfall Mean (mm)', fontsize=14, color=color)
ax2.plot(years, avg_precip, color=color, linestyle='-', linewidth=2, marker='o', label='Precipitation')
ax2.tick_params(axis='y', labelcolor=color)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
color = 'navy'  # Changed from 'seagreen' to 'navy'
ax3.set_ylabel('Wind Speed Average (km/h)', fontsize=14, color=color)
ax3.plot(years, avg_wind_speed, color=color, linestyle='--', linewidth=2, marker='d', label='Wind Speed')
ax3.tick_params(axis='y', labelcolor=color)

ax1.grid(True, linestyle=':', alpha=0.5)  # Changed linestyle
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9), bbox_transform=ax1.transAxes)  # Changed legend location

plt.tight_layout()
plt.show()