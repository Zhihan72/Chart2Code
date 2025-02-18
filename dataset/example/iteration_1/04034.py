import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart will plot the hypothetical temperature changes in two cities (City A and City B) over the course of a year, demonstrating the impact of a heatwave.

# Create data for months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Hypothetical temperature data for City A (slight increase throughout the year) and City B (significant heatwave in July - August)
city_a_temperatures = np.array([4, 6, 9, 12, 16, 19, 21, 20, 17, 13, 8, 5])
city_b_temperatures = np.array([3, 5, 8, 11, 15, 18, 28, 27, 18, 12, 7, 4])

# Plot configuration
plt.figure(figsize=(14, 8))

# Plot data for City A
plt.plot(months, city_a_temperatures, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label='City A Temperatures (°C)')

# Plot data for City B with highlighting around observatory seasons
plt.plot(months, city_b_temperatures, color='red', marker='s', linestyle='--', linewidth=2, markersize=6, label='City B Temperatures (°C)')

# Highlight the heatwave months in City B
heatwave_months = np.array(['Jul', 'Aug'])
heatwave_temps = city_b_temperatures[6:8]
plt.plot(heatwave_months, heatwave_temps, color='orange', marker='*', linestyle='-', linewidth=2, markersize=10, label='Heatwave Impact (City B)')

# Annotations for specific data points
plt.annotate('City B Max Temp', xy=('Jul', 28), xytext=('May', 30),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10)

# Titles and labels
plt.title('Yearly Temperature Changes in City A and City B\nWith a Focus on a Significant Heatwave', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12, labelpad=10)
plt.ylabel('Temperature (°C)', fontsize=12, labelpad=10)

# Grid, Legend, and Layout
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()