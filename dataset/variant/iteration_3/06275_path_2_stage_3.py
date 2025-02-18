import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
penetration_rate = np.array([30, 20, 65, 45, 85, 55, 75])
avg_daily_hours_online = np.array([4.8, 3.2, 1.5, 6.1, 5.5, 2.3, 4.0])

fig, ax1 = plt.subplots(figsize=(10, 6))

# Line plot for penetration rate
color1 = 'tab:blue'
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Penetration (%)', fontsize=14, color=color1)
ax1.plot(years, penetration_rate, color=color1, marker='o', markersize=8, 
         linestyle='-', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color1)

# Second y-axis for daily hours online
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel('Daily Hours', fontsize=14, color=color2)
ax2.plot(years, avg_daily_hours_online, color=color2, marker='s', markersize=8, 
         linestyle='--', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color2)

plt.tight_layout()

plt.show()