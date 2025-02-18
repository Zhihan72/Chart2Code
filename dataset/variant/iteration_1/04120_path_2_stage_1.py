import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
ny_temps = np.array([9.7, 10.2, 10.0, 9.8, 10.1, 10.3, 10.5, 10.6, 10.9, 11.0, 11.2])
la_temps = np.array([17.5, 17.8, 17.9, 18.1, 18.2, 18.4, 18.5, 18.7, 18.8, 19.0, 19.2])
chicago_temps = np.array([8.5, 8.6, 8.8, 9.0, 9.1, 9.3, 9.4, 9.5, 9.8, 10.0, 10.2])

plt.figure(figsize=(12, 7))
plt.plot(years, ny_temps, marker='o', label='NY', linestyle='-', linewidth=2, color='blue')
plt.plot(years, la_temps, marker='s', label='LA', linestyle='--', linewidth=2, color='red')
plt.plot(years, chicago_temps, marker='^', label='CHI', linestyle='-.', linewidth=2, color='green')

plt.annotate('Increase Start', xy=(2010, ny_temps[0]), xytext=(2012, ny_temps[0] - 1),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')
plt.annotate('Increase', xy=(2015, la_temps[5]), xytext=(2015, la_temps[5] + 1),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, color='red')
plt.annotate('Polar Vortex', xy=(2014, chicago_temps[4]), xytext=(2016, chicago_temps[4] + 1),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green')

plt.title('Temperature Changes (2010-2020)', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Avg Temp (°C)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(8, 21, 1))

plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper left', fontsize=10, title='Cities', title_fontsize='13')
plt.tight_layout()
plt.show()