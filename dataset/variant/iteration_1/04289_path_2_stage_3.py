import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rainfall = [65, 45, 75, 95, 125, 155, 175, 155, 145, 105, 85, 65]
avg_temperature = [4, 8, 11, 14, 21, 24, 29, 26, 23, 16, 13, 6]

fig, ax1 = plt.subplots(figsize=(14, 8))

color_rainfall = 'forestgreen'
ax1.plot(months, rainfall, marker='o', linestyle='-', color=color_rainfall, linewidth=2)
ax1.tick_params(axis='y', colors=color_rainfall)
ax1.grid(True, linestyle='--', alpha=0.7)

ax2 = ax1.twinx()
color_temperature = 'darkorange'
ax2.plot(months, avg_temperature, marker='s', linestyle='--', color=color_temperature, linewidth=2)
ax2.tick_params(axis='y', colors=color_temperature)

fig.tight_layout()
plt.show()