import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart depicts the historical climate data for a fictional town called "GreenValley".
# The data focuses on the temperatures recorded in GreenValley over the four seasons from 2015 through 2021.

# Data: Annual average temperatures in GreenValley for each season from 2015 to 2021
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021])
spring_temps = np.array([15.2, 15.8, 16.3, 16.9, 17.2, 17.6, 18.1])
summer_temps = np.array([23.4, 24.1, 24.5, 25.0, 25.3, 25.9, 26.2])
autumn_temps = np.array([17.8, 18.2, 18.7, 19.0, 19.2, 19.6, 20.0])
winter_temps = np.array([5.3, 5.7, 6.1, 6.5, 6.8, 7.2, 7.5])

# Colors for the seasons
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

# Create the main plot
plt.figure(figsize=(14, 8))

# Plotting the average temperatures for each season with different colors
plt.plot(years, spring_temps, color=colors[0], marker='o', linestyle='-', linewidth=2, markersize=6, label='Spring')
plt.plot(years, summer_temps, color=colors[1], marker='o', linestyle='-', linewidth=2, markersize=6, label='Summer')
plt.plot(years, autumn_temps, color=colors[2], marker='o', linestyle='-', linewidth=2, markersize=6, label='Autumn')
plt.plot(years, winter_temps, color=colors[3], marker='o', linestyle='-', linewidth=2, markersize=6, label='Winter')

# Enhancing the title and labels
plt.title('Climate Trends in GreenValley:\nAverage Seasonal Temperatures (2015-2021)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

# Adding grid for better visibility
plt.grid(True, linestyle='--', alpha=0.5)

# Adding a legend to differentiate the seasons, positioned to avoid collision
plt.legend(loc='upper left', title="Seasons", fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(years)

# Use tight layout to ensure elements are not overlapping
plt.tight_layout()

# Display the plot
plt.show()