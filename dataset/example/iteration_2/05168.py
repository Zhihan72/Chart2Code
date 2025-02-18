import matplotlib.pyplot as plt
import numpy as np

# Title and backstory
# This line chart represents a fictional data about the temperature variation throughout the week in three different cities.
# The data provides insights into how the temperature changes from Monday to Sunday in New York, San Francisco, and Miami.
title = "Weekly Temperature Variation in Three Cities"
subtitle = "New York, San Francisco, and Miami"
x_label = "Days of the Week"
y_label = "Temperature (°F)"

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Temperature data for three cities
new_york_temp = [55, 60, 58, 62, 65, 63, 61]          # Temperatures in New York
san_francisco_temp = [50, 52, 54, 53, 55, 56, 57]    # Temperatures in San Francisco
miami_temp = [75, 77, 76, 78, 80, 81, 82]            # Temperatures in Miami

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the temperature data
ax.plot(days, new_york_temp, marker='o', linestyle='-', color='b', label='New York')
ax.plot(days, san_francisco_temp, marker='s', linestyle='--', color='g', label='San Francisco')
ax.plot(days, miami_temp, marker='^', linestyle=':', color='r', label='Miami')

# Title and labels
plt.title(f"{title}\n{subtitle}", fontsize=16, fontweight='bold')
plt.xlabel(x_label, fontsize=14)
plt.ylabel(y_label, fontsize=14)

# Add a grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add a legend
plt.legend(loc='upper left', fontsize=12, title="Cities", title_fontsize='13')

# Annotating specific points of interest, e.g., highest temperature day in Miami
max_temp_miami = max(miami_temp)
max_temp_day = days[miami_temp.index(max_temp_miami)]
plt.annotate(f'Highest Temp: {max_temp_miami}°F',
             xy=(max_temp_day, max_temp_miami),
             xytext=(max_temp_day, max_temp_miami + 5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

# Tight layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()