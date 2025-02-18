import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperatures = [16.0, 15.1, 20.3, 18.5, 23.2, 27.7, 25.5, 27.0, 20.3, 21.2, 15.0, 18.4]
rainfall = [70, 90, 42, 55, 30, 18, 25, 20, 40, 78, 120, 110]

fig, ax1 = plt.subplots(figsize=(12, 8))

common_color = 'darkgreen'
ax1.plot(months, temperatures, color=common_color, marker='o', linestyle='-', linewidth=2)
ax1.set_xlabel('Mths', fontsize=12)
ax1.set_ylabel('Avg Temp (°C)', fontsize=12, color=common_color)
ax1.tick_params(axis='y', labelcolor=common_color)

ax2 = ax1.twinx()
ax2.plot(months, rainfall, color=common_color, marker='s', linestyle='--', linewidth=2)
ax2.set_ylabel('Rain (mm)', fontsize=12, color=common_color)
ax2.tick_params(axis='y', labelcolor=common_color)

plt.title("Monthly Climate: Temp & Rain", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()