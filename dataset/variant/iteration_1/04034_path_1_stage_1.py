import matplotlib.pyplot as plt
import numpy as np

# Create data for months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Hypothetical temperature data for City A (some randomness added) and City B (significant heatwave in July - August)
city_a_temperatures = np.array([5, 7, 10, 11, 14, 20, 22, 18, 17, 14, 9, 6])
city_b_temperatures = np.array([2, 6, 9, 10, 16, 19, 27, 26, 19, 13, 6, 5])

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
plt.annotate('City B Max Temp', xy=('Jul', 27), xytext=('May', 30),
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