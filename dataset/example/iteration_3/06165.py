import matplotlib.pyplot as plt
import numpy as np

# Contextual backstory:
# "Observing Temperature Trends Over a Decade: An Analysis of Monthly Averages in Springfield"

# Data setup
years = np.arange(2010, 2020)
months = range(1, 13)

# Mock data of monthly average temperatures for each year in Springfield
# Here each row represents a year and each column represents a month
temperature_data = [
    [30.5, 32.1, 45.2, 55.3, 65.2, 75.1, 80.0, 78.9, 70.3, 59.2, 45.1, 35.4], # 2010
    [31.2, 33.0, 46.5, 56.0, 66.1, 76.0, 80.3, 79.5, 71.1, 60.0, 46.0, 36.0], # 2011
    [30.8, 32.5, 45.7, 55.8, 65.8, 75.7, 80.5, 79.0, 70.8, 59.8, 45.9, 35.8], # 2012
    [31.0, 33.2, 46.3, 56.3, 66.5, 76.5, 81.0, 79.7, 71.5, 60.5, 46.5, 36.3], # 2013
    [30.9, 32.8, 45.9, 55.6, 65.9, 75.6, 80.8, 78.8, 70.6, 59.5, 45.6, 35.7], # 2014
    [31.5, 33.5, 46.8, 56.8, 66.8, 76.8, 81.5, 80.0, 71.8, 60.8, 46.8, 36.8], # 2015
    [31.8, 33.9, 47.2, 57.2, 67.2, 77.2, 82.0, 80.5, 72.2, 61.2, 47.2, 37.2], # 2016
    [32.0, 34.0, 47.5, 57.5, 67.5, 77.5, 82.5, 81.0, 73.0, 62.0, 47.5, 37.5], # 2017
    [32.3, 34.3, 48.0, 58.0, 68.0, 78.0, 83.0, 81.5, 73.5, 62.5, 48.0, 38.0], # 2018
    [32.5, 34.5, 48.5, 58.5, 68.5, 78.5, 83.5, 82.0, 74.0, 63.0, 48.5, 38.5]  # 2019
]

# Convert to Numpy array for easier indexing
temperature_data = np.array(temperature_data)

# Create the plot
plt.figure(figsize=(14, 8))

# Plot individual lines for each year
for i, year in enumerate(years):
    plt.plot(months, temperature_data[i], marker='o', linestyle='-', label=str(year))

# Plot enhancements
plt.title("Observing Temperature Trends Over a Decade:\nAn Analysis of Monthly Averages in Springfield", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Temperature (°F)", fontsize=12)
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend
plt.legend(title='Year', loc="upper left", fontsize='small')

# Use tight_layout to automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()