import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
ny_temps = np.array([10.1, 9.8, 10.5, 10.0, 10.3, 9.7, 11.0, 10.2, 10.6, 11.2, 10.9])
la_temps = np.array([18.5, 17.9, 18.8, 17.8, 19.0, 17.5, 18.7, 19.2, 18.2, 18.4, 18.1])
chicago_temps = np.array([9.3, 8.6, 9.5, 10.0, 8.5, 10.2, 9.0, 9.8, 8.8, 9.1, 9.4])

plt.figure(figsize=(12, 7))

# Altering stylistic elements
plt.plot(years, ny_temps, marker='*', label='NY', linestyle='-', linewidth=2, color='blue')
plt.plot(years, la_temps, marker='x', label='LA', linestyle='--', linewidth=2, color='green')
plt.plot(years, chicago_temps, marker='d', label='CHI', linestyle=':', linewidth=2, color='red')

# Updating annotations
plt.annotate('Increase Start', xy=(2010, ny_temps[0]), xytext=(2012, ny_temps[0] - 1),
             arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10, color='blue')
plt.annotate('Increase', xy=(2015, la_temps[5]), xytext=(2015, la_temps[5] + 1),
             arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10, color='green')
plt.annotate('Polar Vortex', xy=(2014, chicago_temps[4]), xytext=(2016, chicago_temps[4] + 1),
             arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10, color='red')

plt.title('Temperature Changes (2010-2020)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Avg Temp (°C)', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(8, 21, 1))

# Randomizing some stylistic grid and legend elements
plt.grid(False)
plt.legend(loc='lower right', fontsize=10, title='Cities', title_fontsize='12')

plt.tight_layout()
plt.show()