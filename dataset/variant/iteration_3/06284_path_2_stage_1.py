import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperatures = [15.0, 16.1, 18.3, 20.5, 23.2, 25.7, 27.5, 27.0, 25.3, 21.2, 18.0, 15.4]
rainfall = [78, 60, 55, 42, 30, 25, 18, 20, 40, 90, 110, 120]

fig, ax1 = plt.subplots(figsize=(12, 8))

# Using a single color for both temperature and rainfall data
common_color = 'darkgreen'

ax1.plot(months, temperatures, color=common_color, marker='o', linestyle='-', linewidth=2, label='Avg Temperature (°C)')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Average Temperature (°C)', fontsize=12, color=common_color)
ax1.tick_params(axis='y', labelcolor=common_color)
ax1.grid(axis='y', linestyle='--', color='grey', alpha=0.6)

ax2 = ax1.twinx()
ax2.plot(months, rainfall, color=common_color, marker='s', linestyle='--', linewidth=2, label='Total Rainfall (mm)')
ax2.set_ylabel('Total Rainfall (mm)', fontsize=12, color=common_color)
ax2.tick_params(axis='y', labelcolor=common_color)
ax2.grid(axis='y', linestyle=':', color='grey', alpha=0.6)

plt.title("Monthly Climate Analysis of Coastal City\nTemperature and Rainfall Trends", fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()