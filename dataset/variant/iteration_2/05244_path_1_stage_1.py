import numpy as np
import matplotlib.pyplot as plt

# Define decades
years = np.arange(1920, 2021, 10)

# Temperature anomalies data (in °C)
northern_hemisphere = [-0.1, -0.2, -0.3, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
tropical_regions = [0.1, 0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9, 1.0, 1.1]
southern_hemisphere = [-0.2, -0.3, -0.2, 0.0, 0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9]

# Create a figure for the line chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the lines
ax.plot(years, northern_hemisphere, marker='o', linestyle='-', color='#FF4500', linewidth=2)
ax.plot(years, tropical_regions, marker='^', linestyle='--', color='#32CD32', linewidth=2)
ax.plot(years, southern_hemisphere, marker='s', linestyle='-.', color='#1E90FF', linewidth=2)

# Title and labels
ax.set_title('Temperature Anomalies Over the Last Century\nAcross Different Regions', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=14)

# Setting x-ticks for better clarity
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Customize the plot area background (optional, but keeping it light if necessary)
plt.gca().set_facecolor('white')

# Adjust layout automatically
plt.tight_layout()

# Show the plot
plt.show()