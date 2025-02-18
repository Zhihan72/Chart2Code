import matplotlib.pyplot as plt
import numpy as np

# Data for average monthly temperatures (Celsius) and rainfall (mm)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperatures = np.array([7, 22, 10, 14, 5, 25, 18, 24, 20, 15, 10, 6])  # Shuffled temperatures
rainfall = np.array([60, 50, 65, 70, 75, 55, 45, 70, 55, 50, 70, 65])    # Shuffled rainfall

fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:red'
ax1.set_xlabel('Month', fontsize=12, fontweight='bold')
ax1.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold', color=color)
ax1.plot(months, temperatures, color=color, marker='o', markersize=8, linestyle='-', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Rainfall (mm)', fontsize=12, fontweight='bold', color=color)
ax2.plot(months, rainfall, color=color, marker='s', markersize=8, linestyle='-', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Seasonal Variations in Auroria: Temperature and Rainfall over a Year', fontsize=16, fontweight='bold', pad=20)
fig.tight_layout()

plt.show()