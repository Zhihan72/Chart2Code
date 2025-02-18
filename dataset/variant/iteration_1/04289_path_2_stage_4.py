import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rainfall = [65, 45, 75, 95, 125, 155, 175, 155, 145, 105, 85, 65]
avg_temperature = [4, 8, 11, 14, 21, 24, 29, 26, 23, 16, 13, 6]

fig, ax1 = plt.subplots(figsize=(14, 8))

color_rainfall = 'navy'
ax1.plot(months, rainfall, marker='^', linestyle='-.', color=color_rainfall, linewidth=2)
ax1.tick_params(axis='y', colors=color_rainfall)

ax2 = ax1.twinx()
color_temperature = 'crimson'
ax2.plot(months, avg_temperature, marker='D', linestyle=':', color=color_temperature, linewidth=2)
ax2.tick_params(axis='y', colors=color_temperature)

ax1.set_title('Monthly Rainfall and Average Temperature', fontsize=16)
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Rainfall (mm)', color=color_rainfall, fontsize=14)
ax2.set_ylabel('Avg Temperature (°C)', color=color_temperature, fontsize=14)

# Style changes: borders altered with a thicker grid
ax1.grid(True, linestyle='-', linewidth=1, alpha=0.5)

# Legend random alteration
ax1.legend(['Rainfall'], loc='upper left')
ax2.legend(['Avg Temperature'], loc='upper right')

fig.tight_layout()
plt.show()