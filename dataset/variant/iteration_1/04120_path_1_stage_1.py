import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
ny_temps = np.array([9.7, 10.2, 10.0, 9.8, 10.1, 10.3, 10.5, 10.6, 10.9, 11.0, 11.2])
la_temps = np.array([17.5, 17.8, 17.9, 18.1, 18.2, 18.4, 18.5, 18.7, 18.8, 19.0, 19.2])
chicago_temps = np.array([8.5, 8.6, 8.8, 9.0, 9.1, 9.3, 9.4, 9.5, 9.8, 10.0, 10.2])

plt.figure(figsize=(12, 7))

plt.plot(years, ny_temps, marker='o', linestyle='-', linewidth=2, color='blue')
plt.plot(years, la_temps, marker='s', linestyle='--', linewidth=2, color='red')
plt.plot(years, chicago_temps, marker='^', linestyle='-.', linewidth=2, color='green')

plt.title('Decade-long Average Temperature Changes (2010-2020)\n New York, Los Angeles, and Chicago', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Annual Temperature (°C)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(8, 21, 1))

# Removed grid and legend for simpler visualization

plt.tight_layout()

plt.show()