import matplotlib.pyplot as plt
import numpy as np

# Backstory: Historical Temperature Anomalies from 2000 to 2020
# The chart will show the changes in average global temperature anomalies from the year 2000 to 2020.
# This data is critical for understanding the impact of climate change over the years.

# Define years
years = np.arange(2000, 2021)

# Artificial data for temperature anomalies (in degrees Celsius)
# This data shows how much average global temperature deviated from the baseline (1951-1980 average)
temperature_anomalies = np.array([-0.2, -0.15, -0.1, 0.02, 0.1, 0.12, 0.18, 0.22, 0.3, 0.35, 
                         0.38, 0.4, 0.5, 0.55, 0.57, 0.62, 0.65, 0.68, 0.7, 0.75, 0.8])

# Colors for the different levels of temperature anomalies
colors = np.where(temperature_anomalies < 0, 'blue', 'red')

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature anomalies with suitable design details
ax.plot(years, temperature_anomalies, marker='o', linestyle='-', color='black', linewidth=2, markersize=8, label='Temperature Anomalies')

# Fill under the curve with conditional coloring
ax.fill_between(years, temperature_anomalies, where=(temperature_anomalies < 0), color='blue', alpha=0.3, interpolate=True)
ax.fill_between(years, temperature_anomalies, where=(temperature_anomalies >= 0), color='red', alpha=0.3, interpolate=True)

# Title and labels
ax.set_title("Historical Global Temperature Anomalies (2000-2020)\nData Reflecting Changes Relative to 1951-1980 Average", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Temperature Anomalies (°C)", fontsize=14)

# Customizing x and y axis ticks
ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_yticks(np.arange(-0.2, 0.9, 0.1))
ax.grid(True, linestyle='--', alpha=0.7)

# Adding a legend
ax.legend(loc="upper left", fontsize=12)

# Highlighting significant points
significant_points = [2003, 2012, 2016, 2020]
for sp in significant_points:
    sp_index = np.where(years == sp)[0][0]
    ax.annotate(f'{temperature_anomalies[sp_index]:.2f}°C', 
                xy=(sp, temperature_anomalies[sp_index]), 
                xytext=(sp+0.5, temperature_anomalies[sp_index]+0.15),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=12, fontweight='bold')

# Automatic layout adjustment
plt.tight_layout()

# Show the plot
plt.show()