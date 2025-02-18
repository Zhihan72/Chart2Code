import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

rainfall = [60, 50, 70, 100, 120, 150, 180, 160, 140, 110, 80, 70]
avg_temperature = [5, 7, 10, 15, 20, 25, 28, 27, 22, 17, 12, 7]

fig, ax1 = plt.subplots(figsize=(14, 8))

color_rainfall = 'mediumseagreen'
ax1.plot(months, rainfall, marker='o', linestyle='-', color=color_rainfall, linewidth=2)

ax2 = ax1.twinx()

color_temperature = 'darkorange'
ax2.plot(months, avg_temperature, marker='s', linestyle='--', color=color_temperature, linewidth=2)

ax1.grid(True, linestyle='--', alpha=0.7)

fig.tight_layout()
plt.show()