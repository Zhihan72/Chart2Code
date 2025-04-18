import matplotlib.pyplot as plt
import numpy as np

# Data for average monthly temperatures (Celsius) and rainfall (mm)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperatures = np.array([5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6])
rainfall = np.array([70, 50, 60, 45, 55, 65, 75, 70, 60, 50, 55, 65])

# Create the figure and main subplot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the temperature data as a line plot
color = 'tab:red'
ax1.set_xlabel('Month', fontsize=12, fontweight='bold')
ax1.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold', color=color)
ax1.plot(months, temperatures, color=color, marker='o', markersize=8, linestyle='-', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)

# Create a twin y-axis to plot the rainfall data
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Rainfall (mm)', fontsize=12, fontweight='bold', color=color)
ax2.plot(months, rainfall, color=color, marker='s', markersize=8, linestyle='-', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)

# Title and layout adjustments
plt.title('Seasonal Variations in Auroria: Temperature and Rainfall over a Year', fontsize=16, fontweight='bold', pad=20)
fig.tight_layout()

# Display the plot
plt.show()