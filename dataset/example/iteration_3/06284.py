import matplotlib.pyplot as plt
import numpy as np

# Backstory: Monthly Climate Data of a Coastal City - Analysis of Temperature and Rainfall Trends

# Months of a year
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Average daily temperatures in Celsius
temperatures = [15.0, 16.1, 18.3, 20.5, 23.2, 25.7, 27.5, 27.0, 25.3, 21.2, 18.0, 15.4]

# Total monthly rainfall in mm
rainfall = [78, 60, 55, 42, 30, 25, 18, 20, 40, 90, 110, 120]

# Creating the figure and subplots
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plotting Temperature data on left y-axis
ax1.plot(months, temperatures, color='tab:red', marker='o', linestyle='-', linewidth=2, label='Avg Temperature (°C)')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Average Temperature (°C)', fontsize=12, color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.grid(axis='y', linestyle='--', color='grey', alpha=0.6)

# Creating a second y-axis for Rainfall
ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis
ax2.plot(months, rainfall, color='tab:blue', marker='s', linestyle='--', linewidth=2, label='Total Rainfall (mm)')
ax2.set_ylabel('Total Rainfall (mm)', fontsize=12, color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.grid(axis='y', linestyle=':', color='grey', alpha=0.6)

# Adding titles and legends
plt.title("Monthly Climate Analysis of Coastal City\nTemperature and Rainfall Trends", fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Optimizing layout to prevent overlap
plt.tight_layout()

# Displaying the plot
plt.show()