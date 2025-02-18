import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
ny_temps = np.array([9.7, 10.2, 10.0, 9.8, 10.1, 10.3, 10.5, 10.6, 10.9, 11.0, 11.2])
la_temps = np.array([17.5, 17.8, 17.9, 18.1, 18.2, 18.4, 18.5, 18.7, 18.8, 19.0, 19.2])
chicago_temps = np.array([8.5, 8.6, 8.8, 9.0, 9.1, 9.3, 9.4, 9.5, 9.8, 10.0, 10.2])
boston_temps = np.array([7.9, 8.1, 8.2, 8.4, 8.6, 8.9, 9.0, 9.1, 9.3, 9.5, 9.8])
miami_temps = np.array([24.5, 24.7, 24.8, 25.0, 25.2, 25.3, 25.5, 25.6, 25.8, 26.0, 26.2])

plt.figure(figsize=(12, 7))

plt.plot(years, ny_temps, marker='o', linestyle='-', linewidth=2, color='red')
plt.plot(years, la_temps, marker='s', linestyle='--', linewidth=2, color='green')
plt.plot(years, chicago_temps, marker='^', linestyle='-.', linewidth=2, color='blue')
plt.plot(years, boston_temps, marker='d', linestyle=':', linewidth=2, color='purple')
plt.plot(years, miami_temps, marker='x', linestyle=(0, (3, 1, 1, 1)), linewidth=2, color='orange')

plt.title('Temp Changes (2010-2020) NY, LA, CHI, BOS, MIA', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Avg Temp (°C)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(7, 27, 1))

plt.tight_layout()

plt.show()