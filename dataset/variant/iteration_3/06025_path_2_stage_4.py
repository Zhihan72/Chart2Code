import matplotlib.pyplot as plt
import numpy as np

# Data arrays 
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Temperature data
city_a_2016 = np.array([3.1, 4.0, 7.5, 12.3, 17.9, 22.2, 25.5, 24.9, 20.3, 14.2, 9.1, 4.1])
city_a_2017 = np.array([2.9, 3.8, 7.7, 11.8, 17.5, 21.8, 25.2, 24.8, 20.1, 14.0, 8.8, 3.9])
city_a_2018 = np.array([3.0, 4.2, 7.6, 12.2, 18.0, 22.1, 25.7, 25.0, 20.4, 14.5, 9.2, 4.3])
city_a_2019 = np.array([3.2, 4.1, 7.8, 12.4, 18.1, 22.3, 25.9, 25.3, 20.7, 14.8, 9.4, 4.4])
city_a_2020 = np.array([3.3, 4.3, 8.0, 12.5, 18.3, 22.5, 26.0, 25.4, 20.9, 15.0, 9.6, 4.5])

plt.figure(figsize=(14, 8))

color = '#1f77b4'

# Plotting data
plt.plot(months, city_a_2016, marker='o', color=color)
plt.plot(months, city_a_2017, marker='s', color=color)
plt.plot(months, city_a_2018, marker='^', color=color)
plt.plot(months, city_a_2019, marker='d', color=color)
plt.plot(months, city_a_2020, marker='*', color=color)

plt.title("City A: 5-Year Temperature Patterns\n2016 to 2020 Review", fontsize=16, fontweight='bold')
plt.xlabel('Monthly Trend', fontsize=12)
plt.ylabel('Degree Celsius (°C)', fontsize=12)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()