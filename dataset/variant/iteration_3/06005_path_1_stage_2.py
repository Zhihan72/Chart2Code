import matplotlib.pyplot as plt
import numpy as np

# Data for temperature readings over a week in degrees Celsius
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
year_2022_temps = [30, 32, 31, 29, 28, 29, 30]
year_2023_temps = [32, 33, 34, 32, 31, 30, 33]

fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the line charts for temperature variations in 2022 and 2023
ax.plot(days, year_2022_temps, marker='o', linestyle='-', color='blue')
ax.plot(days, year_2023_temps, marker='v', linestyle='--', color='green')

# Removing the grid lines
ax.grid(False)

# Automatically adjust the layout
plt.tight_layout()

# Display the chart
plt.show()