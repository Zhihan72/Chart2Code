import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

city_a_temps = np.array([6, 5, 11, 10, 15, 17, 22, 18, 16, 12, 7, 4])
city_b_temps = np.array([2, 4, 9, 10, 14, 17, 25, 26, 17, 11, 6, 5])

plt.figure(figsize=(14, 8))

# Changed the color parameter for both city data groups and the heatwave period to blue
plt.plot(months, city_a_temps, color='blue', marker='D', linestyle='-.', linewidth=1.5, markersize=8, label='City A')

plt.plot(months, city_b_temps, color='blue', marker='^', linestyle='-', linewidth=3, markersize=9, label='City B')

heatwave_months = np.array(['Jul', 'Aug'])
heatwave_temps = city_b_temps[6:8]
plt.plot(heatwave_months, heatwave_temps, color='blue', marker='x', linestyle=':', linewidth=2, markersize=12, label='Heatwave')

# Adjusting annotation to match plot color change
plt.annotate('Max Temp', xy=('Jul', 25), xytext=('May', 30), arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=11)

plt.title('Temperature Changes', fontsize=18, fontweight='medium', pad=15)
plt.xlabel('Month', fontsize=13, labelpad=8)
plt.ylabel('Temp (°C)', fontsize=13, labelpad=8)

plt.grid(True, linestyle='-', alpha=0.7)
plt.legend(loc='lower right', fontsize=12, shadow=True)
plt.tight_layout()

plt.show()