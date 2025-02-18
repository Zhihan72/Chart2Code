import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Altered average daily temperatures in Celsius
temperatures = [18.0, 16.1, 15.4, 27.5, 23.2, 20.5, 15.0, 27.0, 18.3, 21.2, 25.3, 25.7]

# Altered total monthly rainfall in mm
rainfall = [20, 110, 18, 55, 60, 78, 42, 40, 30, 90, 25, 120]

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.plot(months, temperatures, color='tab:red', marker='o', linestyle='-', linewidth=2, label='Avg Temperature (°C)')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Average Temperature (°C)', fontsize=12, color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.grid(axis='y', linestyle='--', color='grey', alpha=0.6)

ax2 = ax1.twinx()
ax2.plot(months, rainfall, color='tab:blue', marker='s', linestyle='--', linewidth=2, label='Total Rainfall (mm)')
ax2.set_ylabel('Total Rainfall (mm)', fontsize=12, color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.grid(axis='y', linestyle=':', color='grey', alpha=0.6)

plt.title("Monthly Climate Analysis of Coastal City\nTemperature and Rainfall Trends", fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()