import numpy as np
import matplotlib.pyplot as plt

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Data for sea levels in mm
sea_levels_global = np.array([20, 22, 23, 25, 27, 30, 32, 35, 36, 38, 40, 44, 45, 47, 48, 50, 52, 53, 54, 57, 60])
sea_levels_atlantic = np.array([22, 24, 25, 26, 28, 30, 31, 33, 34, 36, 37, 40, 42, 43, 45, 47, 49, 50, 52, 54, 56])

# Data: Average annual global temperature anomaly (in °C)
temp_anomaly = np.array([0.35, 0.38, 0.39, 0.41, 0.45, 0.48, 0.50, 0.52, 0.53, 0.55, 0.57, 0.60, 0.62, 0.65, 0.67, 0.70, 0.72, 0.74, 0.75, 0.77, 0.80])

# Set up the main plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting sea levels with shuffled colors
ax1.plot(years, sea_levels_global, color='red', label='Global Sea Level', linewidth=2)
ax1.plot(years, sea_levels_atlantic, color='orange', linestyle='-.', label='Atlantic Sea Level', linewidth=2)

# Set the title and labels
ax1.set_title('Climate Change Impact on Sea Levels (2000-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Sea Level (mm)', fontsize=14)

# Adding grid to the plot
ax1.grid(True, linestyle='--', alpha=0.5)

# Adding legend
ax1.legend(loc='upper left', fontsize=12)

# Create another y-axis for temperature anomaly
ax2 = ax1.twinx()
ax2.plot(years, temp_anomaly, color='blue', linestyle=':', label='Temperature Anomaly (°C)', linewidth=2)

# Set the secondary y-axis label
ax2.set_ylabel('Temperature Anomaly (°C)', fontsize=14, color='blue')

# Adjustment to avoid overlapping and ensure tight layout
fig.tight_layout()

# Add legend for the secondary y-axis
fig.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1, 0.9))

# Show the plot
plt.show()