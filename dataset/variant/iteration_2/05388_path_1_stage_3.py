import matplotlib.pyplot as plt
import numpy as np

# Cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Years
years = np.arange(2010, 2021)

# Average temperatures in Fahrenheit (altered data)
ny_temps = [82, 79, 80, 78, 81, 74, 83, 76, 75, 82, 77]
la_temps = [79, 76, 80, 78, 81, 72, 82, 75, 77, 74, 73]
chi_temps = [71, 78, 72, 79, 80, 76, 77, 75, 74, 73, 70]
hou_temps = [85, 90, 86, 91, 89, 92, 87, 94, 88, 84, 93]
phx_temps = [108, 102, 106, 110, 104, 100, 107, 101, 105, 109, 103]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature trends without any labels or annotations
ax.plot(years, ny_temps, marker='o', color='#9467bd', linewidth=2)
ax.plot(years, la_temps, marker='s', color='#1f77b4', linewidth=2)
ax.plot(years, chi_temps, marker='^', color='#d62728', linewidth=2)
ax.plot(years, hou_temps, marker='d', color='#ff7f0e', linewidth=2)
ax.plot(years, phx_temps, marker='p', color='#2ca02c', linewidth=2)

# Enable grid
ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()