import matplotlib.pyplot as plt
import numpy as np

# Backstory: 
# Our city Urbania has experienced drastic changes in monthly average temperatures and monthly rainfall over the last decades due to climate change.
# In this plot, we'll visualize the monthly average temperature over a year alongside the corresponding cumulative rainfall.

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Average temperature data (in °C)
avg_temp = np.array([3, 5, 10, 14, 18, 22, 25, 24, 20, 15, 8, 4])

# Cumulative rainfall data (in mm)
cumulative_rainfall = np.array([50, 80, 120, 160, 210, 270, 350, 430, 500, 570, 620, 680])

# Plotting the charts
fig, ax1 = plt.subplots(figsize=(14, 8))

# Setup primary (left) y-axis for temperature
ax1.set_title("Climate Trends in Urbania: Temperature and Rainfall Patterns", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14)
ax1.set_ylabel("Average Temperature (°C)", fontsize=14, color='tab:orange')
ax1.plot(months, avg_temp, color='tab:orange', label='Average Temperature', linewidth=2)
ax1.fill_between(months, avg_temp, color='orange', alpha=0.3)
ax1.tick_params(axis='y', labelcolor='tab:orange')
ax1.set_ylim(0, 30)

# Adding secondary y-axis for cumulative rainfall
ax2 = ax1.twinx()
ax2.set_ylabel("Cumulative Rainfall (mm)", fontsize=14, color='tab:blue')
ax2.plot(months, cumulative_rainfall, color='tab:blue', label='Cumulative Rainfall', linewidth=2)
ax2.fill_between(months, cumulative_rainfall, color='blue', alpha=0.3)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set_ylim(0, 700)

# Configure legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# Adding grid for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Annotation to highlight significant changes
ax1.annotate('Sharp Temperature Increase in Summer', xy=('Jul', 25), xytext=('Apr', 27),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')

ax2.annotate('Monsoon Rainfall Peak', xy=('Aug', 430), xytext=('Jun', 520),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10, color='purple')

# Automatically adjust layout for readability
plt.tight_layout()

# Show plot
plt.show()