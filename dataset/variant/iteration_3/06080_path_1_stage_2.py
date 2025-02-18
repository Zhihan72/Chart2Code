import numpy as np
import matplotlib.pyplot as plt

# Years
years = np.arange(1990, 2021)

# Average temperature for the fictional city (in °C)
avg_temp = np.array([12.3, 12.1, 12.6, 13.0, 13.1, 12.9, 13.5, 13.8, 14.0,
                     14.2, 13.7, 13.5, 13.9, 14.3, 14.5, 14.8, 15.2, 15.1,
                     15.6, 15.7, 16.0, 16.2, 16.4, 16.5, 16.9, 17.0, 17.1,
                     17.3, 17.5, 17.8, 18.0])

# Average precipitation (mm) for the fictional city
avg_precip = np.array([830, 820, 850, 870, 865, 875, 880, 890, 900, 910,
                       920, 915, 930, 950, 965, 970, 975, 980, 990, 995,
                       1000, 1010, 1020, 1030, 1040, 1050, 1070, 1090,
                       1100, 1120, 1140])

# Average wind speed (km/h) for the fictional city
avg_wind_speed = np.array([15, 14, 16, 16, 17, 18, 16, 15, 18, 19,
                           17, 18, 19, 16, 17, 15, 14, 16, 17, 18,
                           20, 19, 18, 17, 16, 19, 21, 20, 18, 19, 22])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot average temperature
color = 'tab:red'
ax1.set_title('Metropolis Weather Changes (1990-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Annual Period', fontsize=14)
ax1.set_ylabel('Temp Average (°C)', fontsize=14, color=color)
ax1.plot(years, avg_temp, color=color, linestyle='-', linewidth=2, marker='o', label='Temperature Data')
ax1.tick_params(axis='y', labelcolor=color)

# Creating a secondary y-axis for precipitation
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Rainfall Mean (mm)', fontsize=14, color=color)
ax2.plot(years, avg_precip, color=color, linestyle='--', linewidth=2, marker='x', label='Precipitation Data')
ax2.tick_params(axis='y', labelcolor=color)

# Creating a third y-axis for wind speed
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60)) # Offset for the third y-axis
color = 'tab:green'
ax3.set_ylabel('Wind Speed Average (km/h)', fontsize=14, color=color)
ax3.plot(years, avg_wind_speed, color=color, linestyle=':', linewidth=2, marker='s', label='Wind Speed Data')
ax3.tick_params(axis='y', labelcolor=color)

ax1.grid(True, linestyle='--', alpha=0.7)

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.show()