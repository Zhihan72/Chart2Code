import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

city_a_temperatures = np.array([5, 7, 10, 11, 14, 20, 22, 18, 17, 14, 9, 6])
city_b_temperatures = np.array([2, 6, 9, 10, 16, 19, 27, 26, 19, 13, 6, 5])

plt.figure(figsize=(14, 8))

plt.plot(months, city_a_temperatures, color='green', marker='o', linestyle='-', linewidth=2, markersize=6, label='City A Temperatures (°C)')

plt.plot(months, city_b_temperatures, color='purple', marker='s', linestyle='--', linewidth=2, markersize=6, label='City B Temperatures (°C)')

heatwave_months = np.array(['Jul', 'Aug'])
heatwave_temps = city_b_temperatures[6:8]
plt.plot(heatwave_months, heatwave_temps, color='yellow', marker='*', linestyle='-', linewidth=2, markersize=10, label='Heatwave Impact (City B)')

plt.annotate('City B Max Temp', xy=('Jul', 27), xytext=('May', 30),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10)

plt.title('Yearly Temperature Changes in City A and City B\nWith a Focus on a Significant Heatwave', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12, labelpad=10)
plt.ylabel('Temperature (°C)', fontsize=12, labelpad=10)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

plt.show()