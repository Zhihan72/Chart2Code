import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# Temperature anomalies over the past century in three different regions: 
# Northern Hemisphere, Tropical Regions, and Southern Hemisphere.
# The data represents temperature deviations from the 20th-century average.

# Define decades
years = np.arange(1920, 2021, 10)

# Temperature anomalies data (in °C)
northern_hemisphere = [-0.1, -0.2, -0.3, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
tropical_regions = [0.1, 0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9, 1.0, 1.1]
southern_hemisphere = [-0.2, -0.3, -0.2, 0.0, 0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9]

# Create a figure for the line chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the lines
ax.plot(years, northern_hemisphere, marker='o', linestyle='-', color='#FF4500', linewidth=2, label='Northern Hemisphere')
ax.plot(years, tropical_regions, marker='^', linestyle='--', color='#32CD32', linewidth=2, label='Tropical Regions')
ax.plot(years, southern_hemisphere, marker='s', linestyle='-.', color='#1E90FF', linewidth=2, label='Southern Hemisphere')

# Title and labels
ax.set_title('Temperature Anomalies Over the Last Century\nAcross Different Regions', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=14)

# Adding grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)

# Setting x-ticks for better clarity
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adding legend
ax.legend(loc='upper left', title='Regions', fontsize=12)

# Adding reference lines for 0°C anomaly
ax.axhline(0, color='gray', linewidth=1.5, linestyle='--', alpha=0.6)

# Annotating key points
ax.annotate('Sharp increase in NH temperatures',
             xy=(1980, 0.4), xytext=(1960, 0.8),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Consistent rise in Tropical temperatures',
             xy=(1990, 0.7), xytext=(1970, 1.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Customize the plot area background
plt.gca().set_facecolor('#f7f7f7')

# Adjust layout automatically
plt.tight_layout()

# Show the plot
plt.show()