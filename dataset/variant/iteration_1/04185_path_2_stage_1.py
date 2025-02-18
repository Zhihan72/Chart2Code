import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Average temperature data (in °C)
avg_temp = np.array([3, 5, 10, 14, 18, 22, 25, 24, 20, 15, 8, 4])

# Plotting the chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Setup primary (left) y-axis for temperature
ax1.set_title("Climate Trends in Urbania: Temperature Patterns", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14)
ax1.set_ylabel("Average Temperature (°C)", fontsize=14, color='tab:orange')
ax1.plot(months, avg_temp, color='tab:orange', label='Average Temperature', linewidth=2)
ax1.fill_between(months, avg_temp, color='orange', alpha=0.3)
ax1.tick_params(axis='y', labelcolor='tab:orange')
ax1.set_ylim(0, 30)

# Configure legend
ax1.legend(loc='upper left', fontsize=12)

# Adding grid for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Annotation to highlight significant changes
ax1.annotate('Sharp Temperature Increase in Summer', xy=('Jul', 25), xytext=('Apr', 27),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')

# Automatically adjust layout for readability
plt.tight_layout()

# Show plot
plt.show()