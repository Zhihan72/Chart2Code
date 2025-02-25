import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature_celsius = np.array([-5, -2, 4, 10, 16, 21, 25, 24, 19, 12, 5, -1])
precipitation_mm = np.array([60, 45, 50, 40, 70, 85, 90, 82, 75, 70, 65, 50])

# Create a figure with two y-axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the temperature data using gray consistently
ax1.plot(months, temperature_celsius, color='gray', marker='o', linestyle='-', linewidth=2, markersize=6)
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Temperature (°C)', fontsize=14, color='gray')
ax1.tick_params(axis='y', labelcolor='gray')
ax1.set_ylim(-10, 30)

# Creating a second y-axis for precipitation using the same gray color
ax2 = ax1.twinx()
ax2.bar(months, precipitation_mm, color='gray', alpha=0.5)
ax2.set_ylabel('Precipitation (mm)', fontsize=14, color='gray')
ax2.tick_params(axis='y', labelcolor='gray')
ax2.set_ylim(0, 100)

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()