import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a_temperatures = np.array([4, 6, 9, 12, 16, 19, 21, 20, 17, 13, 8, 5])
city_b_temperatures = np.array([3, 5, 8, 11, 15, 18, 28, 27, 18, 12, 7, 4])

plt.figure(figsize=(14, 8))

# Changed style for City A
plt.plot(months, city_a_temperatures, color='green', marker='D', linestyle='-.', linewidth=1.5, markersize=8, label='City A (°C)')

# Changed style for City B
plt.plot(months, city_b_temperatures, color='purple', marker='^', linestyle='-', linewidth=3, markersize=9, label='City B (°C)')

heatwave_months = np.array(['Jul', 'Aug'])
heatwave_temps = city_b_temperatures[6:8]
plt.plot(heatwave_months, heatwave_temps, color='gold', marker='x', linestyle=':', linewidth=2, markersize=12, label='Heatwave Impact')

plt.annotate('City B Max Temp', xy=('Jul', 28), xytext=('May', 30),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=11)

plt.title('Yearly Temperature Changes in City A and City B', fontsize=18, fontweight='medium', pad=15)
plt.xlabel('Month', fontsize=13, labelpad=8)
plt.ylabel('Temperature (°C)', fontsize=13, labelpad=8)

plt.grid(True, linestyle='-', alpha=0.7)
plt.legend(loc='lower right', fontsize=12, shadow=True)
plt.tight_layout()

plt.show()