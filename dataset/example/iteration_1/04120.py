import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The script visualizes the historical average temperature changes in three cities over a decade. 
# The cities monitored are New York, Los Angeles, and Chicago from 2010 to 2020.
# This study shows how temperatures have been changing due to climate variations.

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average annual temperatures in Celsius for each city over time
ny_temps = np.array([9.7, 10.2, 10.0, 9.8, 10.1, 10.3, 10.5, 10.6, 10.9, 11.0, 11.2])
la_temps = np.array([17.5, 17.8, 17.9, 18.1, 18.2, 18.4, 18.5, 18.7, 18.8, 19.0, 19.2])
chicago_temps = np.array([8.5, 8.6, 8.8, 9.0, 9.1, 9.3, 9.4, 9.5, 9.8, 10.0, 10.2])

# Plotting
plt.figure(figsize=(12, 7))

# Plotting the temperature lines for each city
plt.plot(years, ny_temps, marker='o', label='New York', linestyle='-', linewidth=2, color='blue')
plt.plot(years, la_temps, marker='s', label='Los Angeles', linestyle='--', linewidth=2, color='red')
plt.plot(years, chicago_temps, marker='^', label='Chicago', linestyle='-.', linewidth=2, color='green')

# Adding annotations for significant events
plt.annotate('Start of Steady Increase', xy=(2010, ny_temps[0]), xytext=(2012, ny_temps[0] - 1),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')

plt.annotate('Steady Increase', xy=(2015, la_temps[5]), xytext=(2015, la_temps[5] + 1),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, color='red')

plt.annotate('2014 Polar Vortex', xy=(2014, chicago_temps[4]), xytext=(2016, chicago_temps[4] + 1),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green')

# Chart detailed labels and title
plt.title('Decade-long Average Temperature Changes (2010-2020)\n New York, Los Angeles, and Chicago', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Annual Temperature (°C)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(8, 21, 1))

# Adding a grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a legend to distinguish the cities
plt.legend(loc='upper left', fontsize=10, title='Cities', title_fontsize='13')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()