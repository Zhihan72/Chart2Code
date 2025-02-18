import matplotlib.pyplot as plt
import numpy as np

# Define the months and the respective data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Average temperature data (in Celsius)
avg_temps = np.array([5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6])

# Precipitation data (in mm)
precipitation = np.array([70, 55, 60, 80, 90, 100, 45, 40, 75, 85, 95, 80])

# Average humidity data (in percentage)
humidity = np.array([80, 75, 70, 65, 60, 55, 50, 55, 60, 70, 75, 80])

# Create subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the temperature line
ax1.plot(months, avg_temps, color='tab:red', marker='o', linestyle='-', linewidth=2, label='Average Temperature (°C)')

# Set title and labels for the first y-axis
ax1.set_title('Seasonal Changes in Coastal Town: Temperature, Precipitation, and Humidity', fontsize=16, pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12, color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create the second y-axis for precipitation data
ax2 = ax1.twinx()
ax2.plot(months, precipitation, color='tab:blue', marker='s', linestyle='--', linewidth=2, label='Precipitation (mm)')
ax2.set_ylabel('Precipitation (mm)', fontsize=12, color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Create a third axis for humidity data
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(months, humidity, color='tab:green', marker='^', linestyle='-.', linewidth=2, label='Humidity (%)')
ax3.set_ylabel('Humidity (%)', fontsize=12, color='tab:green')
ax3.tick_params(axis='y', labelcolor='tab:green')

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Add gridlines
ax1.grid(True, linestyle='--', alpha=0.5)

# Annotate significant points
ax1.annotate('Peak Summer Heat', xy=('Jul', 28), xytext=('May', 30),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax2.annotate('Heavy Rain Season', xy=('Jun', 100), xytext=('Mar', 110),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()