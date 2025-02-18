import matplotlib.pyplot as plt
import numpy as np

# Constructing the data for temperature readings over a week in degrees Celsius
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
year_2022_temps = [30, 32, 31, 29, 28, 29, 30]
year_2023_temps = [32, 33, 34, 32, 31, 30, 33]

# Create the figure and a set of subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the line charts for temperature variations in 2022 and 2023
ax.plot(days, year_2022_temps, marker='o', linestyle='-', color='blue')
ax.plot(days, year_2023_temps, marker='v', linestyle='--', color='green')

# Remove textual elements
ax.set_title("")
ax.set_xlabel('')
ax.set_ylabel('')

# Remove annotations
# Remove the legend
ax.legend().set_visible(False)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.6)

# Automatically adjust the layout
plt.tight_layout()

# Display the chart
plt.show()