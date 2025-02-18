import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing Monthly Temperature Trends for Five Coastal Cities Over One Year
# Cities: San Francisco, New York, Miami, Seattle, and San Diego

# Define the months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Define fictional average monthly temperatures for each city (in Celsius)
san_francisco_temps = np.array([10, 12, 14, 15, 17, 18, 19, 19, 20, 18, 15, 12])
new_york_temps = np.array([0, 1, 5, 10, 16, 20, 24, 24, 20, 15, 10, 5])
miami_temps = np.array([20, 22, 24, 26, 28, 30, 32, 32, 30, 28, 25, 22])
seattle_temps = np.array([5, 6, 9, 12, 15, 18, 20, 21, 18, 13, 9, 5])
san_diego_temps = np.array([13, 14, 15, 17, 19, 21, 22, 22, 21, 19, 16, 14])

# Create a figure and axis for the line plot
plt.figure(figsize=(14, 8))

# Plotting average temperatures for each city
plt.plot(months, san_francisco_temps, marker='o', linestyle='-', label='San Francisco', color='orange')
plt.plot(months, new_york_temps, marker='s', linestyle='-', label='New York', color='blue')
plt.plot(months, miami_temps, marker='^', linestyle='-', label='Miami', color='green')
plt.plot(months, seattle_temps, marker='D', linestyle='-', label='Seattle', color='purple')
plt.plot(months, san_diego_temps, marker='x', linestyle='-', label='San Diego', color='red')

# Titles and labels
plt.title('Monthly Temperature Trends in Coastal Cities\nAn Analysis of 2022', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

# Customize the grid and appearance
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Cities', title_fontsize=12, fontsize=10, loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()