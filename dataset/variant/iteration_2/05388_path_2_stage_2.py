import matplotlib.pyplot as plt
import numpy as np

# Cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Years
years = np.arange(2010, 2021)

# Average temperatures in Fahrenheit
ny_temps = [74, 75, 76, 77, 78, 79, 80, 81, 82, 82, 83]
la_temps = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]
chi_temps = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
hou_temps = [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]
phx_temps = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature trends with new set of colors
ax.plot(years, ny_temps, marker='o', label='New York', color='teal', linewidth=2)
ax.plot(years, la_temps, marker='s', label='Los Angeles', color='gold', linewidth=2)
ax.plot(years, chi_temps, marker='^', label='Chicago', color='mediumvioletred', linewidth=2)
ax.plot(years, hou_temps, marker='d', label='Houston', color='darkorange', linewidth=2)
ax.plot(years, phx_temps, marker='p', label='Phoenix', color='navy', linewidth=2)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Enable grid
ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()