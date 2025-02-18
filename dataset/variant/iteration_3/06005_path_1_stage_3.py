import matplotlib.pyplot as plt
import numpy as np

# Data for temperature readings over a week in degrees Celsius
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Altered temperature data for 2022 and 2023 while preserving the original structure
year_2022_temps = [32, 31, 30, 29, 28, 30, 29]  # Random shuffle of 2022 data
year_2023_temps = [31, 34, 32, 33, 30, 32, 33]  # Random shuffle of 2023 data

fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the line charts for temperature variations in 2022 and 2023
ax.plot(days, year_2022_temps, marker='o', linestyle='-', color='blue')
ax.plot(days, year_2023_temps, marker='v', linestyle='--', color='green')

# Automatically adjust the layout
plt.tight_layout()

# Display the chart
plt.show()