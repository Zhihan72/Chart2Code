import matplotlib.pyplot as plt
import numpy as np

# Years for the data (2010-2020)
years = np.arange(2010, 2021)

# Artificial data representing average monthly measurements for different river health parameters
dissolved_oxygen = [7.5, 7.2, 6.9, 6.7, 6.5, 6.2, 6.0, 5.8, 5.6, 5.5, 5.2]
ph_level = [7.0, 6.9, 6.8, 6.7, 6.5, 6.4, 6.3, 6.1, 6.0, 6.0, 5.9]
nitrate_concentration = [5, 5.5, 6, 6.2, 6.5, 7, 7.3, 7.5, 8, 8.2, 8.5]

# Additional data series for water temperature (in degrees Celsius)
water_temperature = [15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20]

# Create subplots
fig, ax1 = plt.subplots(figsize=(14, 7))

# Use secondary y-axis for nitrate concentration
ax2 = ax1.twinx()

# Plot the line chart for dissolved oxygen and pH level
ax1.plot(years, dissolved_oxygen, label='Dissolved Oxygen (mg/L)', color='green', marker='x', linestyle='-', linewidth=1.5)
ax1.plot(years, ph_level, label='pH Level', color='blue', marker='*', linestyle='-.', linewidth=1.5)
ax1.plot(years, water_temperature, label='Water Temperature (°C)', color='purple', marker='o', linestyle='-', linewidth=1.5)

# Plot the nitrate concentration on a secondary y-axis
ax2.plot(years, nitrate_concentration, label='Nitrate Concentration (mg/L)', color='red', marker='d', linestyle='--', linewidth=1.5)

# Adding labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Dissolved Oxygen (mg/L) / pH Level / Water Temperature (°C)', fontsize=12, color='black')
ax2.set_ylabel('Nitrate Concentration (mg/L)', fontsize=12, color='red')
plt.title('Decadal Health Monitoring of River (2010-2020)', fontsize=16, fontweight='bold')

# Customizing ticks and legends
ax1.tick_params(axis='y', colors='green')
ax2.tick_params(axis='y', colors='red')
ax1.grid(visible=True, which='major', linestyle='-', linewidth=0.5, color='lightgrey', alpha=0.7)
fig.tight_layout()

# Adding legends
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9), fontsize=9, title='Parameters', title_fontsize='11')

# Display the plot
plt.show()