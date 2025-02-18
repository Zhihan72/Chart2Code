import matplotlib.pyplot as plt
import numpy as np

# Renaming the months for clarity
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Original temperatures for City A altered manually while keeping the array structure
city_a_temperatures = np.array([6, 5, 11, 10, 15, 17, 22, 18, 16, 12, 7, 4])

# Original temperatures for City B altered manually
city_b_temperatures = np.array([2, 4, 9, 10, 14, 17, 25, 26, 17, 11, 6, 5])

plt.figure(figsize=(14, 8))

plt.plot(months, city_a_temperatures, color='green', marker='D', linestyle='-.', linewidth=1.5, markersize=8, label='City A (°C)')

plt.plot(months, city_b_temperatures, color='purple', marker='^', linestyle='-', linewidth=3, markersize=9, label='City B (°C)')

# Heatwave impact data altered manually to match the new sequence in City B
heatwave_months = np.array(['Jul', 'Aug'])
heatwave_temps = city_b_temperatures[6:8]
plt.plot(heatwave_months, heatwave_temps, color='gold', marker='x', linestyle=':', linewidth=2, markersize=12, label='Heatwave Impact')

plt.annotate('City B Max Temp', xy=('Jul', 25), xytext=('May', 30),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=11)

plt.title('Yearly Temperature Changes in City A and City B', fontsize=18, fontweight='medium', pad=15)
plt.xlabel('Month', fontsize=13, labelpad=8)
plt.ylabel('Temperature (°C)', fontsize=13, labelpad=8)

plt.grid(True, linestyle='-', alpha=0.7)
plt.legend(loc='lower right', fontsize=12, shadow=True)
plt.tight_layout()

plt.show()