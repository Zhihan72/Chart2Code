import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are analyzing the temperature variations throughout a week in a fictional tropical city called Tropica,
# focusing on the differences between two recent years: 2022 and 2023.

# Constructing the data for temperature readings over a week in degrees Celsius
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
year_2022_temps = [30, 32, 31, 29, 28, 29, 30]
year_2023_temps = [32, 33, 34, 32, 31, 30, 33]

# Create the figure and a set of subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the line charts for temperature variations in 2022 and 2023
ax.plot(days, year_2022_temps, marker='o', linestyle='-', color='blue', label='Temperature 2022')
ax.plot(days, year_2023_temps, marker='v', linestyle='--', color='green', label='Temperature 2023')

# Titles and labels
ax.set_title("Weekly Temperature Variations in Tropica\nComparing 2022 and 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Days of the Week', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

# Adding annotations at each data point for clarity
for i, temp in enumerate(year_2022_temps):
    ax.annotate(f'{temp}°C', xy=(days[i], temp), xytext=(5, 5), textcoords='offset points', fontsize=10, color='blue')

for i, temp in enumerate(year_2023_temps):
    ax.annotate(f'{temp}°C', xy=(days[i], temp), xytext=(5, -15), textcoords='offset points', fontsize=10, color='green')

# Adding a legend
ax.legend(loc='upper right', fontsize=12, frameon=False)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.6)

# Automatically adjust the layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()