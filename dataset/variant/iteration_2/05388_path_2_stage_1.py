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

# Plot the temperature trends
ax.plot(years, ny_temps, marker='o', label='New York', color='#1f77b4', linewidth=2)
ax.plot(years, la_temps, marker='s', label='Los Angeles', color='#ff7f0e', linewidth=2)
ax.plot(years, chi_temps, marker='^', label='Chicago', color='#2ca02c', linewidth=2)
ax.plot(years, hou_temps, marker='d', label='Houston', color='#d62728', linewidth=2)
ax.plot(years, phx_temps, marker='p', label='Phoenix', color='#9467bd', linewidth=2)

# Remove title and axis labels
# ax.set_title(...)
# ax.set_xlabel(...)
# ax.set_ylabel(...)

# Remove annotations
# ax.annotate(...)

# Label each data point with its value - removed
# for idx, year in enumerate(years):
#     ax.text(...)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Enable grid
ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()