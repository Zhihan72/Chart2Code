import matplotlib.pyplot as plt
import numpy as np

# Define years (for x-axis)
years = np.arange(2010, 2020)

# Data on various metrics
residential_population = [1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.3, 2.5, 2.9, 3.1]
green_space = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100]  # in square kilometers
public_transport_usage = [100, 110, 120, 150, 160, 170, 175, 180, 185, 190]  # in millions of rides/year
energy_consumption = [5.0, 5.1, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6]  # in terawatt-hours
average_commute_time = [40, 38, 37, 35, 33, 32, 30, 29, 28, 27]  # in minutes

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the different metrics over the years
ax.plot(years, residential_population, marker='o')
ax.plot(years, green_space, marker='s')
ax.plot(years, public_transport_usage, marker='^')
ax.plot(years, energy_consumption, marker='d')
ax.plot(years, average_commute_time, marker='x')

# Customizing x-ticks
plt.xticks(years, fontsize=12, rotation=45)

# Customizing y-ticks
plt.yticks(fontsize=12)

# Enabling grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better presentation
plt.tight_layout()

# Display the plot
plt.show()